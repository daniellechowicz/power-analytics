from helpers.calculate_parameters import *
import matplotlib.pyplot as plt
import numpy as np
import sqlite3


class Read:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()

    def connect_to_database(self):
        connection = sqlite3.connect("{}.db".format(self.db_name))
        print(
            "[INFO] new connection {} has been opened successfully".format(connection)
        )

        return connection

    def get_rows_count(self):
        count = self.cursor.execute("SELECT COUNT(measurement_id) FROM metadata;")

        return count.fetchall()[0][0]

    def fetch_joint(self, headers):
        # Otherwise, a possibility of ambigous column names (two tables)
        headers = [
            header.replace("measurement_id", "metadata.measurement_id")
            for header in headers
        ]

        # Create a query
        query = query = """
        SELECT {} 
        FROM metadata 
        INNER JOIN stats ON metadata.measurement_id=stats.measurement_id
        """.format(
            ",".join(headers)
        )

        # Execute the query
        results_ = self.cursor.execute(query)
        results = []
        for result in results_.fetchall():
            results.append(result)

        return results

    def fetch(self, **kwargs):
        query_part_1 = """
        SELECT 
            stats.mean, 
        """
        query_part_2 = """
        FROM metadata
        INNER JOIN stats ON metadata.measurement_id=stats.measurement_id
        WHERE
        """
        counter = 1
        for key, value in kwargs.items():
            # If a sign passed (">", "<" or "=")
            if type(value) == list:
                base = "{}{}{}".format(key, value[0], value[1])
            # SQL queries require quotation marks
            elif type(value) == str:
                base = "{}='{}'".format(key, value)
            else:
                base = "{}={}".format(key, value)

            # If not the last argument
            if counter != len(kwargs):
                query_part_1 += "metadata.{}, ".format(key)
                query_part_2 += base + " AND "
            else:
                query_part_1 += "metadata.{} ".format(key)
                query_part_2 += base + ";"

            counter += 1

        query = query_part_1 + query_part_2

        return self.cursor.execute(query)

    def get_mean_values(self, results):
        arr = []
        for result in results.fetchall():
            arr.append(result[0])

        return np.array(arr)

    def get_unique_values(self, column):
        query = "SELECT DISTINCT {} FROM metadata;".format(column)
        unique = []
        results = self.cursor.execute(query)
        for result in results.fetchall():
            unique.append(result[0])

        return unique

    def group_by(self, column, params):
        unique_values = self.get_unique_values(column)
        dataset = {}
        for value in unique_values:
            # Change predefined value to the current value
            params[column] = value

            # Set parameters that need to be calculated separately
            params["cutting_speed"] = get_cutting_speed(
                float(params["tool_diameter"]), float(params["rotational_speed"])
            )

            params["feed_per_tooth"] = get_feed_per_tooth(
                float(params["feed_speed"]),
                float(params["rotational_speed"]),
                int(params["total_no_of_wings"]),
            )

            params["mean_chip_thickness"] = get_mean_chip_thickness(
                float(params["cutting_angle"]),
                float(params["tool_diameter"]),
                float(params["cutting_depth"]),
                float(params["feed_per_tooth"]),
            )

            params["mean_chip_length"] = get_mean_chip_length(
                float(params["tool_diameter"]), float(params["cutting_depth"])
            )

            for key in params.keys():
                if key in [
                    "material",
                    "cutting_direction",
                    "tool_id",
                    "cutting_material",
                    "body_material",
                ]:
                    params[key] = str(params[key])
                else:
                    params[key] = float(params[key])

            # Fetch results from the database based on "params" variable
            results = self.fetch(
                material=list(params.values())[0],
                moisture_content=float(list(params.values())[1]),
                cutting_direction=list(params.values())[2],
                rotational_speed=float(list(params.values())[3]),
                feed_speed=float(list(params.values())[4]),
                feed_per_tooth=float(list(params.values())[5]),
                cutting_speed=float(list(params.values())[6]),
                cutting_width=float(list(params.values())[7]),
                cutting_depth=float(list(params.values())[8]),
                cutting_angle=float(list(params.values())[9]),
                mean_chip_thickness=float(list(params.values())[10]),
                mean_chip_length=float(list(params.values())[11]),
                tool_id=list(params.values())[12],
                tool_diameter=float(list(params.values())[13]),
                tool_cutting_width=float(list(params.values())[14]),
                no_of_wings=float(list(params.values())[15]),
                total_no_of_wings=float(list(params.values())[16]),
                cutting_material=list(params.values())[17],
                body_material=list(params.values())[18],
                rake_angle=float(list(params.values())[19]),
            )
            arr = self.get_mean_values(results)
            dataset["{}".format(value)] = arr

        return dataset

    def group_by_material(self):
        unique_values = self.get_unique_values("material")
        dataset = {}
        for value in unique_values:
            results = self.fetch(
                material=value,
            )
            arr = self.get_mean_values(results)
            dataset["{}".format(value)] = arr

        return dataset

    def group_by_moisture_content(self):
        unique_values = self.get_unique_values("moisture_content")
        dataset = {}
        for value in unique_values:
            results = self.fetch(
                moisture_content=value,
            )
            arr = self.get_mean_values(results)
            dataset["{}".format(value)] = arr

        return dataset

    def group_by_cutting_direction(self):
        unique_values = self.get_unique_values("cutting_direction")
        dataset = {}
        for value in unique_values:
            results = self.fetch(
                cutting_direction=value,
            )
            arr = self.get_mean_values(results)
            dataset["{}".format(value)] = arr

        return dataset

    def group_by_feed_speed(self):
        unique_values = self.get_unique_values("feed_speed")
        dataset = {}
        for value in unique_values:
            results = self.fetch(
                feed_speed=value,
            )
            arr = self.get_mean_values(results)
            dataset["{}".format(value)] = arr

        return dataset

    def group_by_cutting_speed(self):
        unique_values = self.get_unique_values("cutting_speed")
        dataset = {}
        for value in unique_values:
            results = self.fetch(
                cutting_speed=value,
            )
            arr = self.get_mean_values(results)
            dataset["{}".format(value)] = arr

        return dataset

    def group_by_cutting_depth(self):
        unique_values = self.get_unique_values("cutting_depth")
        dataset = {}
        for value in unique_values:
            results = self.fetch(
                cutting_depth=value,
            )
            arr = self.get_mean_values(results)
            dataset["{}".format(value)] = arr

        return dataset
