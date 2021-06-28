from nptdms import TdmsFile
from settings import *
import ctypes
import numpy as np
import os
import json


def get_group_name(path):
    tdms_file = TdmsFile.read(path)
    group_name = tdms_file.groups()[0].name
    return group_name


def get_channel_name(path):
    tdms_file = TdmsFile.read(path)
    group_name = tdms_file.groups()[0].name
    group = tdms_file[group_name]
    channels = []
    available_channel_matches_settings = False
    for channel in group.channels():
        channels.append(channel.name)
        if channel.name == CHANNEL_NAME:
            available_channel_matches_settings = True
            return channel.name

    if not available_channel_matches_settings:
        ctypes.windll.user32.MessageBoxW(
            0,
            f"Die Kanäle {channels} sind verfügbar, es wurde jedoch {CHANNEL_NAME} gewählt. Ändern Sie die Einstellungen entsprechend der gefundenen Kanalnamen.",
            f"{Strings.APP_NAME} | {Strings.DIALOG_DATA_IMPORT}",
            0 | 0x40,
        )

    return CHANNEL_NAME


def get_key(d, val):
    """
    This function comes in handy when working with dictionaries.
    Having the value only, it allows to get corresponding key.
    """
    for key, value in d.items():
        if val == value:
            return key
    return None


def get_permission_dialog(text, title, utype):
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    msg_box = user32.MessageBoxW
    result = msg_box(None, text, title, utype)
    if not result:
        raise ctypes.WinError(ctypes.get_last_error())
    return result


def get_available_tool_ids():
    data = np.loadtxt(
        os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS),
        delimiter=DELIMITER,
        dtype=str,
        skiprows=1,
    )
    if len(data) == 0:
        ctypes.windll.user32.MessageBoxW(
            0,
            "Es sieht so aus, als ob die Datei mit den Tools leer ist. Bitte aktualisieren Sie diese zuerst und wiederholen Sie den Vorgang.",
            f"{Strings.APP_NAME} | {Strings.DIALOG_DATA_IMPORT}",
            0 | 0x40,
        )
        return None
    else:
        tool_ids = data[:, 0]
        return tool_ids


def get_full_name(column):
    """
    This function is used, among other things, by the database window to set full headers.
    """

    translations = {
        "measurement_id": "Mess-ID",
        "author": "Autor",
        "measurement_date": "Messzeitpunkt",
        "material": "Werkstoff",
        "moisture_content": "Feuchtegehalt [%]",
        "cutting_direction": "Schnittrichtung",
        "rotational_speed": "Drehzahl [U/min]",
        "feed_speed": "Vorschubgeschwindigkeit [m/min]",
        "feed_per_tooth": "Zahnvorschub [mm]",
        "cutting_speed": "Schnittgeschwindigkeit [m/s]",
        "cutting_width": "SB - Werkstück [mm]",
        "cutting_depth": "Schnitttiefe [mm]",
        "mean_chip_thickness": "Mittlere Spandicke [mm]",
        "mean_chip_length": "Mittlere Spanlänge [mm]",
        "tool_id": "Werkzeug-ID",
        "classification_number": "Klassifizierungsnummer",
        "strategic_business_unit": "Strategische Geschäftszahl",
        "tool_diameter": "Werkzeugdurchmesser [mm]",
        "tool_cutting_width": "Schneidenbreite [mm]",
        "bore_diameter": "Bohrungsdurchmesser [mm]",
        "no_of_wings": "Schneidenzahl",
        "total_no_of_wings": "Gesamtschneidenzahl",
        "cutting_material": "Schneidenwerkstoff",
        "cutting_material_quality": "PCD Qualität",
        "body_material": "Grundkörpermaterial",
        "n_max": "Max. Drehzahl [U/min]",
        "n_opt": "Optimale Drehzahl [U/min]",
        "rake_angle": "Spanwinkel γ [°]",
        "shear_angle": "Achswinkel λ [°]",
        "comments": "Kommentare",
        "min_idle": "Leerlauf - Minimale Leistungsaufnahme [kW]",
        "max_idle": "Leerlauf - Maximale Leistungsaufnahme [kW]",
        "mean_idle": "Leerlauf - Mittlere Leistungsaufnahme [kW]",
        "median_idle": "Leerlauf - Median der Leistungsaufnahme [kW]",
        "std_idle": "Leerlauf - Standardabweichung der Leistungsaufnahme [kW]",
        "min_cutting": "Bearbeitung inkl. Leerlauf - Minimale Leistungsaufnahme [kW]",
        "max_cutting": "Bearbeitung inkl. Leerlauf - Maximale Leistungsaufnahme [kW]",
        "mean_cutting": "Bearbeitung inkl. Leerlauf - Mittlere Leistungsaufnahme [kW]",
        "median_cutting": "Bearbeitung inkl. Leerlauf - Median der Leistungsaufnahme [kW]",
        "std_cutting": "Bearbeitung inkl. Leerlauf - Standardabweichung der Leistungsaufnahme [kW]",
        "mean_cutting_no_idle": "Bearbeitung ohne Leerlauf - Mittlere Leistungsaufnahme [kW]",
        "report_name": "Protokoll-Name",
    }
    return translations[column]


def translate(text):
    for i, char in enumerate(text):
        if char == "[":
            start = i

    try:
        text = text[:start]
    except:
        pass

    text = "".join(text.rstrip())
    text = text.lower().replace(" ", "_")

    # Just in case if there are dots as well (e.g. "Max. N [1/min]").
    text = text.replace(".", "")

    # For "number_of_wings" and "total_number_of_wings".
    if "number" in text:
        text = text.replace("number", "no")

    return text


def convert_type(key, value):
    if key in [
        "author",
        "date",
        "material",
        "cutting_direction",
        "tool_id",
        "comments",
    ]:
        return f"'{value}'"
    else:
        return value


def edit_settings(key, value):
    filename = "settings.json"
    with open(filename, "r") as f:
        data = json.load(f)
        data[key] = value
    os.remove(filename)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
