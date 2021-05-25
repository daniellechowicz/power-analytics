# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_tool_add import Ui_ToolAdd

from settings import *
import ctypes
import os


class ToolAddWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ToolAdd()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_initial_view()
        self.setup_type_validators()
        self.setup_callbacks()

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
                "MainWindow", "Power Analytics | Neues Werkzeug", None
            )
        )

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

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

    def setup_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_2.clicked.connect(lambda: self.save())

    def get_permission_dialog(self, text, title, utype):
        user32 = ctypes.WinDLL("user32", use_last_error=True)
        msg_box = user32.MessageBoxW
        result = msg_box(None, text, title, utype)
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return result

    def get_data(self):
        # Append given parameters to this variable
        data = dict()

        # QWidget -> QLineEdit
        # "scrollAreaWidgetContents" is the one I have to use
        for widget in self.ui.scrollAreaWidgetContents.children():
            if isinstance(widget, QLineEdit):
                key = widget.objectName()[
                    3:
                ]  # e.g. "le_tool_diameter"[3:] -> "tool_diameter"
                value = widget.text()
                data[key] = value
        ctypes.windll.user32.MessageBoxW(
            0,
            "Das Werkzeug wurde erfolgreich in die bestehende Datenbank aufgenommen",
            "Power Analytics | Neues Werkzeug",
            0,
        )

        return data

    def save(self):
        OK_CANCEL = 1
        OK = 1
        CANCEL = 2

        result = self.get_permission_dialog(
            "Sind Sie sicher, dass Sie ein neues Werkzeug zur bestehenden Datenbank hinzufügen möchten?",
            "Power Analytics | Neues Werkzeug",
            OK_CANCEL,
        )

        if result == OK:
            data = self.get_data()
            file = open(os.path.join("database", LEITZ_TOOLS), "a")
            file_updates = open(os.path.join("database", LEITZ_TOOLS_UPDATES), "a")

            seq = [
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
            ]

            for i, key in enumerate(seq):
                if i != len(seq) - 1:
                    file.write(data[key] + ";")
                    file_updates.write(data[key] + ";")
                else:
                    file.write(data[key] + "\n")
                    file_updates.write(data[key] + "\n")

            file.close()
            file_updates.close()

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
