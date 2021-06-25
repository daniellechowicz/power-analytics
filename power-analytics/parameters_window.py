# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui
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
        self.setup_user_interface()
        self.setup_type_validators()
        self.define_callbacks()
        self.set_last_used()

        # Enable drag functionality.
        self.oldPos = self.pos()
        self.show()

    def setup_user_interface(self):
        self.setWindowIcon(QtGui.QIcon("ui/icons/lighting.svg"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Power Analytics | Parameter", None
            )
        )

        # Remove title bar.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Drop shadow effect.
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.frame_shadow.setGraphicsEffect(self.shadow)

    def setup_type_validators(self):
        self.only_int = QtGui.QIntValidator()
        self.only_float = QtGui.QDoubleValidator()
        self.ui.le_moisture_content.setValidator(self.only_int)
        self.ui.le_rotational_speed.setValidator(self.only_float)
        self.ui.le_feed_speed.setValidator(self.only_float)
        self.ui.le_cutting_width.setValidator(self.only_float)
        self.ui.le_cutting_depth.setValidator(self.only_float)

    def define_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_2.clicked.connect(lambda: self.clear_metadata())
        self.ui.pushButton_3.clicked.connect(lambda: self.confirm())

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
                    # What is the idea behind the following lines?
                    # QML components (line edits) were called accordingly to the parameters' names
                    # they correspond to. For example, tool_id -> le_tool_id.
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

    def set_remaining_parameters(self):
        """
        Based on the parameters available (i.e. user-defined),
        the following helper functions will calculate cutting speed,
        feed per tooth, mean chip thickness and mean chip length, respectively.
        Then, these values will be appended to the existing metadata variable (dictionary).
        """

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
            float(self.metadata["shear_angle"]),
            float(self.metadata["tool_diameter"]),
            float(self.metadata["cutting_depth"]),
            float(self.metadata["feed_per_tooth"]),
        )
        self.metadata["mean_chip_length"] = get_mean_chip_length(
            float(self.metadata["tool_diameter"]), float(self.metadata["cutting_depth"])
        )

        # Change them to strings (needed to update labels with "setText()" function).
        self.metadata["cutting_speed"] = str(self.metadata["cutting_speed"])
        self.metadata["feed_per_tooth"] = str(self.metadata["feed_per_tooth"])
        self.metadata["mean_chip_thickness"] = str(self.metadata["mean_chip_thickness"])
        self.metadata["mean_chip_length"] = str(self.metadata["mean_chip_length"])

    def tool_exists(self):
        tool_id = self.ui.le_tool_id.text()
        available_records = np.loadtxt(
            os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS),
            delimiter=DELIMITER,
            dtype=str,
            skiprows=1,
            usecols=0,
        )
        if tool_id in available_records:
            return True
        else:
            return False

    def get_corresponding_parameters(self):
        if self.tool_exists():
            result = Tools(
                os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS),
                self.metadata["tool_id"],
            ).export()
            return result
        else:
            ctypes.windll.user32.MessageBoxW(
                0,
                "Die angegebene Werkzeug-ID-Nummer existiert nicht - tragen Sie das Werkzeug in die Datenbank ein.",
                f"{Strings.APP_NAME} | {Strings.DIALOG_PARAMETERS}",
                0 | 0x40,
            )
            return None

    def append_parameters_to_metadata(self, parameters):
        for key, value in parameters.items():
            if key == "tool_id":
                continue
            else:
                self.metadata[key] = value

    def set_entered_parameters(self):
        self.author = self.ui.le_author.text().upper()
        self.date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        self.material = self.ui.le_material.text().upper()
        self.moisture_content = self.ui.le_moisture_content.text().replace(",", ".")
        self.cutting_direction = (
            self.ui.le_cutting_direction.text().upper().replace(",", ".")
        )
        self.rotational_speed = self.ui.le_rotational_speed.text().replace(",", ".")
        self.feed_speed = self.ui.le_feed_speed.text().replace(",", ".")
        self.cutting_width = self.ui.le_cutting_width.text().replace(",", ".")
        self.cutting_depth = self.ui.le_cutting_depth.text().replace(",", ".")
        self.tool_id = self.ui.le_tool_id.text()
        self.comments = self.ui.le_comments.text()

        if self.moisture_content == "":
            self.moisture_content = "0"

        if self.author == "":
            self.author = "Nicht definiert"

        if self.comments == "":
            self.comments = "Keine Kommentare"

        self.metadata = {
            "author": self.author,
            "date": self.date,
            "material": self.material,
            "moisture_content": self.moisture_content,
            "cutting_direction": self.cutting_direction,
            "rotational_speed": self.rotational_speed,
            "feed_speed": self.feed_speed,
            "cutting_width": self.cutting_width,
            "cutting_depth": self.cutting_depth,
            "tool_id": self.tool_id,
            "comments": self.comments,
        }

    def parameters_are_valid(self):
        # Checking validity of cutting direction.
        if self.metadata["cutting_direction"].lower() not in ["ggl", "gll"]:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Es können nur zwei Schnittrichtungen gewählt werden: GGL oder GLL. Stattdessen wurde \"{self.metadata['cutting_direction']}\" eingegeben.",
                f"{Strings.APP_NAME} | {Strings.DIALOG_PARAMETERS}",
                0 | 0x40,
            )
            return False

        # Checking if fields are not empty.
        for key, value in self.metadata.items():
            if value == "":
                # Change to 'NaN' if empty (compatible with Leitz's database).
                self.metadata[key] = "NaN"
                ctypes.windll.user32.MessageBoxW(
                    0,
                    "Es fehlen noch einige Werte - füllen Sie das Formular aus und versuchen Sie es erneut.",
                    f"{Strings.APP_NAME} | {Strings.DIALOG_PARAMETERS}",
                    0 | 0x40,
                )
                return False
        
        return True

    def confirm(self):
        """
        This function also checks if there are any "," instead of ".".
        Upper case to avoid conflicts for:
        - author field,
        - material field.
        """

        # First, set the parameters that were entered into class' line edits.
        self.set_entered_parameters()

        if self.parameters_are_valid():
            with open("metadata.json", "w") as outfile:
                if self.metadata["tool_id"] != "NaN":
                    # Parameters from the file "tools.csv".
                    ext_params = self.get_corresponding_parameters()
                    if ext_params is not None:
                        self.append_parameters_to_metadata(ext_params)
                        self.set_remaining_parameters()
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
