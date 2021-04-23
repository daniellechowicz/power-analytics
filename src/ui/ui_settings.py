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


class Ui_Settings(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(450, 650))
        MainWindow.setMaximumSize(QSize(450, 650))
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
        self.shadow_frame = QFrame(self.centralwidget)
        self.shadow_frame.setObjectName(u"shadow_frame")
        self.shadow_frame.setStyleSheet(
            u"QFrame {\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 101, 190, 255), stop:1 rgba(81, 47, 154, 255));\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.shadow_frame.setFrameShape(QFrame.StyledPanel)
        self.shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.shadow_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(18, 18, 18, 18)
        self.label = QLabel(self.shadow_frame)
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

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.shadow_frame)
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

        self.verticalLayout_3.addWidget(self.label_2)

        self.scrollArea = QScrollArea(self.shadow_frame)
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
            "border-radius: 4px;\n"
            "}"
            "\n"
            "\n"
            "QScrollBar::handle:vertical:hover {\n"
            "background-color: rgba(0, 255, 213);\n"
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
            "background: none;\n"
            "}\n"
            "\n"
            ""
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "background: none;\n"
            "}"
        )
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -488, 375, 938))
        self.scrollAreaWidgetContents.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);"
        )
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"")
        self.label_14.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_14)

        self.le_group_name = QLineEdit(self.scrollAreaWidgetContents)
        self.le_group_name.setObjectName(u"le_group_name")
        self.le_group_name.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.le_group_name)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"")
        self.label_15.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_15)

        self.le_channel_name = QLineEdit(self.scrollAreaWidgetContents)
        self.le_channel_name.setObjectName(u"le_channel_name")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(12)
        self.le_channel_name.setFont(font)
        self.le_channel_name.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.le_channel_name)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label_16)

        self.le_sampling_rate = QLineEdit(self.scrollAreaWidgetContents)
        self.le_sampling_rate.setObjectName(u"le_sampling_rate")
        self.le_sampling_rate.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.le_sampling_rate)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"")
        self.label_17.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_17)

        self.le_resample_factor = QLineEdit(self.scrollAreaWidgetContents)
        self.le_resample_factor.setObjectName(u"le_resample_factor")
        self.le_resample_factor.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.le_resample_factor)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_13)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"")
        self.label_18.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_18)

        self.le_window_size = QLineEdit(self.scrollAreaWidgetContents)
        self.le_window_size.setObjectName(u"le_window_size")
        self.le_window_size.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.le_window_size)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")
        self.label_8.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_8)

        self.le_idle_0 = QLineEdit(self.scrollAreaWidgetContents)
        self.le_idle_0.setObjectName(u"le_idle_0")

        self.verticalLayout_2.addWidget(self.le_idle_0)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_9)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_10)

        self.le_idle_1 = QLineEdit(self.scrollAreaWidgetContents)
        self.le_idle_1.setObjectName(u"le_idle_1")

        self.verticalLayout_2.addWidget(self.le_idle_1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_11)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_12)

        self.le_cutting_0 = QLineEdit(self.scrollAreaWidgetContents)
        self.le_cutting_0.setObjectName(u"le_cutting_0")

        self.verticalLayout_2.addWidget(self.le_cutting_0)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_19)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_20)

        self.le_cutting_1 = QLineEdit(self.scrollAreaWidgetContents)
        self.le_cutting_1.setObjectName(u"le_cutting_1")

        self.verticalLayout_2.addWidget(self.le_cutting_1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font-weight: bold;")

        self.verticalLayout_2.addWidget(self.label_25)

        self.label_26 = QLabel(self.scrollAreaWidgetContents)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_26)

        self.le_leitz_tools = QLineEdit(self.scrollAreaWidgetContents)
        self.le_leitz_tools.setObjectName(u"le_leitz_tools")

        self.verticalLayout_2.addWidget(self.le_leitz_tools)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.frame_3 = QFrame(self.shadow_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnClose = QPushButton(self.frame_3)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy2.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy2)
        self.btnClose.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnClose.setStyleSheet(
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

        self.horizontalLayout_2.addWidget(self.btnClose)

        self.btnAccept = QPushButton(self.frame_3)
        self.btnAccept.setObjectName(u"btnAccept")
        sizePolicy2.setHeightForWidth(self.btnAccept.sizePolicy().hasHeightForWidth())
        self.btnAccept.setSizePolicy(sizePolicy2)
        self.btnAccept.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAccept.setStyleSheet(
            u"QPushButton {\n"
            "color: #ffffff;\n"
            "background-color:  rgb(0, 221, 51);\n"
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
            "background-color: rgba(0, 221, 51, 0.5);\n"
            "}"
        )

        self.horizontalLayout_2.addWidget(self.btnAccept)

        self.verticalLayout_3.addWidget(self.frame_3)

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
            QCoreApplication.translate("MainWindow", u"Einstellungen", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", u"\u00c4ndern der Standardprogrammeinstellungen", None
            )
        )
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"Gruppenname", None)
        )
        self.label_14.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Voraussetzung ist das TDMS-Dateiformat. Um den Gruppennamen zu erhalten, \u00f6ffnen Sie die Datei mit dem Excel Importer.",
                None,
            )
        )
        self.le_group_name.setText("")
        self.le_group_name.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Gruppenname", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"Kanalname", None)
        )
        self.label_15.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Voraussetzung ist das TDMS-Dateiformat.Um den Kanalnamen zu erhalten, \u00f6ffnen Sie die Datei mit dem Excel Importer.",
                None,
            )
        )
        self.le_channel_name.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Kanalname", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", u"Abtastrate [Hz]", None)
        )
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow", u"Im Experiment verwendete Abtastrate [Hz].", None
            )
        )
        self.le_sampling_rate.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Abtastrate [Hz]", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", u"Resampling Faktor", None)
        )
        self.label_17.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Aufgrund der Aufzeichnungsl\u00e4ngen ist die Berechnungszeit relativ aufw\u00e4ndig, daher ist ein Downsampling erforderlich.",
                None,
            )
        )
        self.le_resample_factor.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Resampling Faktor", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"Fenstergr\u00f6\u00dfe", None)
        )
        self.label_18.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Anzahl der Werte \u00fcber die gemittelt werden soll (siehe Median, arithmetischer und quadratischer Mittelwert).",
                None,
            )
        )
        self.le_window_size.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Fenstergr\u00f6\u00dfe", None)
        )
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", u"Leerlaufbeginn [S]", None)
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Standardeinstellung f\u00fcr den ersten\u00a0Messwertdes Leerlaufs.",
                None,
            )
        )
        self.le_idle_0.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Leerlaufbeginn [S]", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", u"Leerlaufende [S]", None)
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Standardeinstellung f\u00fcr den letzten Messwert des Leerlaufs.",
                None,
            )
        )
        self.le_idle_1.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Leerlaufende [S]", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", u"Schnittprozessbeginn [S]", None)
        )
        self.label_12.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Standardeinstellung f\u00fcr den ersten Messwert des Schnittprozesses.",
                None,
            )
        )
        self.le_cutting_0.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Schnittprozessbeginn [S]", None)
        )
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", u"Schnittprozessende [S]", None)
        )
        self.label_20.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Standardeinstellung f\u00fcr den letzten\u00a0Messwert des Schnittprozesses.",
                None,
            )
        )
        self.le_cutting_1.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Schnittprozessende [S]", None)
        )
        self.label_25.setText(
            QCoreApplication.translate("MainWindow", u"Werkzeuge CSV-Dateiname", None)
        )
        self.label_26.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Name der externen CSV-Datei, die Parameter der Werkzeuge enth\u00e4lt.",
                None,
            )
        )
        self.le_leitz_tools.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Werkzeuge CSV-Dateiname", None)
        )
        self.btnClose.setText(
            QCoreApplication.translate("MainWindow", u"Schlie\u00dfen", None)
        )
        self.btnAccept.setText(
            QCoreApplication.translate("MainWindow", u"Best\u00e4tigen", None)
        )

    # retranslateUi
