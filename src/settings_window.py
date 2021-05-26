# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_settings import Ui_Settings

from settings import edit_settings
import ctypes
import json


class SettingsWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_initial_view()
        self.setup_type_validators()
        self.define_callbacks()
        self.set_from_json()

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
                "MainWindow", "Power Analytics | Einstellungen", None
            )
        )

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def setup_type_validators(self):
        self.only_int = QtGui.QIntValidator()

        self.ui.le_sampling_rate.setValidator(self.only_int)
        self.ui.le_resample_factor.setValidator(self.only_int)
        self.ui.le_window_size.setValidator(self.only_int)
        self.ui.le_idle_0.setValidator(self.only_int)
        self.ui.le_idle_1.setValidator(self.only_int)
        self.ui.le_cutting_0.setValidator(self.only_int)
        self.ui.le_cutting_1.setValidator(self.only_int)

    def define_callbacks(self):
        self.ui.btnClose.clicked.connect(lambda: self.close())
        self.ui.btnAccept.clicked.connect(lambda: self.save())

    def set_from_json(self):
        with open("settings.json") as json_file:
            settings = json.load(json_file)

        self.corresponding_keys = {
            "Group name": "group_name",
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
        # "scrollAreaWidgetContents" is the one I have to use
        for widget in self.ui.scrollAreaWidgetContents.children():
            if isinstance(widget, QLineEdit):
                key = widget.objectName()[
                    3:
                ]  # [3:] in order to avoid "le_" in object's name
                widget.setText(str(settings[key]))

    def get_permission_dialog(self, text, title, utype):
        user32 = ctypes.WinDLL("user32", use_last_error=True)
        msg_box = user32.MessageBoxW
        result = msg_box(None, text, title, utype)
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return result

    def save(self):
        OK_CANCEL = 1
        OK = 1
        CANCEL = 2

        result = self.get_permission_dialog(
            "Wollen sie wirklich die Standardeinstellungen ändern?",
            "Power Analytics | Einstellungen",
            OK_CANCEL,
        )

        if result == OK:
            # QWidget -> QLineEdit
            # "scrollAreaWidgetContents" is the one I have to use
            for widget in self.ui.scrollAreaWidgetContents.children():
                if isinstance(widget, QLineEdit):
                    key = widget.objectName()[
                        3:
                    ]  # [3:] in order to avoid "le_" in object's name
                    value = widget.text()
                    # If target value is of string type, just pass since it is string by default
                    if key in [
                        "group_name",
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
                "Die Einstellungen wurden erfolgreich geändert",
                "Power Analytics | Einstellungen",
                0 | 0x40,
            )
        else:
            pass

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


if __name__ == "__main__":
    from PySide2.QtWidgets import *
    import sys

    app = QApplication(sys.argv)
    window = SettingsWindow()
    sys.exit(app.exec_())
