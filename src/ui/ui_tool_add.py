# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_ToolAdd(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.shadow_frame = QFrame(self.centralwidget)
        self.shadow_frame.setObjectName(u"shadow_frame")
        self.shadow_frame.setStyleSheet(u"QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 101, 190, 255), stop:1 rgba(81, 47, 154, 255));\n"
"border-radius: 10px;\n"
"}")
        self.shadow_frame.setFrameShape(QFrame.StyledPanel)
        self.shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.shadow_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.label = QLabel(self.shadow_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 16pt;\n"
"font-family: \"Segoe UI Light\";\n"
"font-weight: bold;")
        self.label.setIndent(0)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.shadow_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 12pt;\n"
"font-family: \"Segoe UI Light\";\n"
"margin-bottom: 10px;")
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(0)

        self.verticalLayout.addWidget(self.label_2)

        self.scrollArea = QScrollArea(self.shadow_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit {\n"
"height: 20px;\n"
"font-size: 12pt;\n"
"font-family: \"Segoe UI Light\";\n"
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
"font-family: \"Segoe UI Light\";\n"
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
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 429, 740))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, 9, -1)
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_3)

        self.le_tool_id = QLineEdit(self.scrollAreaWidgetContents)
        self.le_tool_id.setObjectName(u"le_tool_id")

        self.verticalLayout_3.addWidget(self.le_tool_id)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_4)

        self.le_classification_number = QLineEdit(self.scrollAreaWidgetContents)
        self.le_classification_number.setObjectName(u"le_classification_number")

        self.verticalLayout_3.addWidget(self.le_classification_number)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_3.addWidget(self.label_16)

        self.le_strategic_business_number = QLineEdit(self.scrollAreaWidgetContents)
        self.le_strategic_business_number.setObjectName(u"le_strategic_business_number")

        self.verticalLayout_3.addWidget(self.le_strategic_business_number)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.le_tool_diameter = QLineEdit(self.scrollAreaWidgetContents)
        self.le_tool_diameter.setObjectName(u"le_tool_diameter")

        self.verticalLayout_3.addWidget(self.le_tool_diameter)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.le_bore_diameter = QLineEdit(self.scrollAreaWidgetContents)
        self.le_bore_diameter.setObjectName(u"le_bore_diameter")

        self.verticalLayout_3.addWidget(self.le_bore_diameter)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_3.addWidget(self.label_12)

        self.le_tool_cutting_width = QLineEdit(self.scrollAreaWidgetContents)
        self.le_tool_cutting_width.setObjectName(u"le_tool_cutting_width")

        self.verticalLayout_3.addWidget(self.le_tool_cutting_width)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.le_no_of_wings = QLineEdit(self.scrollAreaWidgetContents)
        self.le_no_of_wings.setObjectName(u"le_no_of_wings")

        self.verticalLayout_3.addWidget(self.le_no_of_wings)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.le_total_no_of_wings = QLineEdit(self.scrollAreaWidgetContents)
        self.le_total_no_of_wings.setObjectName(u"le_total_no_of_wings")

        self.verticalLayout_3.addWidget(self.le_total_no_of_wings)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_3.addWidget(self.label_13)

        self.le_cutting_material = QLineEdit(self.scrollAreaWidgetContents)
        self.le_cutting_material.setObjectName(u"le_cutting_material")

        self.verticalLayout_3.addWidget(self.le_cutting_material)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_3.addWidget(self.label_14)

        self.le_cutting_material_quality = QLineEdit(self.scrollAreaWidgetContents)
        self.le_cutting_material_quality.setObjectName(u"le_cutting_material_quality")

        self.verticalLayout_3.addWidget(self.le_cutting_material_quality)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_3.addWidget(self.label_15)

        self.le_body_material = QLineEdit(self.scrollAreaWidgetContents)
        self.le_body_material.setObjectName(u"le_body_material")

        self.verticalLayout_3.addWidget(self.le_body_material)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.le_n_max = QLineEdit(self.scrollAreaWidgetContents)
        self.le_n_max.setObjectName(u"le_n_max")

        self.verticalLayout_3.addWidget(self.le_n_max)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.le_n_opt = QLineEdit(self.scrollAreaWidgetContents)
        self.le_n_opt.setObjectName(u"le_n_opt")

        self.verticalLayout_3.addWidget(self.le_n_opt)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.le_rake_angle = QLineEdit(self.scrollAreaWidgetContents)
        self.le_rake_angle.setObjectName(u"le_rake_angle")

        self.verticalLayout_3.addWidget(self.le_rake_angle)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.frame = QFrame(self.shadow_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"color: #ffffff;\n"
"background-color: rgb(255, 170, 0);\n"
"height: 30px;\n"
"padding-bottom: 5px;\n"
"border-radius: 17px;\n"
"font-size: 12pt;\n"
"font-family: \"Segoe UI Light\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background-color: rgba(255, 170, 0, 0.5);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"color: #ffffff;\n"
"background-color:  rgb(0, 221, 51);\n"
"height: 30px;\n"
"padding-bottom: 5px;\n"
"border-radius: 17px;\n"
"font-size: 12pt;\n"
"font-family: \"Segoe UI Light\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: rgba(255, 255, 255, 0.5);\n"
"background-color: rgba(0, 221, 51, 0.5);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hinzuf\u00fcgen eines neuen Werkzeugs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Falls ein Parameter fehlt, Feld frei lassen", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ID-Nummer", None))
        self.le_tool_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID-Nummer", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Klassifizierungsnummer", None))
        self.le_classification_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Klassifizierungsnummer", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"SGE", None))
        self.le_strategic_business_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SGE", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Werkzeugdurchmesser [mm]", None))
        self.le_tool_diameter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Werkzeugdurchmesser [mm] ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Wellendurchmesser [mm]", None))
        self.le_bore_diameter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wellendurchmesser [mm]", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Schneidenbreite [mm]", None))
        self.le_tool_cutting_width.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Schneidenbreite [mm]", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Schneidenzahl", None))
        self.le_no_of_wings.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Schneidenzahl", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gesamtschneidenanzahl", None))
        self.le_total_no_of_wings.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gesamtschneidenanzahl", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Schneidenwerkstoff", None))
        self.le_cutting_material.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Schneidenwerkstoff", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"PCD Qualit\u00e4t", None))
        self.le_cutting_material_quality.setPlaceholderText(QCoreApplication.translate("MainWindow", u"PCD Qualit\u00e4t", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Grundk\u00f6rpermaterial", None))
        self.le_body_material.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Grundk\u00f6rpermaterial", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Maximale Drehzahl [U/min]", None))
        self.le_n_max.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Maximale Drehzahl [U/min]", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Optimale Drehzahl [U/min]", None))
        self.le_n_opt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Optimale Drehzahl [U/min]", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Spanwinkel [\u00b0]", None))
        self.le_rake_angle.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Spanwinkel [\u00b0]", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Schlie\u00dfen", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Best\u00e4tigen", None))
    # retranslateUi

