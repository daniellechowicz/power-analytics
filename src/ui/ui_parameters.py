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


class Ui_Parameters(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.frame_shadow = QFrame(self.centralwidget)
        self.frame_shadow.setObjectName(u"frame_shadow")
        self.frame_shadow.setStyleSheet(
            u"QFrame {\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 101, 190, 255), stop:1 rgba(81, 47, 154, 255));\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.frame_shadow.setFrameShape(QFrame.StyledPanel)
        self.frame_shadow.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_shadow)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, 18, 18, 18)
        self.label = QLabel(self.frame_shadow)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            'font-family: "Segoe UI Light";\n'
            "font-weight: bold;"
        )
        self.label.setIndent(0)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_shadow)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "margin-bottom: 10px;"
        )
        self.label_2.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_2)

        self.scrollArea = QScrollArea(self.frame_shadow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(
            u"QScrollArea {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "QLineEdit {\n"
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
            "}\n"
            "\n"
            "QLabel {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 8pt;\n"
            'font-family: "Segoe UI Light";\n'
            "font-weight: bold;\n"
            "}\n"
            "\n"
            "QScrollBar:vertical {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "width: 15px;\n"
            "margin: 15px 3px 15px 3px;\n"
            "border: 1px transparent #2A2929;\n"
            "border-radius: 4px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical {\n"
            "background-color: #fff;\n"
            "min-height: 5px;\n"
            "bo"
            "rder-radius: 4px;\n"
            "}\n"
            "\n"
            "QScrollBar::handle:vertical:hover {\n"
            "background-color: rgb(0, 255, 213);\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical {\n"
            "margin: 3px 0px 3px 0px;\n"
            "border-image: url(:/);\n"
            "height: 10px;\n"
            "width: 10px;\n"
            "subcontrol-position: top;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical {\n"
            "margin: 3px 0px 3px 0px;\n"
            "border-image: url(:/);\n"
            "height: 10px;\n"
            "width: 10px;\n"
            "subcontrol-position: bottom;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on {\n"
            "border-image: url(:/);\n"
            "height: 10px;\n"
            "width: 10px;\n"
            "subcontrol-position: top;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on {\n"
            "border-image: url(:/);\n"
            "height: 10px;\n"
            "width: 10px;\n"
            "subcontrol-position: bottom;\n"
            "subcontrol-origin: margin;\n"
            "}\n"
            "\n"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "backgroun"
            "d: none;\n"
            "}\n"
            "\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "background: none;\n"
            "}"
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -178, 375, 628))
        self.scrollAreaWidgetContents.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);"
        )
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_3)

        self.le_author = QLineEdit(self.scrollAreaWidgetContents)
        self.le_author.setObjectName(u"le_author")
        self.le_author.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_author)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_4)

        self.le_material = QLineEdit(self.scrollAreaWidgetContents)
        self.le_material.setObjectName(u"le_material")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(12)
        self.le_material.setFont(font)
        self.le_material.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_material)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_5)

        self.le_moisture_content = QLineEdit(self.scrollAreaWidgetContents)
        self.le_moisture_content.setObjectName(u"le_moisture_content")
        self.le_moisture_content.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_moisture_content)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_6)

        self.le_cutting_direction = QLineEdit(self.scrollAreaWidgetContents)
        self.le_cutting_direction.setObjectName(u"le_cutting_direction")
        self.le_cutting_direction.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_cutting_direction)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_13)

        self.le_rotational_speed = QLineEdit(self.scrollAreaWidgetContents)
        self.le_rotational_speed.setObjectName(u"le_rotational_speed")
        self.le_rotational_speed.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_rotational_speed)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_7)

        self.le_feed_speed = QLineEdit(self.scrollAreaWidgetContents)
        self.le_feed_speed.setObjectName(u"le_feed_speed")
        self.le_feed_speed.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_feed_speed)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_8)

        self.le_cutting_width = QLineEdit(self.scrollAreaWidgetContents)
        self.le_cutting_width.setObjectName(u"le_cutting_width")
        self.le_cutting_width.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_cutting_width)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_9)

        self.le_cutting_depth = QLineEdit(self.scrollAreaWidgetContents)
        self.le_cutting_depth.setObjectName(u"le_cutting_depth")
        self.le_cutting_depth.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_cutting_depth)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_10)

        self.le_cutting_angle = QLineEdit(self.scrollAreaWidgetContents)
        self.le_cutting_angle.setObjectName(u"le_cutting_angle")
        self.le_cutting_angle.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_cutting_angle)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_11)

        self.le_tool_id = QLineEdit(self.scrollAreaWidgetContents)
        self.le_tool_id.setObjectName(u"le_tool_id")
        self.le_tool_id.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_tool_id)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_12)

        self.le_comments = QLineEdit(self.scrollAreaWidgetContents)
        self.le_comments.setObjectName(u"le_comments")
        self.le_comments.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.le_comments)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.frame_2 = QFrame(self.frame_shadow)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
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

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
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

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(
            self.pushButton_3.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(
            u"QPushButton {\n"
            "color: #ffffff;\n"
            "background-color: rgb(0, 221, 51);\n"
            "height: 30px;\n"
            "padding-bottom: 5px;\n"
            "border-radius: 17px;;\n"
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
            "background-color: rgba(0, 221, 51, 0.5);\n"
            "}"
        )

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout.addWidget(self.frame_shadow)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", u"Parameter", None))
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", u"Eingabe der Versuchsparameter", None
            )
        )
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.le_author.setText("")
        self.le_author.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Autor", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"* Werkstoff", None)
        )
        self.le_material.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Werkstoff", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", u"Feuchtigkeit [%]", None)
        )
        self.le_moisture_content.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Feuchtigkeit [%]", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", u"* Schnittrichtung", None)
        )
        self.le_cutting_direction.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Schnittrichtung", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"* Drehzahl [U/min]", None)
        )
        self.le_rotational_speed.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Drehzahl [U/min]", None)
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow", u"* Vorschubgeschwindigkeit [m/min]", None
            )
        )
        self.le_feed_speed.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"Vorschubgeschwindigkeit [m/min]", None
            )
        )
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", u"* Schnittbreite [mm]", None)
        )
        self.le_cutting_width.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Schnittbreite [mm]", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", u"* Schnitttiefe [mm]", None)
        )
        self.le_cutting_depth.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Schnitttiefe [mm]", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", u"* Achswinkel λ [\u00b0]", None)
        )
        self.le_cutting_angle.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Achswinkel λ [\u00b0]", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"* ID-Nummer", None)
        )
        self.le_tool_id.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"ID-Nummer", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("MainWindow", u"Kommentare", None)
        )
        self.le_comments.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Kommentare", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"Schlie\u00dfen", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"L\u00f6schen", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", u"Best\u00e4tigen", None)
        )

    # retranslateUi
