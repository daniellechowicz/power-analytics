# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_material_add import Ui_MaterialAdd

from database.database import Material
from settings import *
import ctypes


class MaterialAddWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MaterialAdd()
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
                "MainWindow",
                f"{Strings.APP_NAME} | {Strings.DIALOG_MATERIAL_EDIT}",
                None,
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

    def setup_callbacks(self):
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_2.clicked.connect(lambda: self.delete_material())
        self.ui.pushButton_3.clicked.connect(lambda: self.add_new_material())

    def add_new_material(self):
        material = self.ui.lineEdit.text()
        material_db = Material()
        material_db.insert_into_database(material)
        self.close()

    def delete_material(self):
        material = self.ui.lineEdit.text()
        material_db = Material()
        material_db.delete_from_database(material)
        ctypes.windll.user32.MessageBoxW(
            0,
            "Das Material wurde erfolgreich aus der Datenbank entfernt.",
            f"{Strings.APP_NAME} | {Strings.DIALOG_MATERIAL_EDIT}",
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
