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


class Ui_Database(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 720)
        MainWindow.setMinimumSize(QSize(960, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, -1)
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
        self.verticalLayout_3 = QVBoxLayout(self.shadow_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(27, 18, 27, 18)
        self.label = QLabel(self.shadow_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            'font-family: "Segoe UI Light";\n'
            "font-weight: bold;"
        )
        self.label.setIndent(0)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.shadow_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "margin-bottom: 10px;"
        )
        self.label_2.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_2)

        self.frame_4 = QFrame(self.shadow_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 100))
        self.frame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\n" "border-radius: 17.0px;"
        )
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, 18, 18, 18)
        self.tableWidget = QTableWidget(self.frame_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n"
            "font-size: 10pt;\n"
            'font-family: "Segoe UI Light";\n'
            "color: rgb(0, 0, 0);"
        )
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setGridStyle(Qt.DotLine)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame = QFrame(self.shadow_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
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
            "background-color:  rgb(255, 170, 0);\n"
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

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(
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

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout_3.addWidget(self.frame)

        self.verticalLayout.addWidget(self.shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", u"Datenbank", None))
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Erkunden der in der Datenbank verf\u00fcgbaren Daten",
                None,
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"Schlie\u00dfen", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"Speichern als CSV", None)
        )

    # retranslateUi
