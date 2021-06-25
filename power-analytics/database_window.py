# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_database import Ui_Database

from database.read import Read
from database_edit_window import DatabaseEditWindow
from helpers.helpers import get_full_name
from settings import *
import ctypes
import os
import pandas as pd
import sqlite3


class DatabaseWindow(QMainWindow):
    def __init__(self, db_name, show=True):
        self.db_name = db_name

        QMainWindow.__init__(self)
        self.ui = Ui_Database()
        self.ui.setupUi(self)
        self.setup_user_interface()
        self.define_callbacks()

        # Drag functionality enabled.
        self.oldPos = self.pos()

        if show != False:
            self.show()

    def setup_user_interface(self):
        self.setWindowIcon(QtGui.QIcon(f"ui/icons/{Strings.ICON}"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", f"{Strings.APP_NAME} | {Strings.DIALOG_DATABASE}", None
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

    def define_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_2.clicked.connect(lambda: self.export_as_CSV())
        self.ui.pushButton_3.clicked.connect(lambda: DatabaseEditWindow().show())
        self.ui.tableWidget.itemSelectionChanged.connect(
            lambda: self.open_chosen_report()
        )

    def setup_headers(self):
        # Get headers from the database "metadata".
        connection = sqlite3.connect(
            os.path.join(Strings.DIRECTORY_DATABASE, self.db_name + ".db")
        )
        cursor = connection.execute("SELECT * FROM metadata")
        headers_1 = [description[0] for description in cursor.description]

        # Get headers from the database "stats".
        cursor = connection.execute("SELECT * FROM stats")
        headers_2 = [
            description[0]
            for description in cursor.description
            if description[0] not in headers_1
        ]

        # Merge two vectors.
        self.headers = headers_1 + headers_2

        for header in self.headers:
            count = self.ui.tableWidget.columnCount()
            header = get_full_name(header)
            self.ui.tableWidget.setColumnCount(count + 1)
            self.ui.tableWidget.setHorizontalHeaderItem(count, QTableWidgetItem())
            self.ui.tableWidget.horizontalHeaderItem(count).setText(
                QtCore.QCoreApplication.translate(
                    "MainWindow", "{}".format(header), None
                )
            )

        connection.close()

    def setup_rows(self):
        read = Read(os.path.join(Strings.DIRECTORY_DATABASE, self.db_name))
        rows = read.fetch_joint(self.headers)
        for row in rows:
            count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.setRowCount(count + 1)
            self.ui.tableWidget.setVerticalHeaderItem(count, QTableWidgetItem())
            self.ui.tableWidget.verticalHeaderItem(count).setText(
                QtCore.QCoreApplication.translate(
                    "MainWindow", "{}".format(row[0]), None
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

    def get_directory(self):
        folder_path = str(
            QtWidgets.QFileDialog.getExistingDirectory(
                self, f"{Strings.APP_NAME} | Ordner auswählen"
            )
        )
        return folder_path

    def export_as_CSV(self):
        folder_path = self.get_directory()
        path = os.path.join(folder_path, DB_CSV_NAME)

        # Otherwise, a possibility of ambigous column names (two tables).
        headers = [
            header.replace("measurement_id", "metadata.measurement_id")
            for header in self.headers
        ]
        query = """
        SELECT {} 
        FROM metadata 
        INNER JOIN stats ON metadata.measurement_id=stats.measurement_id
        """.format(
            ",".join(headers)
        )

        # Connect to the database and close it immediately to avoid errors.
        connection = sqlite3.connect(
            os.path.join(Strings.DIRECTORY_DATABASE, self.db_name + ".db")
        )
        db_df = pd.read_sql_query(query, connection)
        connection.close()

        if path != DB_CSV_NAME:
            db_df.to_csv(path, index=False)
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Die Datenbank wurde erfolgreich exportiert.",
                f"{Strings.APP_NAME} | {Strings.DIALOG_DATABASE}",
                0 | 0x40,
            )

    def open_chosen_report(self):
        items = self.ui.tableWidget.selectedItems()
        measurement_id = int(items[0].text())
        db_read = Read(os.path.join(Strings.DIRECTORY_DATABASE, self.db_name))
        report_name = db_read.get_report_name(measurement_id)
        os.startfile(
            os.path.join(
                Strings.DIRECTORY_REPORT_MAIN,
                Strings.DIRECTORY_REPORT_PDFS,
                report_name,
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
