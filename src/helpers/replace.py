from settings import *
import os
import pandas as pd
import shutil


class Replace:
    """
    This class is a set of functions responsible for
    changing the CSV file with tool parameters,
    as well as refreshing and changing parameters
    that have been updated manually.
    """

    def find_by_ID(self, file, tool_id):
        df = pd.read_csv(
            os.path.join("database", file), delimiter=";", keep_default_na=False
        )
        row = df.loc[df["Identnummer"] == tool_id]
        i = row.index[0]
        corresponding_params = {
            "Identnummer": row["Identnummer"][i],
            "Klassifizierungsnummer": row["Klassifizierungsnummer"][i],
            "SGE": row["SGE"][i],
            "D": row["D"][i],
            "SB": row["SB"][i],
            "BO": row["BO"][i],
            "Z": row["Z"][i],
            "QUALITAT": row["QUALITAT"][i],
            "COD": row["COD"][i],
            "TKQ": row["TKQ"][i],
            "NMAX": row["NMAX"][i],
            "NOPT": row["NOPT"][i],
            "SW": row["SW"][i],
        }

        return corresponding_params

    def edit_by_ID(self, tool_id, column_name, value):
        df = pd.read_csv(
            os.path.join("database", LEITZ_TOOLS), delimiter=";", keep_default_na=False
        )
        row = df.loc[df["Identnummer"] == tool_id]
        i = row.index[0]
        df.at[i, column_name] = value
        df.to_csv(os.path.join("database", LEITZ_TOOLS), sep=";", index=False)

    def get_updates(self, tool_id):
        # r1 - from file exported from the database
        # r2 - from file containing all the updates done
        r1 = self.find_by_ID(LEITZ_TOOLS, tool_id)
        try:
            r2 = self.find_by_ID(LEITZ_TOOLS_UPDATES, tool_id)
        except:
            return None

        updates = dict()
        for key, value in r1.items():
            # If an update was detected, then...
            if r1[key] != r2[key]:
                # What was changed? -> key
                # New file's value -> r1[key]
                # The last value -> r2[key]
                updates[key] = r2[key]
            else:
                pass

        return updates

    def update_replaced_CSV(self):
        """
        This function updates individual values. In contrary to "copy_new_tools_to_main" function,
        it only works when a particular ID was found both in "tools.csv" and "tools_updates.csv"
        """
        path = os.path.join("database", LEITZ_TOOLS)
        tools = pd.read_csv(path, delimiter=";")
        for tool_id in tools["Identnummer"]:
            updates = self.get_updates(tool_id)
            # If no updates were ever perform, then just pass...
            if updates != None:
                for column_name, value in updates.items():
                    self.edit_by_ID(tool_id, column_name, value)
                    # print(column_name, value)
            else:
                pass

    import pandas as pd

    def get_all_ids_from_main(self):
        """
        This function is responsible for getting all the IDs from the file "tools.csv"
        """
        data = pd.read_csv(os.path.join("database", LEITZ_TOOLS), delimiter=";")
        ids = []
        for d in data["Identnummer"]:
            ids.append(d)
        return ids

    def get_all_ids_from_updates(self):
        """
        This function is responsible for getting all the IDs from the file "tools_updates.csv"
        """
        data = pd.read_csv(os.path.join("database", LEITZ_TOOLS_UPDATES), delimiter=";")
        ids = []
        for d in data["Identnummer"]:
            ids.append(d)
        return ids

    def copy_new_tools_to_main(self):
        """
        This function works as follows:
        1. Get all the IDs from "tools.csv"
        2. Get all the IDs from "tools_updates.csv"
        3. If ID from "tools_updates.csv" was not found in the main CSV file,
        then write the corresponding line to "tools.csv"
        """
        ids_main = self.get_all_ids_from_main()
        ids_updates = self.get_all_ids_from_updates()
        for id in ids_updates:
            if id not in ids_main:
                file_updates = open(os.path.join("database", LEITZ_TOOLS_UPDATES), "r")
                found = False
                while not found:
                    line = file_updates.readline()
                    if str(id) in str(line):
                        found = True
                        file = open(os.path.join("database", LEITZ_TOOLS), "a")
                        file.write(line)
                        file.close()

    def replace_unwanted_chars(self):
        """
        Why? Sometimes "," instead of ".".
        """
        shutil.copy(os.path.join("database", LEITZ_TOOLS), os.path.join("database", "temp.csv"))
        # Input file.
        fin = open(os.path.join("database", LEITZ_TOOLS), "rt")
        # Output file to write the result to.
        fout = open(os.path.join("database", "temp.csv"), "wt")
        for line in fin:
            fout.write(line.replace(',', '.'))
        # Close input and output files.
        fin.close()
        fout.close()

        os.remove(os.path.join("database", LEITZ_TOOLS))
        os.rename(os.path.join("database", "temp.csv"), os.path.join("database", LEITZ_TOOLS))