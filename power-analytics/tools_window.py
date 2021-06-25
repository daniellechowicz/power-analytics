# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_tools import Ui_Tools

from settings import *
import os
import pandas as pd


class ToolsWindow(QMainWindow):

    FULL_NAMES = {
        "Identnummer": "Identnummer",
        "Klassifizierungsnummer": "Klassifizierungsnummer",
        "SGE": "Strategische Geschäftszahl",
        "D": "Werkzeugdurchmesser [mm]",
        "SB": "Schneidenbreite [mm]",
        "BO": "Bohrungsdurchmesser [mm]",
        "Z": "Schneidenzahl",
        "ZGE": "Gesamtschneidenzahl",
        "QUALITAT": "Schneidenwerkstoff",
        "COD": "PCD Qualität",
        "TKQ": "Grundkörpermaterial",
        "NMAX": "Max. Drehzahl [U/min]",
        "NOPT": "Optimale Drehzahl [U/min]",
        "SW": "Spanwinkel γ [°]",
        "AW": "Achswinkel λ [°]",
    }

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Tools()
        self.ui.setupUi(self)
        self.setup_user_interface()
        self.setup_callbacks()

        # Drag functionality enabled.
        self.oldPos = self.pos()
        self.show()

    def setup_user_interface(self):
        self.setWindowIcon(QtGui.QIcon(f"ui/icons/{Strings.ICON}"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS}", None
            )
        )

        # Remove title bar.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setup_headers()
        self.setup_rows()

        # Drop shadow effect.
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 60))
        self.ui.shadow_frame.setGraphicsEffect(self.shadow)

    def setup_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.close())

    def setup_headers(self):
        df = pd.read_csv(
            os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS), delimiter=DELIMITER
        )
        headers = df.columns
        for header in headers:
            count = self.ui.tableWidget.columnCount()
            header = self.FULL_NAMES[header]
            self.ui.tableWidget.setColumnCount(count + 1)
            self.ui.tableWidget.setHorizontalHeaderItem(count, QTableWidgetItem())
            self.ui.tableWidget.horizontalHeaderItem(count).setText(
                QtCore.QCoreApplication.translate(
                    "MainWindow", "{}".format(header), None
                )
            )

    def setup_rows(self):
        df = pd.read_csv(
            os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS), delimiter=DELIMITER
        )
        for row in df.iloc():
            count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count + 1)
            self.ui.tableWidget.setVerticalHeaderItem(count, QTableWidgetItem())
            self.ui.tableWidget.verticalHeaderItem(count).setText(
                QtCore.QCoreApplication.translate(
                    "MainWindow", "{}".format(count + 1), None
                )
            )
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
