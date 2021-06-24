import pandas as pd


class Tools:
    def __init__(self, path, id):
        self.path = path
        self.id = id
        self.upload()

    def upload(self):
        self.df_params = pd.read_csv(self.path, delimiter=";")

    def get_headers(self):
        headers = self.df_params.columns.tolist()
        return headers

    # requirements: dict
    def extract(self, requirements):
        res = self.df_params.copy()
        for key, value in requirements.items():
            res = res.loc[res[key] == value]
        return res

    def find_by_id(self):
        id_header = "Identnummer"
        if id_header in self.get_headers():
            res = self.extract({id_header: "{}".format(self.id)})
            return res
        else:
            raise AssertionError(
                'No header called "{}" is present in the given file'.format(id_header)
            )

    def export(self):
        found = self.find_by_id()
        params = {
            "tool_id": self.id,
            "classification_no": found["Klassifizierungsnummer"],
            "strategic_business_unit": found["SGE"],
            "tool_diameter": found["D"],
            "tool_cutting_width": found["SB"],
            "bore_diameter": found["BO"],
            "no_of_wings": found["Z"],
            "total_no_of_wings": found["ZGE"],
            "cutting_material": found["QUALITAT"],
            "cutting_material_quality": found["COD"],
            "body_material": found["TKQ"],
            "n_max": found["NMAX"],
            "n_opt": found["NOPT"],
            "rake_angle": found["SW"],
            "shear_angle": found["AW"],
        }
        # To get rid of "name" and "dtype",
        # transform it to string and ignore index
        for key, value in params.items():
            try:
                params[key] = value.to_string(index=False)
            # e.g. "tool_id" does not use "find_by_id" function
            except:
                continue
        return params
