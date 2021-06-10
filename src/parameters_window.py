# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_parameters import Ui_Parameters

from database.manage_tools import Tools
from helpers.calculate_parameters import (
    get_cutting_speed,
    get_feed_per_tooth,
    get_mean_chip_thickness,
    get_mean_chip_length,
)
from helpers.helpers import translate
from settings import *
import ctypes
import datetime
import json
import numpy as np
import os


class ParametersWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Parameters()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_initial_view()
        self.setup_type_validators()
        self.define_callbacks()
        self.set_last_used()
        self.oldPos = self.pos()

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.frame_shadow.setGraphicsEffect(self.shadow)

        self.show()

    def setup_ui(self):
        self.setWindowIcon(QtGui.QIcon("ui/icons/lighting.svg"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Power Analytics | Parameter", None
            )
        )

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def setup_type_validators(self):
        self.only_int = QtGui.QIntValidator()
        self.only_float = QtGui.QDoubleValidator()

        self.ui.le_moisture_content.setValidator(self.only_int)
        self.ui.le_rotational_speed.setValidator(self.only_float)
        self.ui.le_feed_speed.setValidator(self.only_float)
        self.ui.le_cutting_width.setValidator(self.only_float)
        self.ui.le_cutting_depth.setValidator(self.only_float)
        self.ui.le_cutting_angle.setValidator(self.only_float)

    def define_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_2.clicked.connect(lambda: self.clear_metadata())
        self.ui.pushButton_3.clicked.connect(lambda: self.accept())

    def set_last_used(self):
        try:
            with open("metadata.json") as json_file:
                metadata = json.load(json_file)
        except:
            metadata = None

        if metadata is not None:
            i = 0
            for widget in self.ui.scrollAreaWidgetContents.children():
                if isinstance(widget, QLineEdit):
                    key = widget.objectName().replace("le_", "")
                    if metadata[key] != "NaN":
                        widget.setText(metadata[key])
                    i += 1

    def clear_metadata(self):
        try:
            os.remove("metadata.json")
        except:
            pass

        for widget in self.ui.scrollAreaWidgetContents.children():
            if isinstance(widget, QLineEdit):
                widget.setText("")

    def get_remaining_parameters(self):
        # Set parameters that need to be calculated separately
        self.metadata["cutting_speed"] = get_cutting_speed(
            float(self.metadata["tool_diameter"]),
            float(self.metadata["rotational_speed"]),
        )

        self.metadata["feed_per_tooth"] = get_feed_per_tooth(
            float(self.metadata["feed_speed"]),
            float(self.metadata["rotational_speed"]),
            int(self.metadata["no_of_wings"]),
        )

        self.metadata["mean_chip_thickness"] = get_mean_chip_thickness(
            float(self.metadata["cutting_angle"]),
            float(self.metadata["tool_diameter"]),
            float(self.metadata["cutting_depth"]),
            float(self.metadata["feed_per_tooth"]),
        )

        self.metadata["mean_chip_length"] = get_mean_chip_length(
            float(self.metadata["tool_diameter"]), float(self.metadata["cutting_depth"])
        )

        # Change them to strings (needed to update labels with "setText()" function)
        self.metadata["cutting_speed"] = str(self.metadata["cutting_speed"])
        self.metadata["feed_per_tooth"] = str(self.metadata["feed_per_tooth"])
        self.metadata["mean_chip_thickness"] = str(self.metadata["mean_chip_thickness"])
        self.metadata["mean_chip_length"] = str(self.metadata["mean_chip_length"])

    def tool_exists(self):
        tool_id = self.ui.le_tool_id.text()
        d = np.loadtxt(
            f"database/{LEITZ_TOOLS}", delimiter=";", dtype=str, skiprows=1, usecols=0
        )
        if tool_id in d:
            return True
        else:
            return False

    # External CSV file containing tools' parameters
    def get_corresponding_parameters(self):
        if self.tool_exists():
            result = Tools(f"database/{LEITZ_TOOLS}", self.metadata["tool_id"]).export()
            return result
        else:
            ctypes.windll.user32.MessageBoxW(
                0,
                "Die angegebene Werkzeug-ID-Nummer existiert nicht - tragen Sie das Werkzeug in die Datenbank ein",
                "Power Analytics | Parameter",
                0 | 0x40,
            )
            return None

    def append_parameters_to_metadata(self, parameters):
        for key, value in parameters.items():
            if key == "tool_id":
                continue
            else:
                self.metadata[key] = value

    # This function also checks if there are any "," instead of "."
    # Upper case to avoid conflicts
    def accept(self):
        self.metadata = {
            "author": self.ui.le_author.text().upper() if self.ui.le_author.text() != "" else 'Nicht definiert',
            "date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
            "material": self.ui.le_material.text().upper(),
            "moisture_content": self.ui.le_moisture_content.text(),
            "cutting_direction": self.ui.le_cutting_direction.text().upper(),
            "rotational_speed": self.ui.le_rotational_speed.text().replace(",", "."),
            "feed_speed": self.ui.le_feed_speed.text().replace(",", "."),
            "cutting_width": self.ui.le_cutting_width.text().replace(",", "."),
            "cutting_depth": self.ui.le_cutting_depth.text().replace(",", "."),
            "cutting_angle": self.ui.le_cutting_angle.text().replace(",", "."),
            "tool_id": self.ui.le_tool_id.text(),
            "comments": self.ui.le_comments.text() if self.ui.le_comments.text() != "" else 'Keine Kommentare'
        }

        if self.metadata["cutting_direction"].lower() not in ["ggl", "gll"]:
            # To prompt the user to enter all parameters, follow these steps
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Es können nur zwei Schnittrichtungen gewählt werden: GGL oder GLL. Stattdessen wurde \"{self.metadata['cutting_direction']}\" eingegeben.",
                "Power Analytics | Parameter",
                0 | 0x40,
            )

            # Exit the function without further execution
            return

        for key, value in self.metadata.items():
            if value == "":
                # Change to 'NaN' if empty (compatible with Leitz's database)
                self.metadata[key] = "NaN"

                # To prompt the user to enter all parameters, follow these steps
                ctypes.windll.user32.MessageBoxW(
                    0,
                    "Es fehlen noch einige Werte - füllen Sie das Formular aus und versuchen Sie es erneut",
                    "Power Analytics | Parameter",
                    0 | 0x40,
                )

                # Exit the function without further execution
                return

        with open("metadata.json", "w") as outfile:
            if self.metadata["tool_id"] != "NaN":
                # Parameters from the file "tools.cs"
                ext_params = self.get_corresponding_parameters()

                if ext_params is not None:
                    self.append_parameters_to_metadata(ext_params)
                    self.get_remaining_parameters()
                    json.dump(self.metadata, outfile)
                    self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
