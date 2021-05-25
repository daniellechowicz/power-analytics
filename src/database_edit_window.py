# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_database_edit import Ui_DatabaseEdit

from helpers.helpers import convert_type
from parameters_window import ParametersWindow
from settings import *
import ctypes
import os
import sqlite3


class DatabaseEditWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_DatabaseEdit()
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
        self.ui.shadow_frame.setGraphicsEffect(self.shadow)

        # Drag functionality enabled
        self.oldPos = self.pos()
        self.show()

    def setup_ui(self):
        self.setWindowIcon(QtGui.QIcon("ui/icons/lighting.svg"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Power Analytics | Datenbank bearbeiten", None
            )
        )

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def setup_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_2.clicked.connect(lambda: self.delete())
        self.ui.pushButton_3.clicked.connect(lambda: self.edit())

    def setup_combobox(self):
        self.choices = {
            "Autor": "author",
            "Werkstoff": "material",
            "Feuchtigkeit": "moisture_content",
            "Schnittrichtung": "cutting_direction",
            "Drehzahl": "rotational_speed",
            "Schneidenzahl": "feed_speed",
            "Schnittbreite": "cutting_width",
            "Schnitttiefe": "cutting_depth",
            "Schnittwinkel": "cutting_angle",
            "ID-Nummer": "tool_id",
            "Kommentare": "comments",
        }

        for key, value in self.choices.items():
            self.ui.comboBox.addItem(key)

    def delete(self):
        try:
            # Take the ID fom the line edit
            measurement_id = int(self.ui.lineEdit.text())
        except:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Geben Sie die ID-Nummer der Messung ein, bevor Sie die Daten in der Datenbank bearbeiten",
                "Power Analytics | Datenbank bearbeiten",
                0,
            )
            return

        if measurement_id:
            # Connect to the database
            connection = sqlite3.connect(f"database/{DB_NAME}.db")

            # Execute the queries (both for stats and metadata -
            # it needs to be done this way due to foreign key presence)
            delete_query_stats = (
                f"DELETE FROM stats WHERE measurement_id={measurement_id};"
            )
            delete_query_metadata = (
                f"DELETE FROM metadata WHERE measurement_id={measurement_id};"
            )
            connection.execute(delete_query_stats)
            connection.commit()
            connection.execute(delete_query_metadata)
            connection.commit()
            connection.close()
            self.close()

    def edit(self):
        key = self.ui.comboBox.currentText()
        column = self.choices[key]

        # Measurement ID line edit
        try:
            # Take the ID fom the line edit
            measurement_id = int(self.ui.lineEdit.text())
        except:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Geben Sie die ID-Nummer der Messung ein, bevor Sie die Daten in der Datenbank bearbeiten",
                "Power Analytics | Datenbank bearbeiten",
                0,
            )
            return

        # New value line edit
        try:
            new_value = self.ui.lineEdit_2.text()
        except:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Geben Sie den neuen Wert für den gewählten Parameter ein, bevor Sie die Auswahl bestätigen",
                "Power Analytics | Datenbank bearbeiten",
                0,
            )
            return

        # Remember to check if the functionality with database tools works
        if measurement_id and new_value:
            # Connect to the database
            connection = sqlite3.connect(f"database/{DB_NAME}.db")

            # Just in case, check variable's type and change it if needed
            new_value = convert_type(column, new_value)

            # Execute the queries (both for stats and metadata -
            # it needs to be done this way due to foreign key presence)
            edit_query = f"""
            UPDATE metadata
            SET {column}={new_value}
            WHERE measurement_id={measurement_id};
            """
            connection.execute(edit_query)
            connection.commit()
            connection.close()
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
