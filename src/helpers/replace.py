from settings import *
import os
import pandas as pd


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
