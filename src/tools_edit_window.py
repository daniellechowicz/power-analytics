# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from src.ui.ui_tools_edit import Ui_ToolsEdit
from src.tool_add_window import ToolAddWindow

from src.settings import *
import ctypes
import numpy as np
import os
import pandas as pd


class ToolsEditWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ToolsEdit()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_initial_view()
        self.setup_callbacks()
        self.setup_combobox()

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.frame_shadow.setGraphicsEffect(self.shadow)

        self.show()

    def setup_ui(self):
        self.setWindowIcon(QtGui.QIcon("pkgs/src/ui/icons/lighting.svg"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Power Analytics | Werkzeugparameter bearbeiten", None
            )
        )

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def setup_callbacks(self):
        self.ui.btn_search.clicked.connect(lambda: self.search_and_update_labels())
        self.ui.btn_add.clicked.connect(lambda: ToolAddWindow().show())
        self.ui.btn_update.clicked.connect(lambda: self.update_file())
        self.ui.btn_close.clicked.connect(lambda: self.close())

    def setup_combobox(self):
        self.choices = {
            "Indentnummer": "ID-Nummer",
            "Klassifizierungsnummer": "Klassifizierungsnummer",
            "SGE": "SGE",
            "D": "Werkzeugdurchmesser",
            "SB": "Schnittbreite",
            "BO": "Wellendurchmesser",
            "Z": "Schneidenzahl",
            "QUALITAT": "Schneidenwerkstoff",
            "COD": "PCD Qualität",
            "TKQ": "Grundkörpermaterial",
            "NMAX": "Maximale Drehzahl",
            "NOPT": "Optimale Drehzahl",
            "SW": "Spanwinkel",
        }
        for key, value in self.choices.items():
            self.ui.comboBox.addItem(value)

    def get_data_to_update(self):
        def get_key(d, val):
            for key, value in d.items():
                if val == value:
                    return key
            return None

        choice_text = self.ui.comboBox.currentText()
        tool_id = self.ui.lineEdit.text()
        column_name = get_key(self.choices, choice_text)
        value = self.ui.lineEdit_2.text()

        return tool_id, column_name, value

    def find_by_ID(self, file, tool_id):
        df = pd.read_csv(
            os.path.join("pkgs/src/database", file),
            delimiter=";",
            keep_default_na=False,
        )
        row = df.loc[df["Identnummer"] == tool_id]
        i = row.index[0]
        corresponding_params = {
            "tool_id": row["Identnummer"][i],
            "classification_number": row["Klassifizierungsnummer"][i],
            "strategic_business_number": row["SGE"][i],
            "tool_diameter": row["D"][i],
            "cutting_width": row["SB"][i],
            "bore_diameter": row["BO"][i],
            "no_of_wings": row["Z"][i],
            "cutting_material": row["QUALITAT"][i],
            "cutting_material_quality": row["COD"][i],
            "body_material": row["TKQ"][i],
            "n_max": row["NMAX"][i],
            "n_opt": row["NOPT"][i],
            "rake_angle": row["SW"][i],
        }
        self.update_labels(corresponding_params)
        return corresponding_params

    # line - this is a row from "tools.csv"
    def track_changes(self, tool_id, column_name, value, line):
        # Update "tools_updates.csv" now (to keep track of changes done over time)
        df = pd.read_csv(
            os.path.join("pkgs/src/database", LEITZ_TOOLS_UPDATES),
            delimiter=";",
            keep_default_na=False,
        )
        row = df.loc[df["Identnummer"] == tool_id]
        # If there is the record for the ID of interest, then execute the following
        if len(row) != 0:
            i = row.index[0]
            df.at[i, column_name] = value
            df.to_csv(
                os.path.join("pkgs/src/database", LEITZ_TOOLS_UPDATES),
                sep=";",
                index=False,
            )
        # If there is no record for the ID of interest, then append it to the file
        else:
            f = open(os.path.join("pkgs/src/database", LEITZ_TOOLS_UPDATES), "a")
            f.write(line)
            f.close()

    def edit_by_ID(self, tool_id, column_name, value, track_changes=False):
        # Update "tools.csv" itself
        df = pd.read_csv(
            os.path.join("pkgs/src/database", LEITZ_TOOLS),
            delimiter=";",
            keep_default_na=False,
        )
        row = df.loc[df["Identnummer"] == tool_id]
        i = row.index[0]
        df.at[i, column_name] = value
        df.to_csv(os.path.join("pkgs/src/database", LEITZ_TOOLS), sep=";", index=False)

        if track_changes:
            # Update a row (but for these lines, no new value would have been added)
            row = df.loc[df["Identnummer"] == tool_id]

            # Preprocess the line
            row = row.to_csv(header=False, index=False, sep=";").replace("\r", "")
            self.track_changes(tool_id, column_name, value, row)

        # When done, refresh the labels
        self.search_and_update_labels()

    def search_and_update_labels(self):
        tool_id, _, _ = self.get_data_to_update()
        if tool_id is "":
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Es wurde keine Werkzeug-ID eingegeben",
                "Power Analytics | Werkzeugparameter bearbeiten",
                0,
            )
        else:
            self.find_by_ID(LEITZ_TOOLS, tool_id)

    def update_labels(self, params):
        for key, value in params.items():
            # QGroupBox -> QLabel
            # "groupBox" is the one I have to use
            for widget in self.ui.groupBox.children():
                if isinstance(widget, QLabel):
                    if widget.objectName() == "l_" + key:
                        if value == "":
                            widget.setText("Undefined")
                        else:
                            widget.setText(str(value))

    def update_file(self):
        tool_id, column_name, value = self.get_data_to_update()
        try:
            self.edit_by_ID(tool_id, column_name, value, track_changes=True)
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Die Datei {LEITZ_TOOLS} wurde erfolgreich aktualisiert",
                "Power Analytics | Werkzeugparameter bearbeiten",
                0,
            )
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Fehler beim Speichern aufgetreten ({e})",
                "Power Analytics | Werkzeugparameter bearbeiten",
                0,
            )

    def get_updates(self, tool_id):
        # r1 - from file exported from the database
        # r2 - from file containing all the updates done
        r1 = self.find_by_ID(LEITZ_TOOLS, tool_id)
        try:
            r2 = self.find_by_ID(LEITZ_TOOLS_UPDATES, tool_id)
        except:
            r2 = None

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
