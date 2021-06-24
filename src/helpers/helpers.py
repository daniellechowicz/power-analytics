from bisect import bisect_left, insort
from collections import deque
from itertools import islice
from nptdms import TdmsFile
from settings import *
import ctypes
import numpy as np


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
            "Power Analytics | Datenimport",
            0 | 0x40,
        )

    return CHANNEL_NAME


def get_labels():
    labels = {
        "material": "Werkstoff",
        "moisture_content": "Feuchtegehalt [%]",
        "cutting_direction": "Schnittrichtung",
        "rotational_speed": "Drehzahl [U/min]",
        "feed_speed": "Vorschubgeschwindigkeit [m/min]",
        "feed_per_tooth": "Zahnvorschub [mm]",
        "cutting_speed": "Schnittgeschwindigkeit [m/s]",
        "cutting_width": "SB - Werkstück [mm]",
        "cutting_depth": "Schnitttiefe [mm]",
        "shear_angle": "Achswinkel λ [°]",
        "mean_chip_thickness": "Mittlere Spandicke [mm]",
        "mean_chip_length": "Mittlere Spanlänge [mm]",
        "tool_id": "Werkzeug-ID",
        "tool_diameter": "Werkzeugdurchmesser [mm]",
        "tool_cutting_width": "Schneidenbreite [mm]",
        "bore_diameter": "Bohrungsdurchmesser [mm]",
        "no_of_wings": "Schneidenzahl",
        "total_no_of_wings": "Gesamtschneidenzahl",
        "cutting_material": "Schneidenwerkstoff",
        "body_material": "Grundkörpermaterial",
        "rake_angle": "Spanwinkel γ [°]",
    }
    return labels


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

    # Just in case if there are dots as well (e.g. "Max. N [1/min]")
    text = text.replace(".", "")

    # For "number_of_wings" and "total_number_of_wings"
    if "number" in text:
        text = text.replace("number", "no")

    return text


def moving_median(data, window_size):
    seq = iter(data)
    d = deque()
    s = []
    y_vector = []
    for item in islice(seq, window_size):
        d.append(item)
        insort(s, item)
        y_vector.append(s[len(d) // 2])

    m = window_size // 2

    for item in seq:
        old = d.popleft()
        d.append(item)
        del s[bisect_left(s, old)]
        insort(s, item)
        y_vector.append(s[m])

    x_vector = np.linspace(0, len(y_vector) / SAMPLING_RATE, len(y_vector))

    return x_vector, y_vector


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
