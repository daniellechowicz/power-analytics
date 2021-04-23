from bisect import bisect_left, insort
from collections import deque
from itertools import islice
from src.settings import *
import numpy as np


def get_labels():
    labels = {
        "material": "Species",
        "moisture_content": "Moisture content [%]",
        "cutting_direction": "Cutting direction",
        "rotational_speed": "Rotational speed [m/s]",
        "feed_speed": "Feed speed [m/s]",
        "feed_per_tooth": "Feed per tooth [mm]",
        "cutting_speed": "Cutting speed [m/s]",
        "cutting_width": "Cutting width [mm]",
        "cutting_depth": "Cutting depth [mm]",
        "cutting_angle": "Cutting angle [°]",
        "mean_chip_thickness": "Mean chip thickness [mm]",
        "mean_chip_length": "Mean chip length [mm]",
        "tool_id": "Tool ID",
        "tool_diameter": "Tool diameter [mm]",
        "tool_cutting_width": "Tool cutting width [mm]",
        "no_of_wings": "Number of wings",
        "total_no_of_wings": "Total number of wings",
        "cutting_material": "Cutting material",
        "body_material": "Body material",
        "rake_angle": "Rake angle [°]",
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
