from helpers.calculate_parameters import *
import numpy as np
import sqlite3


class Read:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()

    def connect_to_database(self):
        connection = sqlite3.connect("{}.db".format(self.db_name))
        return connection

    def get_rows_count(self):
        count = self.cursor.execute("SELECT COUNT(measurement_id) FROM metadata;")
        return count.fetchall()[0][0]

    def fetch_joint(self, headers):
        # Otherwise, a possibility of ambigous column names (two tables) exists.
        headers = [
            header.replace("measurement_id", "metadata.measurement_id")
            for header in headers
        ]

        query = query = """
        SELECT {} 
        FROM metadata 
        INNER JOIN stats ON metadata.measurement_id=stats.measurement_id
        """.format(
            ",".join(headers)
        )
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
            # If a sign passed (">", "<" or "=").
            if type(value) == list:
                base = "{}{}{}".format(key, value[0], value[1])
            # SQL queries require quotation marks.
            elif type(value) == str:
                base = "{}='{}'".format(key, value)
            else:
                base = "{}={}".format(key, value)

            # If not the last argument.
            if counter != len(kwargs):
                query_part_1 += "metadata.{}, ".format(key)
                query_part_2 += base + " AND "
            else:
                query_part_1 += "metadata.{} ".format(key)
                query_part_2 += base + ";"

            counter += 1

        query = query_part_1 + query_part_2

        return self.cursor.execute(query)

    def get_unique_values(self, column):
        query = "SELECT DISTINCT {} FROM metadata;".format(column)
        unique = []
        results = self.cursor.execute(query)
        for result in results.fetchall():
            unique.append(result[0])

        return unique

    def get_report_name(self, measurement_id):
        query = (
            f"SELECT report_name FROM metadata WHERE measurement_id={measurement_id};"
        )
        results = self.cursor.execute(query).fetchall()  # returns: [('report_name')]
        report_name = results[0][0]
        return report_name
