# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_tool_add import Ui_ToolAdd

from helpers.helpers import get_permission_dialog
from settings import *
import ctypes
import os
import pandas as pd


class ToolAddWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ToolAdd()
        self.ui.setupUi(self)
        self.setup_user_interface()
        self.setup_type_validators()
        self.setup_callbacks()
        self.show()

    def setup_user_interface(self):
        self.setWindowIcon(QtGui.QIcon(os.path.join("ui", "icons", Strings.ICON)))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS_NEW}", None
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
        self.ui.shadow_frame.setGraphicsEffect(self.shadow)

    def setup_type_validators(self):
        self.only_int = QtGui.QIntValidator()
        self.only_float = QtGui.QDoubleValidator()
        self.ui.le_tool_diameter.setValidator(self.only_float)
        self.ui.le_bore_diameter.setValidator(self.only_float)
        self.ui.le_tool_cutting_width.setValidator(self.only_float)
        self.ui.le_no_of_wings.setValidator(self.only_int)
        self.ui.le_total_no_of_wings.setValidator(self.only_int)
        self.ui.le_n_max.setValidator(self.only_int)
        self.ui.le_n_opt.setValidator(self.only_int)
        self.ui.le_rake_angle.setValidator(self.only_float)
        self.ui.le_shear_angle.setValidator(self.only_float)

    def setup_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_2.clicked.connect(lambda: self.add_new_tool())

    def get_data(self):
        data = dict()
        for widget in self.ui.scrollAreaWidgetContents.children():
            if isinstance(widget, QLineEdit):
                key = widget.objectName()[
                    3:
                ] # e.g. "le_tool_diameter"[3:] -> "tool_diameter"
                value = widget.text()
                value = value.replace(",", ".")
                data[key] = value
        return data

    def tool_already_exists(self, tool_id):
        df = pd.read_csv(os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS), delimiter=DELIMITER)
        # 0 - not found
        # 1 - found
        result = len(df.loc[df["Identnummer"] == str(tool_id)].index)
        if result == 0:
            return False
        else:
            return True

    def add_new_tool(self):
        OK_CANCEL = 1
        OK = 1
        CANCEL = 2

        result = get_permission_dialog(
            "Sind Sie sicher, dass Sie ein neues Werkzeug zur bestehenden Datenbank hinzufügen möchten?",
            f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS_NEW}",
            OK_CANCEL,
        )

        if result == OK:
            data = self.get_data()
            file = open(os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS), "a")
            file_updates = open(os.path.join(Strings.DIRECTORY_DATABASE, LEITZ_TOOLS_UPDATES), "a")

            SEQUENCE = [
                "tool_id",
                "classification_number",
                "strategic_business_number",
                "tool_diameter",
                "tool_cutting_width",
                "bore_diameter",
                "no_of_wings",
                "total_no_of_wings",
                "cutting_material",
                "cutting_material_quality",
                "body_material",
                "n_max",
                "n_opt",
                "rake_angle",
                "shear_angle",
            ]

            for i, key in enumerate(SEQUENCE):
                if key == "tool_id":
                    if self.tool_already_exists(data[key]):
                        ctypes.windll.user32.MessageBoxW(
                            0,
                            "Das Werkzeug mit der angegebenen ID-Nummer befindet sich in der Datenbank.",
                            f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS_NEW}",
                            0 | 0x40,
                        )
                        return

                if i != len(SEQUENCE) - 1:
                    file.write(data[key] + ";")
                    file_updates.write(data[key] + ";")
                else:
                    file.write(data[key] + "\n")
                    file_updates.write(data[key] + "\n")

            ctypes.windll.user32.MessageBoxW(
                0,
                "Das Werkzeug wurde erfolgreich in die bestehende Datenbank aufgenommen.",
                f"{Strings.APP_NAME} | {Strings.DIALOG_TOOLS_NEW}",
                0 | 0x40,
            )
            file.close()
            file_updates.close()
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