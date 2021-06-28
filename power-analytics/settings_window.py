# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_settings import Ui_Settings

from helpers.helpers import edit_settings, get_permission_dialog
from settings import *
import ctypes
import json
import os


class SettingsWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setup_user_interface()
        self.setup_type_validators()
        self.setup_callbacks()
        self.set_from_json()
        self.show()

    def setup_user_interface(self):
        self.setWindowIcon(QtGui.QIcon(os.path.join("ui", "icons", Strings.ICON)))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", f"{Strings.APP_NAME} | {Strings.DIALOG_SETTINGS}", None
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
        self.ui.le_sampling_rate.setValidator(self.only_int)
        self.ui.le_resample_factor.setValidator(self.only_int)
        self.ui.le_window_size.setValidator(self.only_int)
        self.ui.le_idle_0.setValidator(self.only_int)
        self.ui.le_idle_1.setValidator(self.only_int)
        self.ui.le_cutting_0.setValidator(self.only_int)
        self.ui.le_cutting_1.setValidator(self.only_int)

    def setup_callbacks(self):
        self.ui.btnClose.clicked.connect(lambda: self.close())
        self.ui.btnAccept.clicked.connect(lambda: self.change_settings())

    def set_from_json(self):
        with open("settings.json") as json_file:
            settings = json.load(json_file)

        self.corresponding_keys = {
            "Channel name": "channel_name",
            "Sampling rate [Hz]": "sampling_rate",
            "Resampling factor": "resample_factor",
            "Window size": "window_size",
            "Start of idling [S]": "idle_0",
            "End of idling [S]": "idle_1",
            "Start of cutting [S]": "cutting_0",
            "End of cutting [S]": "cutting_1",
            "Tools CSV filename": "leitz_tools",
        }

        # QWidget -> QLineEdit
        # "scrollAreaWidgetContents" is the one I have to use.
        for widget in self.ui.scrollAreaWidgetContents.children():
            if isinstance(widget, QLineEdit):
                # [3:] in order to avoid "le_" in object's name.
                key = widget.objectName()[
                    3:
                ]
                widget.setText(str(settings[key]))

    def change_settings(self):
        OK_CANCEL = 1
        OK = 1
        CANCEL = 2

        result = get_permission_dialog(
            "Wollen sie wirklich die Standardeinstellungen ändern?",
            f"{Strings.APP_NAME} | {Strings.DIALOG_SETTINGS}",
            OK_CANCEL,
        )

        if result == OK:
            # QWidget -> QLineEdit
            # "scrollAreaWidgetContents" is the one I have to use.
            for widget in self.ui.scrollAreaWidgetContents.children():
                if isinstance(widget, QLineEdit):
                    # [3:] in order to avoid "le_" in object's name.
                    key = widget.objectName()[
                        3:
                    ]
                    value = widget.text()

                    # If target value is of string type, just pass since it is string by default.
                    if key in [
                        "channel_name",
                        "db_name",
                        "db_csv_name",
                        "leitz_tools",
                    ]:
                        pass
                    else:
                        value = int(value)

                    edit_settings(key, value)

            ctypes.windll.user32.MessageBoxW(
                0,
                "Die Einstellungen wurden erfolgreich geändert. Um die Änderungen zu bestätigen, starten Sie die Software neu.",
                f"{Strings.APP_NAME} | {Strings.DIALOG_SETTINGS}",
                0 | 0x40,
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