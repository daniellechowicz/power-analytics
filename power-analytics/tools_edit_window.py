# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_tools_edit import Ui_ToolsEdit
from tool_add_window import ToolAddWindow
from tools_window import ToolsWindow

from helpers.helpers import get_key
from database.database import Database
from settings import *
import ctypes
import os
import pandas as pd


class ToolsEditWindow(QMainWindow):

    CHOICES = {
        "Klassifizierungsnummer": "Klassifizierungsnummer",
        "SGE": "Strategische Geschäftszahl",
        "D": "Werkzeugdurchmesser",
        "SB": "Schneidenbreite",
        "BO": "Bohrungsdurchmesser",
        "Z": "Schneidenzahl",
        "ZGE": "Gesamtschneidenzahl",
        "QUALITAT": "Schneidenwerkstoff",
        "COD": "PCD Qualität",
        "TKQ": "Grundkörpermaterial",
        "NMAX": "Maximale Drehzahl",
        "NOPT": "Optimale Drehzahl",
        "SW": "Spanwinkel γ",
        "AW": "Achswinkel λ",
    }

    def __init__(self):
        # Open the database.
        self.db = Database(DB_NAME)

        QMainWindow.__init__(self)
        self.ui = Ui_ToolsEdit()
        self.ui.setupUi(self)
        self.set_types()
        self.setup_user_interface()
        self.update_type_validator()
        self.setup_callbacks()
        self.setup_combobox()
        self.show()

    def setup_user_interface(self):
        self.setWindowIcon(QtGui.QIcon(os.path.join("ui", "icons", Strings.ICON)))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS_EDIT}", None
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

    def setup_callbacks(self):
        self.ui.btn_search.clicked.connect(lambda: self.search_and_update_labels())
        self.ui.btn_add.clicked.connect(lambda: ToolAddWindow().show())
        self.ui.btn_show_all.clicked.connect(lambda: ToolsWindow().show())
        self.ui.btn_update.clicked.connect(lambda: self.update_file())
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.comboBox.currentIndexChanged.connect(
            lambda: self.update_type_validator()
        )

    def setup_combobox(self):
        for key, value in self.CHOICES.items():
            self.ui.comboBox.addItem(value)

    def update_type_validator(self):
        self.only_int = QtGui.QIntValidator()
        self.only_float = QtGui.QDoubleValidator()

        integers = ["Schneidenzahl", "Gesamtschneidenzahl"]
        floats = [
            "Werkzeugdurchmesser",
            "Schneidenbreite",
            "Bohrungsdurchmesser",
            "Maximale Drehzahl",
            "Optimale Drehzahl",
            "Spanwinkel γ",
            "Achswinkel λ",
        ]

        if self.ui.comboBox.currentText() in integers:
            self.ui.lineEdit_2.setValidator(self.only_int)
        elif self.ui.comboBox.currentText() in floats:
            self.ui.lineEdit_2.setValidator(self.only_float)
        else:
            self.ui.lineEdit_2.setValidator(None)

    def set_types(self):
        df = pd.read_csv(
            os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS),
            delimiter=DELIMITER,
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
        df["AW"] = pd.to_numeric(df["AW"], downcast="float")

        # Confirm the types.
        df.to_csv(os.path.join("database", LEITZ_TOOLS), sep=";", index=False)

    def get_data_to_update(self):
        choice_text = self.ui.comboBox.currentText()
        tool_id = self.ui.lineEdit.text()
        column_name = get_key(self.CHOICES, choice_text)
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
            os.path.join(Strings.DIRECTORY_DATABASE, file),
            delimiter=DELIMITER,
            keep_default_na=False,
        )

        if not self.tool_already_exists(tool_id):
            self.clean_labels()
            ctypes.windll.user32.MessageBoxW(
                0,
                "Das Werkzeug mit der angegebenen ID-Nummer ist nicht in der Datenbank.",
                f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS_NEW}",
                0 | 0x40,
            )
            return

        # There was a problem:
        # IndexError: index 0 is out of bounds for axis 0 with size 0
        # Sometimes I have strings (e.g. L 1234 WA), sometimes I have integers (e.g. 12345).
        # Therefore, simple try-except can be used.
        try:
            row = df.loc[df["Identnummer"] == str(tool_id)]
            if len(row) != 0:
                i = row.index[0]
        except:
            row = df.loc[df["Identnummer"] == int(tool_id)]
            if len(row) != 0:
                i = row.index[0]

        corresponding_params = {
            "tool_id": str(row["Identnummer"][i]),
            "classification_number": row["Klassifizierungsnummer"][i],
            "strategic_business_number": row["SGE"][i],
            "tool_diameter": row["D"][i],
            "cutting_width": row["SB"][i],
            "bore_diameter": row["BO"][i],
            "no_of_wings": row["Z"][i],
            "total_no_of_wings": row["ZGE"][i],
            "cutting_material": row["QUALITAT"][i],
            "cutting_material_quality": row["COD"][i],
            "body_material": row["TKQ"][i],
            "n_max": row["NMAX"][i],
            "n_opt": row["NOPT"][i],
            "rake_angle": row["SW"][i],
            "shear_angle": row["AW"][i],
        }
        self.update_labels(corresponding_params)

        return corresponding_params

    def track_changes(self, tool_id, column_name, value, new_line):
        """
        This function is responsible for keeping the track of all the changes
        performed (adding and/or deleting of the tools).
        """
        df = pd.read_csv(
            os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS_UPDATES),
            delimiter=DELIMITER,
            keep_default_na=False,
        )

        # There was a problem:
        # IndexError: index 0 is out of bounds for axis 0 with size 0
        # Sometimes I have strings (e.g. L 1234 WA), sometimes I have integers (e.g. 12345).
        # Therefore, simple try-except can be used.
        try:
            row = df.loc[df["Identnummer"] == str(tool_id)]
            if len(row) != 0:
                i = row.index[0]
        except:
            row = df.loc[df["Identnummer"] == int(tool_id)]
            if len(row) != 0:
                i = row.index[0]

        # If the ID of interest is present, then execute the following condition (i.e. edit the line corresponding to the tool).
        if len(row) != 0:
            i = row.index[0]
            df.at[i, column_name] = value
            df.to_csv(
                os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS_UPDATES),
                sep=DELIMITER,
                index=False,
            )
        # If there is no record for the ID of interest, then append it to the file.
        else:
            # Why am I doing it this way?
            # There was a particular problem: in "tools_updates.csv" file,
            # i.e. all the updates were saved multiple times. As it sounds like a good idea,
            # because one can introduced changes easily, it was causing problems when
            # the second file had to be replaced as it was copying all the lines instead of one.
            # Open the file and get all the lines.
            with open(
                os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS_UPDATES), "r"
            ) as f:
                lines = f.readlines()

            # Delete (or just skip) the line which starts with the same tool ID.
            with open(
                os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS_UPDATES), "w"
            ) as f:
                for line in lines:
                    if line.startswith(tool_id):
                        pass
                    else:
                        f.write(line)

            # Eventually, once the line was deleted, append a new line to the existing file.
            f = open(os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS_UPDATES), "a")
            f.write(new_line)
            f.close()

    def get_database_equivalent(self, key):
        """
        Since database's headers are in English, this function is needed
        to get headers that correspond with German equivalents.
        """
        headers = {
            "Klassifizierungsnummer": "classification_number",
            "SGE": "strategic_business_unit",
            "D": "tool_diameter",
            "SB": "tool_cutting_width",
            "BO": "bore_diameter",
            "Z": "no_of_wings",
            "ZGE": "total_no_of_wings",
            "QUALITAT": "cutting_material",
            "COD": "cutting_material_quality",
            "TKQ": "body_material",
            "NMAX": "n_max",
            "NOPT": "n_opt",
            "SW": "rake_angle",
            "AW": "shear_angle",
        }
        return headers[key]

    def edit_by_ID(self, tool_id, column_name, value, track_changes=False):
        # Since it contains "," by default (type validators are responsible for that).
        value = value.replace(",", ".")

        # Update "tools.csv" itself.
        df = pd.read_csv(
            os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS),
            delimiter=DELIMITER,
            keep_default_na=False,
        )

        # There was a problem:
        # IndexError: index 0 is out of bounds for axis 0 with size 0
        # Sometimes I have strings (e.g. L 1234 WA), sometimes I have integers (e.g. 12345).
        # Therefore, simple try-except can be used.
        try:
            row = df.loc[df["Identnummer"] == str(tool_id)]
            i = row.index[0]
        except:
            row = df.loc[df["Identnummer"] == int(tool_id)]
            i = row.index[0]

        df.at[i, column_name] = value
        df.to_csv(
            os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS),
            sep=DELIMITER,
            index=False,
        )

        # Whenever saved, it is necessary to change the default data types.
        self.set_types()

        if track_changes:
            row = df.loc[df["Identnummer"] == tool_id]
            row = row.to_csv(header=False, index=False, sep=DELIMITER).replace("\r", "")
            self.track_changes(tool_id, column_name, value, row)

        # When done, refresh the labels and update the database.
        self.search_and_update_labels()
        english_header = self.get_database_equivalent(column_name)
        self.db.modify_existing_record(tool_id, english_header, value)

    def search_and_update_labels(self):
        tool_id, _, _ = self.get_data_to_update()
        if tool_id is "":
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Es wurde keine Werkzeug-ID eingegeben.",
                f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS_EDIT}",
                0 | 0x40,
            )
        else:
            self.find_by_ID(LEITZ_TOOLS, tool_id)

    def clean_labels(self):
        """
        This function is responsible for cleaning the labels only.
        It does not affect neither the database nor CSV files.
        """
        for widget in self.ui.groupBox.children():
            if isinstance(widget, QLabel):
                if widget.objectName().startswith("l_"):
                    widget.setText("")

    def update_labels(self, params):
        """
        This function is responsible for updating the labels only.
        It does not affect neither the database nor CSV files.
        """
        for key, value in params.items():
            for widget in self.ui.groupBox.children():
                if isinstance(widget, QLabel):
                    if widget.objectName() == "l_" + key:
                        # Since number of wings and total number of wings need to be shown within one line,
                        # the following instruction is needed.
                        if widget.objectName() == "l_no_of_wings":
                            widget.setText(
                                str(value) + " | " + str(params["total_no_of_wings"])
                            )
                        else:
                            # For the rest of the labels, no complications.
                            if value == "":
                                widget.setText("Undefined")
                            else:
                                widget.setText(str(value))

    def update_file(self):
        """
        This function is responsible for updating the CSV file.
        It does affect the files (both "tools.csv" and "tools_updates.csv") permanently.
        """
        tool_id, column_name, value = self.get_data_to_update()
        try:
            self.edit_by_ID(tool_id, column_name, value, track_changes=True)
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Die Datei {LEITZ_TOOLS} wurde erfolgreich aktualisiert.",
                f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS_EDIT}",
                0 | 0x40,
            )
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Fehler beim Speichern aufgetreten ({e}).",
                f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS_EDIT}",
                0 | 0x40,
            )
        self.ui.lineEdit_2.clear()

    def get_updates(self, tool_id):
        """
        Whenever replacing the entire file, this function will compare both of them.
        In case of any differences found, it will return all the updates that need to be performed.
        """

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