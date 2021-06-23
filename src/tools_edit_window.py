# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_tools_edit import Ui_ToolsEdit
from tool_add_window import ToolAddWindow
from tools_window import ToolsWindow

from database.database import Database
from settings import *
import ctypes
import numpy as np
import os
import pandas as pd


class ToolsEditWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ToolsEdit()
        self.ui.setupUi(self)
        self.change_default_data_types()
        self.setup_ui()
        self.setup_initial_view()
        self.update_type_validator()
        self.setup_callbacks()
        self.setup_combobox()

        # Open the database
        self.db = Database(DB_NAME)

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
        self.ui.btn_show_all.clicked.connect(lambda: ToolsWindow().show())
        self.ui.btn_update.clicked.connect(lambda: self.update_file())
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.update_type_validator())
    
    def setup_combobox(self):
        self.choices = {
            "Klassifizierungsnummer": "Klassifizierungsnummer",
            "SGE": "Strategische Geschäftszahl",
            "D": "Werkzeugdurchmesser",
            "SB": "Schneidenbreite",
            "BO": "Bohrungsdurchmesser",
            "Z": "Schneidenzahl",
            "QUALITAT": "Schneidenwerkstoff",
            "COD": "PCD Qualität",
            "TKQ": "Grundkörpermaterial",
            "NMAX": "Maximale Drehzahl",
            "NOPT": "Optimale Drehzahl",
            "SW": "Spanwinkel γ",
        }
        for key, value in self.choices.items():
            self.ui.comboBox.addItem(value)

    def update_type_validator(self):
        self.only_int = QtGui.QIntValidator()
        self.only_float = QtGui.QDoubleValidator()

        integers = [
            'Schneidenzahl'
        ]
        floats = [
            'Werkzeugdurchmesser',
            'Schneidenbreite',
            'Bohrungsdurchmesser',
            'Maximale Drehzahl',
            'Optimale Drehzahl',
            'Spanwinkel γ'
        ]
        
        if self.ui.comboBox.currentText() in integers:
            self.ui.lineEdit_2.setValidator(self.only_int)
        elif self.ui.comboBox.currentText() in floats:
            self.ui.lineEdit_2.setValidator(self.only_float)
        else:
            self.ui.lineEdit_2.setValidator(None)

    def change_default_data_types(self):
        df = pd.read_csv(
            os.path.join("database", LEITZ_TOOLS),
            delimiter=";",
            keep_default_na=False,
        )
        df["Identnummer"] = df["Identnummer"].astype(str)
        df["Klassifizierungsnummer"] = df["Klassifizierungsnummer"].astype(str)
        df["SGE"] = df["SGE"].astype(str)        
        df["QUALITAT"] = df["QUALITAT"].astype(str)        
        df["COD"] = df["COD"].astype(str)        
        df["TKQ"] = df["TKQ"].astype(str)        
        df["Z"] = pd.to_numeric(df["Z"], downcast="integer")
        df["ZGE"] = pd.to_numeric(df["ZGE"], downcast="integer")
        df["D"] = pd.to_numeric(df["D"], downcast="float")
        df["SB"] = pd.to_numeric(df["SB"], downcast="float")
        df["BO"] = pd.to_numeric(df["BO"], downcast="float")
        df["NMAX"] = pd.to_numeric(df["NMAX"], downcast="float")
        df["NOPT"] = pd.to_numeric(df["NOPT"], downcast="float")
        df["SW"] = pd.to_numeric(df["SW"], downcast="float")
        df.to_csv(os.path.join("database", LEITZ_TOOLS), sep=";", index=False)

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

    def tool_already_exists(self, tool_id):
        df = pd.read_csv(os.path.join("database", LEITZ_TOOLS), delimiter=";")
        # 0 - not found
        # 1 - found
        result = len(df.loc[df["Identnummer"] == str(tool_id)].index)
        if result == 0:
            return False
        else:
            return True

    def find_by_ID(self, file, tool_id):
        df = pd.read_csv(
            os.path.join("database", file),
            delimiter=";",
            keep_default_na=False,
        )

        if not self.tool_already_exists(tool_id):
            self.clean_labels()
            ctypes.windll.user32.MessageBoxW(
                0,
                "Das Werkzeug mit der angegebenen ID-Nummer ist nicht in der Datenbank",
                "Power Analytics | Neues Werkzeug",
                0 | 0x40,
            )
            return

        # There was a problem:
        # IndexError: index 0 is out of bounds for axis 0 with size 0
        # Sometimes I have strings (e.g. L 1234 WA), sometimes I have integers (e.g. 12345)...
        # Therefore, simple try-except can be used.
        try:
            row = df.loc[df["Identnummer"] == str(tool_id)]
            i = row.index[0]
        except:
            row = df.loc[df["Identnummer"] == int(tool_id)]
            i = row.index[0]

        corresponding_params = {
            "tool_id": str(row["Identnummer"][i]),
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
    def track_changes(self, tool_id, column_name, value, new_line):
        # Update "tools_updates.csv" now (to keep track of changes done over time)
        df = pd.read_csv(
            os.path.join("database", LEITZ_TOOLS_UPDATES),
            delimiter=";",
            keep_default_na=False,
        )
        # There was a problem:
        # IndexError: index 0 is out of bounds for axis 0 with size 0
        # Sometimes I have strings (e.g. L 1234 WA), sometimes I have integers (e.g. 12345)...
        # Therefore, simple try-except can be used.
        try:
            row = df.loc[df["Identnummer"] == str(tool_id)]
            if len(row) != 0:
                i = row.index[0]
        except:
            row = df.loc[df["Identnummer"] == int(tool_id)]
            if len(row) != 0:
                i = row.index[0]

        # If there is the record for the ID of interest, then execute the following
        if len(row) != 0:
            i = row.index[0]
            df.at[i, column_name] = value
            df.to_csv(
                os.path.join("database", LEITZ_TOOLS_UPDATES),
                sep=";",
                index=False,
            )
        # If there is no record for the ID of interest, then append it to the file
        else:
            # Why am I doing it this way?
            # There was a particular problem: in "tools_updates.csv" file,
            # all the updates were saved multiple times. As it sounds like a good idea,
            # because one can introduced changes easily, it was causing problems when
            # the second file had to be replaced as it was copying all the lines instead of one.
            # Open the file and get all the lines.
            with open(os.path.join("database", LEITZ_TOOLS_UPDATES), "r") as f:
                lines = f.readlines()

            # Delete (or just skip) the line which starts with the same tool ID.
            with open(os.path.join("database", LEITZ_TOOLS_UPDATES), "w") as f:
                for line in lines:
                    if line.startswith(tool_id):
                        pass
                    else:
                        f.write(line)

            # Eventually, once the line was deleted, append a new line to the existing file.
            f = open(os.path.join("database", LEITZ_TOOLS_UPDATES), "a")
            f.write(new_line)
            f.close()

    def get_database_equivalent(self, key):
        headers = {
            "Klassifizierungsnummer": "classification_number",
            "SGE": "strategic_business_unit",
            "D": "tool_diameter",
            "SB": "tool_cutting_width",
            "BO": "bore_diameter",
            "Z": "no_of_wings",
            "QUALITAT": "cutting_material",
            "COD": "cutting_material_quality",
            "TKQ": "body_material",
            "NMAX": "n_max",
            "NOPT": "n_opt",
            "SW": "rake_angle",
        }
        return headers[key]

    def edit_by_ID(self, tool_id, column_name, value, track_changes=False):
        # Since it contains "," by default (type validators are responsible for that).
        value = value.replace(",", ".")

        # Update "tools.csv" itself
        df = pd.read_csv(
            os.path.join("database", LEITZ_TOOLS),
            delimiter=";",
            keep_default_na=False,
        )
        # There was a problem:
        # IndexError: index 0 is out of bounds for axis 0 with size 0
        # Sometimes I have strings (e.g. L 1234 WA), sometimes I have integers (e.g. 12345)...
        # Therefore, simple try-except can be used.
        try:
            row = df.loc[df["Identnummer"] == str(tool_id)]
            i = row.index[0]
        except:
            row = df.loc[df["Identnummer"] == int(tool_id)]
            i = row.index[0]

        df.at[i, column_name] = value
        df.to_csv(os.path.join("database", LEITZ_TOOLS), sep=";", index=False)
        
        # Whenever saved, it is necessary to change the default data types.
        self.change_default_data_types()

        if track_changes:
            # Update a row (but for these lines, no new value would have been added)
            row = df.loc[df["Identnummer"] == tool_id]

            # Preprocess the line
            row = row.to_csv(header=False, index=False, sep=";").replace("\r", "")
            self.track_changes(tool_id, column_name, value, row)

        # When done, refresh the labels and update the database
        self.search_and_update_labels()
        column = self.get_database_equivalent(column_name)
        self.db.modify_existing_record(tool_id, column, value)

    def search_and_update_labels(self):
        tool_id, _, _ = self.get_data_to_update()
        if tool_id is "":
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Es wurde keine Werkzeug-ID eingegeben",
                "Power Analytics | Werkzeugparameter bearbeiten",
                0 | 0x40,
            )
        else:
            self.find_by_ID(LEITZ_TOOLS, tool_id)

    def clean_labels(self):
        for widget in self.ui.groupBox.children():
            if isinstance(widget, QLabel):
                if widget.objectName().startswith("l_"):
                    widget.setText("")

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
                0 | 0x40,
            )
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Fehler beim Speichern aufgetreten ({e})",
                "Power Analytics | Werkzeugparameter bearbeiten",
                0 | 0x40,
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
