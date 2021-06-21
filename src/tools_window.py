# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_tools import Ui_Tools

from settings import *
import os
import pandas as pd


class ToolsWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Tools()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_initial_view()
        self.setup_callbacks()
        self.oldPos = self.pos()

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.shadow_frame.setGraphicsEffect(self.shadow)

        self.show()

    def setup_ui(self):
        self.setWindowIcon(QtGui.QIcon("ui/icons/lighting.svg"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Power Analytics | Werkzeuge", None
            )
        )

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setup_headers()
        self.setup_rows()

    def setup_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.close())

    def get_full_name(self, column):
        translations = {
            "Identnummer": "Identnummer",
            "Klassifizierungsnummer": "Klassifizierungsnummer",
            "SGE": "Strategische Geschäftszahl",
            "D": "Werkzeugdurchmesser [mm]",
            "SB": "Schnittbreite [mm]",
            "BO": "Schaftdurchmesser [mm]",
            "Z": "Schneidenzahl",
            "ZGE": "Gesamtschneidenzahl",
            "QUALITAT": "Schneidenwerkstoff",
            "COD": "PCD Qualität",
            "TKQ": "Grundkörpermaterial",
            "NMAX": "Max. Drehzahl [U/min]",
            "NOPT": "Optimale Drehzahl [U/min]",
            "SW": "Spanwinkel γ [°]"
        }
        return translations[column]

    def setup_headers(self):
        df = pd.read_csv("database/{}".format(LEITZ_TOOLS), delimiter=";")
        headers = df.columns
        for header in headers:
            count = self.ui.tableWidget.columnCount()
            self.ui.tableWidget.setColumnCount(count + 1)
            self.ui.tableWidget.setHorizontalHeaderItem(count, QTableWidgetItem())
            self.ui.tableWidget.horizontalHeaderItem(count).setText(
                QtCore.QCoreApplication.translate(
                    "MainWindow", "{}".format(self.get_full_name(header)), None
                )
            )

    def setup_rows(self):
        df = pd.read_csv("database/{}".format(LEITZ_TOOLS), delimiter=";")
        for row in df.iloc():
            count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count + 1)
            self.ui.tableWidget.setVerticalHeaderItem(count, QTableWidgetItem())
            self.ui.tableWidget.verticalHeaderItem(count).setText(
                QtCore.QCoreApplication.translate(
                    "MainWindow", "{}".format(count + 1), None
                )
            )

            # Add values
            self.add_row(count, row)

    def add_row(self, row_number, row_values):
        for column, record in enumerate(row_values):
            self.ui.tableWidget.setItem(row_number, column, QTableWidgetItem())
            self.ui.tableWidget.item(row_number, column).setText(
                QtCore.QCoreApplication.translate(
                    "MainWindow", "{}".format(record), None
                )
            )

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
