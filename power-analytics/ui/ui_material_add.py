# -*- coding: utf-8 -*-

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QUrl,
    Qt,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *


class Ui_MaterialAdd(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(607, 250)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.shadow_frame = QFrame(self.centralwidget)
        self.shadow_frame.setObjectName(u"shadow_frame")
        self.shadow_frame.setStyleSheet(
            u"QFrame {\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 101, 190, 255), stop:1 rgba(81, 47, 154, 255));\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            "\n"
            ""
        )
        self.shadow_frame.setFrameShape(QFrame.StyledPanel)
        self.shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.shadow_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, 18, 18, 18)
        self.label = QLabel(self.shadow_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            'font-family: "Segoe UI Light";\n'
            "font-weight: bold;"
        )

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.shadow_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "margin-bottom: 10px;"
        )

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.shadow_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(
            u"QLabel {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 8pt;\n"
            'font-family: "Segoe UI Light";\n'
            "font-weight: bold;\n"
            "}"
        )

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.shadow_frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(
            u"QLineEdit {\n"
            "height: 20px;\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "padding-left: 10px;\n"
            "padding-bottom: 5px;\n"
            "border-bottom: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 0px;\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "border-bottom: 2px solid rgb(0, 255, 213);\n"
            "border-radius: 0px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "border-bottom: 2px solid rgb(0, 255, 213);\n"
            "border-radius: 0px;\n"
            "}"
        )

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.frame = QFrame(self.shadow_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(
            u"QPushButton {\n"
            "color: #ffffff;\n"
            "background-color: rgb(255, 170, 0);\n"
            "height: 30px;\n"
            "padding-bottom: 5px;\n"
            "border-radius: 17px;\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border: 2px solid rgb(255, 255, 255)\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "color: rgba(255, 255, 255, 0.5);\n"
            "background-color: rgba(255, 170, 0, 0.5);\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(
            u"QPushButton {\n"
            "color: #ffffff;\n"
            "background-color: rgb(255, 0, 0);\n"
            "height: 30px;\n"
            "padding-bottom: 5px;\n"
            "border-radius: 17px;\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border: 2px solid rgb(255, 255, 255)\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "color: rgba(255, 255, 255, 0.5);\n"
            "background-color: rgba(255, 0, 0, 0.5);\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(
            u"QPushButton {\n"
            "color: #ffffff;\n"
            "background-color:  rgb(0, 221, 51);\n"
            "height: 30px;\n"
            "padding-left: 10px;\n"
            "padding-bottom: 5px;\n"
            "border-radius: 17.0px;\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "color: rgba(255, 255, 255, 0.5);\n"
            "background-color: rgba(0, 221, 51, 0.5);\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout.addWidget(self.shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow", u"Werkstoff hinzuf\u00fcgen oder entfernen", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Neues Werkstoff hinzuf\u00fcgen oder bestehendes Werkstoff l\u00f6schen",
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"Werkstoff", None)
        )
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Werkstoff", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"Schlie\u00dfen", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"L\u00f6schen", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", u"Hinzufügen", None)
        )

    # retranslateUi
