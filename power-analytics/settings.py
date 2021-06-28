from dataclasses import dataclass
import datetime
import json


with open("settings.json", encoding="utf8") as json_file:
    settings = json.load(json_file)


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
DELIMITER = settings["delimiter"]


@dataclass
class Strings:
    APP_NAME = "Power Analytics"
    ICON = "lighting.svg"
    DIALOG_DATABASE_EDIT = "Datenbank bearbeiten"
    DIALOG_DATABASE = "Datenbank"
    DIALOG_PARAMETERS = "Parameter"
    DIALOG_TOOLS = "Werkzeuge"
    DIALOG_VISUALIZATION = "Datenvisualisierung"
    DIRECTORY_DATABASE = "database"
    DIRECTORY_REPORT_MAIN = "report"
    DIRECTORY_REPORT_PDFS = "reports"
