import datetime
import json
import os


with open("pkgs/src/settings.json") as json_file:
    settings = json.load(json_file)

GROUP_NAME = "Leistungsmessung\nVerstärkungsfaktor Spindelleistung 20,426"
CHANNEL_NAME = settings["channel_name"]
FONTSIZE = settings["fontsize"]
FONTSIZE_REPORT = settings["fontsize_report"]
RESOLUTION = settings["resolution"]
SAMPLING_RATE = settings["sampling_rate"]
RESAMPLE_FACTOR = settings["resample_factor"]
CUTOFF_FREQUENCY = settings["cutoff_frequency"]
ORDER = settings["order"]
WINDOW_SIZE = settings["window_size"]
IDLE_0 = settings["idle_0"]
IDLE_1 = settings["idle_1"]
CUTTING_0 = settings["cutting_0"]
CUTTING_1 = settings["cutting_1"]
WINDOW_NAME = settings["window_name"]
DB_NAME = settings["db_name"]
DB_CSV_NAME = settings["db_csv_name"] + "_{}.csv".format(str(datetime.date.today()))
LEITZ_TOOLS = settings["leitz_tools"]
LEITZ_TOOLS_UPDATES = settings["leitz_tools_updates"]
SYMBOLS = settings["symbols"]
COLOURS = settings["colours"]
SYMBOL_SIZE = settings["symbol_size"]


def edit_settings(key, value):
    filename = "pkgs/src/settings.json"
    with open(filename, "r") as f:
        data = json.load(f)
        data[key] = value
    os.remove(filename)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
