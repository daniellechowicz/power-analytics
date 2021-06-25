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


class Ui_DatabaseEdit(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(679, 342)
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

        self.frame_2 = QFrame(self.shadow_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(
            u"QFrame {\n" "background-color: rgba(0, 0, 0, 0);\n" "}"
        )
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(18)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(
            u"QLabel {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 8pt;\n"
            'font-family: "Segoe UI Light";\n'
            "font-weight: bold;\n"
            "}"
        )

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignVCenter)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(
            u"QComboBox {\n"
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
            "QComboBox::drop-down {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "QComboBox:hover {\n"
            "border-bottom: 2px solid rgb(0, 255, 213);\n"
            "border-radius: 0px;\n"
            "}\n"
            "\n"
            "QListView { \n"
            "border: 0px; \n"
            "border-top-left-radius: 0px;\n"
            "border-top-right-radius: 0px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border-bottom-right-radius: 0px;\n"
            "color: rgb(62, 101, 190);\n"
            "background-color: rgb(255, 255, 255);\n"
            "font-weight: normal;\n"
            "selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 101, 190, 255), stop:1 rgba(80, 50, 156, 255));\n"
            "show-decoration-selected: 1;\n"
            "padding: "
            "8px;\n"
            "}"
        )

        self.verticalLayout_3.addWidget(self.comboBox)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(
            u"QLabel {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 8pt;\n"
            'font-family: "Segoe UI Light";\n'
            "font-weight: bold;\n"
            "}"
        )

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignVCenter)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(
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
            ""
        )

        self.verticalLayout_4.addWidget(self.lineEdit_2)

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.verticalLayout_2.addWidget(self.frame_2)

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
            "background-color:  rgb(255, 0, 0);\n"
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
            "background-color: rgba(255, 0, 0, 0.5);\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(
            u"QPushButton {\n"
            "color: #ffffff;\n"
            "background-color: rgb(255, 170, 0);\n"
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
            "background-color: rgba(255, 170, 0, 0.5);\n"
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
            QCoreApplication.translate("MainWindow", u"Datenbank bearbeiten", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Bearbeiten oder L\u00f6schen von Datenbankeintr\u00e4gen",
                None,
            )
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"Measurement ID", None)
        )
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Measurement ID", None)
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow", u"W\u00e4hlen Sie einen Parameter zum Aktualisieren", None
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "MainWindow", u"Zu aktualisierender Wert des Parameters", None
            )
        )
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Optional", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"Schlie\u00dfen", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"L\u00f6schen", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", u"Bearbeiten", None)
        )

    # retranslateUi
