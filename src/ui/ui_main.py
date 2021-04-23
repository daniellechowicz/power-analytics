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

from pyqtgraph import GraphicsLayoutWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 850)
        MainWindow.setMinimumSize(QSize(1200, 850))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 61, 74, 255), stop:1 rgba(71, 74, 120, 255));\n"
            "border-radius: 10px;"
        )
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #ffffff;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.gridLayout.addWidget(self.frame_4, 3, 0, 1, 2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Light")
        font1.setPointSize(16)
        self.labelTitle.setFont(font1)
        self.labelTitle.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n" "color: rgb(255, 255, 255);"
        )

        self.verticalLayout_4.addWidget(self.labelTitle)

        self.labelSubtitle = QLabel(self.centralwidget)
        self.labelSubtitle.setObjectName(u"labelSubtitle")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(12)
        self.labelSubtitle.setFont(font2)
        self.labelSubtitle.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n" "color: rgb(142, 132, 180);"
        )

        self.verticalLayout_4.addWidget(self.labelSubtitle)

        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(120, 0))
        self.frame_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonAdd = QPushButton(self.frame_2)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setMinimumSize(QSize(0, 75))
        self.buttonAdd.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonAdd.setStyleSheet(
            u"QPushButton {\n"
            "border-bottom-right-radius: 15px;\n"
            "border-top-right-radius: 15px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border-top-left-radius: 0px;\n"
            "border-left: 5px solid rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border-left: 5px solid rgb(142, 132, 180);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border-left: 5px solid rgb(85, 170, 255);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}"
        )
        icon = QIcon()
        icon.addFile(
            u"pkgs/src/ui/icons/add-button.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.buttonAdd.setIcon(icon)
        self.buttonAdd.setIconSize(QSize(48, 48))

        self.verticalLayout.addWidget(self.buttonAdd)

        self.buttonAnalyse = QPushButton(self.frame_2)
        self.buttonAnalyse.setObjectName(u"buttonAnalyse")
        self.buttonAnalyse.setMinimumSize(QSize(0, 80))
        self.buttonAnalyse.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonAnalyse.setStyleSheet(
            u"QPushButton {\n"
            "border-bottom-right-radius: 15px;\n"
            "border-top-right-radius: 15px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border-top-left-radius: 0px;\n"
            "border-left: 5px solid rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border-left: 5px solid rgb(142, 132, 180);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border-left: 5px solid rgb(85, 170, 255);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(u"pkgs/src/ui/icons/loupe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonAnalyse.setIcon(icon1)
        self.buttonAnalyse.setIconSize(QSize(48, 48))

        self.verticalLayout.addWidget(self.buttonAnalyse)

        self.buttonDatabase = QPushButton(self.frame_2)
        self.buttonDatabase.setObjectName(u"buttonDatabase")
        self.buttonDatabase.setMinimumSize(QSize(0, 80))
        self.buttonDatabase.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonDatabase.setStyleSheet(
            u"QPushButton {\n"
            "border-bottom-right-radius: 15px;\n"
            "border-top-right-radius: 15px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border-top-left-radius: 0px;\n"
            "border-left: 5px solid rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border-left: 5px solid rgb(142, 132, 180);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border-left: 5px solid rgb(85, 170, 255);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}"
        )
        icon2 = QIcon()
        icon2.addFile(
            u"pkgs/src/ui/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.buttonDatabase.setIcon(icon2)
        self.buttonDatabase.setIconSize(QSize(48, 48))

        self.verticalLayout.addWidget(self.buttonDatabase)

        self.buttonReport = QPushButton(self.frame_2)
        self.buttonReport.setObjectName(u"buttonReport")
        self.buttonReport.setMinimumSize(QSize(0, 80))
        self.buttonReport.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonReport.setStyleSheet(
            u"QPushButton {\n"
            "border-bottom-right-radius: 15px;\n"
            "border-top-right-radius: 15px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border-top-left-radius: 0px;\n"
            "border-left: 5px solid rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border-left: 5px solid rgb(142, 132, 180);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border-left: 5px solid rgb(85, 170, 255);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}"
        )
        icon3 = QIcon()
        icon3.addFile(u"pkgs/src/ui/icons/report.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonReport.setIcon(icon3)
        self.buttonReport.setIconSize(QSize(48, 48))
        self.buttonReport.setFlat(False)

        self.verticalLayout.addWidget(self.buttonReport)

        self.buttonSettings = QPushButton(self.frame_2)
        self.buttonSettings.setObjectName(u"buttonSettings")
        self.buttonSettings.setMinimumSize(QSize(0, 80))
        self.buttonSettings.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonSettings.setStyleSheet(
            u"QPushButton {\n"
            "border-bottom-right-radius: 15px;\n"
            "border-top-right-radius: 15px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border-top-left-radius: 0px;\n"
            "border-left: 5px solid rgba(0, 0, 0, 0);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border-left: 5px solid rgb(142, 132, 180);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border-left: 5px solid rgb(85, 170, 255);\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "}"
        )
        icon4 = QIcon()
        icon4.addFile(
            u"pkgs/src/ui/icons/setting-lines.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.buttonSettings.setIcon(icon4)
        self.buttonSettings.setIconSize(QSize(48, 48))

        self.verticalLayout.addWidget(self.buttonSettings)

        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(130, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 10, 0)
        self.buttonMinimize = QPushButton(self.frame)
        self.buttonMinimize.setObjectName(u"buttonMinimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.buttonMinimize.sizePolicy().hasHeightForWidth()
        )
        self.buttonMinimize.setSizePolicy(sizePolicy2)
        self.buttonMinimize.setMinimumSize(QSize(30, 30))
        self.buttonMinimize.setMaximumSize(QSize(30, 30))
        self.buttonMinimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonMinimize.setStyleSheet(
            u"QPushButton {\n"
            "background-color: rgb(255, 170, 0);\n"
            "border-radius: 15px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 170, 0, 0.8);\n"
            "}"
        )

        self.horizontalLayout_2.addWidget(self.buttonMinimize)

        self.buttonMaximize = QPushButton(self.frame)
        self.buttonMaximize.setObjectName(u"buttonMaximize")
        sizePolicy2.setHeightForWidth(
            self.buttonMaximize.sizePolicy().hasHeightForWidth()
        )
        self.buttonMaximize.setSizePolicy(sizePolicy2)
        self.buttonMaximize.setMinimumSize(QSize(30, 30))
        self.buttonMaximize.setMaximumSize(QSize(30, 30))
        self.buttonMaximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonMaximize.setStyleSheet(
            u"QPushButton {\n"
            "background-color: rgb(0, 221, 51);\n"
            "border-radius: 15px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(0, 221, 51, 0.8);\n"
            "}"
        )

        self.horizontalLayout_2.addWidget(self.buttonMaximize)

        self.buttonClose = QPushButton(self.frame)
        self.buttonClose.setObjectName(u"buttonClose")
        sizePolicy2.setHeightForWidth(self.buttonClose.sizePolicy().hasHeightForWidth())
        self.buttonClose.setSizePolicy(sizePolicy2)
        self.buttonClose.setMinimumSize(QSize(30, 30))
        self.buttonClose.setMaximumSize(QSize(30, 30))
        self.buttonClose.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonClose.setStyleSheet(
            u"QPushButton {\n"
            "background-color: rgb(255, 0, 0);\n"
            "border-radius: 15px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(255, 0, 0, 0.8);\n"
            "}"
        )

        self.horizontalLayout_2.addWidget(self.buttonClose)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2, Qt.AlignRight)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.page_greeting = QWidget()
        self.page_greeting.setObjectName(u"page_greeting")
        self.verticalLayout_12 = QVBoxLayout(self.page_greeting)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_greeting)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        self.horizontalLayout_3 = QHBoxLayout(self.page_add)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_add)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(400, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 30, 0)
        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_5 = QSpacerItem(
            20, 203, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.buttonPathImport = QPushButton(self.frame_11)
        self.buttonPathImport.setObjectName(u"buttonPathImport")
        sizePolicy2.setHeightForWidth(
            self.buttonPathImport.sizePolicy().hasHeightForWidth()
        )
        self.buttonPathImport.setSizePolicy(sizePolicy2)
        self.buttonPathImport.setMinimumSize(QSize(200, 200))
        self.buttonPathImport.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonPathImport.setStyleSheet(
            u"QPushButton:hover {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "border-radius: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border: 5px solid rgb(85, 170, 255);\n"
            "}"
        )
        icon5 = QIcon()
        icon5.addFile(u"pkgs/src/ui/icons/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonPathImport.setIcon(icon5)
        self.buttonPathImport.setIconSize(QSize(128, 128))
        self.buttonPathImport.setFlat(False)

        self.verticalLayout_11.addWidget(self.buttonPathImport, 0, Qt.AlignHCenter)

        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(
            u"margin-top: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_11.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";'
        )
        self.label_16.setWordWrap(False)

        self.verticalLayout_11.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.verticalSpacer_8 = QSpacerItem(
            20, 202, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_11.addItem(self.verticalSpacer_8)

        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_6 = QSpacerItem(
            20, 203, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_14.addItem(self.verticalSpacer_6)

        self.buttonParams = QPushButton(self.frame_12)
        self.buttonParams.setObjectName(u"buttonParams")
        sizePolicy2.setHeightForWidth(
            self.buttonParams.sizePolicy().hasHeightForWidth()
        )
        self.buttonParams.setSizePolicy(sizePolicy2)
        self.buttonParams.setMinimumSize(QSize(200, 200))
        self.buttonParams.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonParams.setStyleSheet(
            u"QPushButton:hover {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "border-radius: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border: 5px solid rgb(85, 170, 255);\n"
            "}"
        )
        icon6 = QIcon()
        icon6.addFile(
            u"pkgs/src/ui/icons/bullet-form.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.buttonParams.setIcon(icon6)
        self.buttonParams.setIconSize(QSize(128, 128))

        self.verticalLayout_14.addWidget(self.buttonParams, 0, Qt.AlignHCenter)

        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(
            u"margin-top: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_14.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_14.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.verticalSpacer_9 = QSpacerItem(
            20, 202, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_14.addItem(self.verticalSpacer_9)

        self.horizontalLayout_4.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_13)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_7 = QSpacerItem(
            20, 203, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_15.addItem(self.verticalSpacer_7)

        self.buttonDone = QPushButton(self.frame_13)
        self.buttonDone.setObjectName(u"buttonDone")
        self.buttonDone.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.buttonDone.sizePolicy().hasHeightForWidth())
        self.buttonDone.setSizePolicy(sizePolicy2)
        self.buttonDone.setMinimumSize(QSize(200, 200))
        self.buttonDone.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonDone.setStyleSheet(
            u"QPushButton:hover {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "border-radius: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border: 5px solid rgb(85, 170, 255);\n"
            "}"
        )
        icon7 = QIcon()
        icon7.addFile(u"pkgs/src/ui/icons/accept.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonDone.setIcon(icon7)
        self.buttonDone.setIconSize(QSize(128, 128))
        self.buttonDone.setCheckable(False)
        self.buttonDone.setChecked(False)

        self.verticalLayout_15.addWidget(self.buttonDone, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(
            u"margin-top: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_15.addWidget(self.label_15, 0, Qt.AlignHCenter)

        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_15.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(
            20, 202, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_15.addItem(self.verticalSpacer_10)

        self.horizontalLayout_4.addWidget(self.frame_13)

        self.horizontalLayout_3.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_add)
        self.page_analyse = QWidget()
        self.page_analyse.setObjectName(u"page_analyse")
        self.verticalLayout_2 = QVBoxLayout(self.page_analyse)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 30, 60, 30)
        self.tabWidget = QTabWidget(self.page_analyse)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setStyleSheet(
            u"QTabBar::tab {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "padding: 10px;\n"
            "color: rgba(255, 255, 255, 0.5);\n"
            "margin-left: 2px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:first {\n"
            "margin-left: 0px;\n"
            "}\n"
            "\n"
            "QTabBar::tab:selected {\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(85, 170, 255);\n"
            "}\n"
            "\n"
            "QTabWidget::pane {\n"
            "background: #ffffff;\n"
            "border-bottom-right-radius: 15px;\n"
            "border-top-right-radius: 15px;\n"
            "} "
        )
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_13 = QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.graphicsViewRangeSelection = GraphicsLayoutWidget(self.tab)
        self.graphicsViewRangeSelection.setObjectName(u"graphicsViewRangeSelection")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.graphicsViewRangeSelection.sizePolicy().hasHeightForWidth()
        )
        self.graphicsViewRangeSelection.setSizePolicy(sizePolicy3)
        self.graphicsViewRangeSelection.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.graphicsViewRangeSelection)

        self.frame_18 = QFrame(self.tab)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy4)
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_7.setSpacing(12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.buttonUpdateGraphs = QPushButton(self.frame_18)
        self.buttonUpdateGraphs.setObjectName(u"buttonUpdateGraphs")
        self.buttonUpdateGraphs.setFont(font)
        self.buttonUpdateGraphs.setStyleSheet(
            u"QPushButton {\n"
            "background-color: rgba(85, 170, 255, 1);\n"
            "border: 2px solid rgb(85, 170, 255);\n"
            "padding: 5px;\n"
            "border-radius: 5px;\n"
            "font-size: 12px;\n"
            "color: rgb(255, 255, 255);\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgba(85, 170, 255, 0.75);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgba(85, 170, 255, 0.5);\n"
            "}"
        )

        self.horizontalLayout_7.addWidget(self.buttonUpdateGraphs)

        self.save_to_database = QCheckBox(self.frame_18)
        self.save_to_database.setObjectName(u"save_to_database")
        sizePolicy2.setHeightForWidth(
            self.save_to_database.sizePolicy().hasHeightForWidth()
        )
        self.save_to_database.setSizePolicy(sizePolicy2)
        self.save_to_database.setStyleSheet(
            u"QCheckBox::indicator {\n"
            "width: 20px;\n"
            "height: 20px;\n"
            "border: 2px solid rgb(85, 170, 255);\n"
            "background: none;\n"
            "}\n"
            "\n"
            "QCheckBox {\n"
            "color: rgb(0, 0, 0);\n"
            "font-size: 12px;\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QCheckBox::indicator:hover {\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            "QCheckBox::indicator:checked {\n"
            "border-radius: 10px;\n"
            "border: 2px solid rgb(85, 170, 255);\n"
            "background-color: rgba(85, 170, 255, 0.5);\n"
            "}"
        )
        self.save_to_database.setChecked(True)

        self.horizontalLayout_7.addWidget(self.save_to_database)

        self.verticalLayout_13.addWidget(self.frame_18)

        self.tabWidget.addTab(self.tab, "")
        self.tab_raw = QWidget()
        self.tab_raw.setObjectName(u"tab_raw")
        self.verticalLayout_3 = QVBoxLayout(self.tab_raw)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.graphicsViewRaw = GraphicsLayoutWidget(self.tab_raw)
        self.graphicsViewRaw.setObjectName(u"graphicsViewRaw")
        sizePolicy3.setHeightForWidth(
            self.graphicsViewRaw.sizePolicy().hasHeightForWidth()
        )
        self.graphicsViewRaw.setSizePolicy(sizePolicy3)
        self.graphicsViewRaw.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.graphicsViewRaw)

        self.frame_5 = QFrame(self.tab_raw)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(0, 125))
        self.frame_5.setStyleSheet(
            u"color: #ffffff;\n" "background-color: rgb(85, 170, 255);"
        )
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Light")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 5)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        font4 = QFont()
        font4.setFamily(u"Segoe UI Light")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 1, 4, 1, 1)

        self.labelMinRaw = QLabel(self.frame_5)
        self.labelMinRaw.setObjectName(u"labelMinRaw")
        self.labelMinRaw.setFont(font4)
        self.labelMinRaw.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelMinRaw.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelMinRaw, 2, 0, 1, 1)

        self.labelMeanRaw = QLabel(self.frame_5)
        self.labelMeanRaw.setObjectName(u"labelMeanRaw")
        self.labelMeanRaw.setFont(font4)
        self.labelMeanRaw.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelMeanRaw.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelMeanRaw, 2, 2, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)

        self.labelMaxRaw = QLabel(self.frame_5)
        self.labelMaxRaw.setObjectName(u"labelMaxRaw")
        self.labelMaxRaw.setFont(font4)
        self.labelMaxRaw.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelMaxRaw.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelMaxRaw, 2, 1, 1, 1)

        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.labelSTDRaw = QLabel(self.frame_5)
        self.labelSTDRaw.setObjectName(u"labelSTDRaw")
        self.labelSTDRaw.setFont(font4)
        self.labelSTDRaw.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelSTDRaw.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelSTDRaw, 2, 4, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 1, 3, 1, 1)

        self.labelMedianRaw = QLabel(self.frame_5)
        self.labelMedianRaw.setObjectName(u"labelMedianRaw")
        self.labelMedianRaw.setFont(font4)
        self.labelMedianRaw.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelMedianRaw.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelMedianRaw, 2, 3, 1, 1)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.verticalLayout_3.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab_raw, "")
        self.tab_mm = QWidget()
        self.tab_mm.setObjectName(u"tab_mm")
        self.verticalLayout_7 = QVBoxLayout(self.tab_mm)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.graphicsViewMM = GraphicsLayoutWidget(self.tab_mm)
        self.graphicsViewMM.setObjectName(u"graphicsViewMM")
        sizePolicy3.setHeightForWidth(
            self.graphicsViewMM.sizePolicy().hasHeightForWidth()
        )
        self.graphicsViewMM.setSizePolicy(sizePolicy3)
        self.graphicsViewMM.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.graphicsViewMM)

        self.frame_8 = QFrame(self.tab_mm)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMinimumSize(QSize(0, 125))
        self.frame_8.setStyleSheet(
            u"color: #ffffff;\n" "background-color: rgb(85, 170, 255);"
        )
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.labelMeanMM = QLabel(self.frame_8)
        self.labelMeanMM.setObjectName(u"labelMeanMM")
        self.labelMeanMM.setFont(font4)
        self.labelMeanMM.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelMeanMM.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelMeanMM, 2, 2, 1, 1)

        self.label_48 = QLabel(self.frame_8)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font4)
        self.label_48.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_48, 1, 4, 1, 1)

        self.label_53 = QLabel(self.frame_8)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font3)
        self.label_53.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_53, 0, 0, 1, 5)

        self.labelMinMM = QLabel(self.frame_8)
        self.labelMinMM.setObjectName(u"labelMinMM")
        self.labelMinMM.setFont(font4)
        self.labelMinMM.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelMinMM.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelMinMM, 2, 0, 1, 1)

        self.labelMedianMM = QLabel(self.frame_8)
        self.labelMedianMM.setObjectName(u"labelMedianMM")
        self.labelMedianMM.setFont(font4)
        self.labelMedianMM.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelMedianMM.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelMedianMM, 2, 3, 1, 1)

        self.label_47 = QLabel(self.frame_8)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font4)
        self.label_47.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_47, 1, 3, 1, 1)

        self.label_42 = QLabel(self.frame_8)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font4)
        self.label_42.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_42, 1, 0, 1, 1)

        self.labelMaxMM = QLabel(self.frame_8)
        self.labelMaxMM.setObjectName(u"labelMaxMM")
        self.labelMaxMM.setFont(font4)
        self.labelMaxMM.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelMaxMM.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelMaxMM, 2, 1, 1, 1)

        self.label_45 = QLabel(self.frame_8)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font4)
        self.label_45.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_45, 1, 1, 1, 1)

        self.labelSTDMM = QLabel(self.frame_8)
        self.labelSTDMM.setObjectName(u"labelSTDMM")
        self.labelSTDMM.setFont(font4)
        self.labelSTDMM.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.labelSTDMM.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.labelSTDMM, 2, 4, 1, 1)

        self.label_49 = QLabel(self.frame_8)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font4)
        self.label_49.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_49, 1, 2, 1, 1)

        self.verticalLayout_7.addWidget(self.frame_8)

        self.tabWidget.addTab(self.tab_mm, "")
        self.tab_psd = QWidget()
        self.tab_psd.setObjectName(u"tab_psd")
        self.verticalLayout_10 = QVBoxLayout(self.tab_psd)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.graphicsViewPSD = GraphicsLayoutWidget(self.tab_psd)
        self.graphicsViewPSD.setObjectName(u"graphicsViewPSD")
        sizePolicy3.setHeightForWidth(
            self.graphicsViewPSD.sizePolicy().hasHeightForWidth()
        )
        self.graphicsViewPSD.setSizePolicy(sizePolicy3)
        self.graphicsViewPSD.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.graphicsViewPSD)

        self.tabWidget.addTab(self.tab_psd, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_analyse)
        self.page_db_menu = QWidget()
        self.page_db_menu.setObjectName(u"page_db_menu")
        self.horizontalLayout = QHBoxLayout(self.page_db_menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_14 = QFrame(self.page_db_menu)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_11 = QSpacerItem(
            20, 194, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_17.addItem(self.verticalSpacer_11)

        self.buttonDatabaseShow = QPushButton(self.frame_14)
        self.buttonDatabaseShow.setObjectName(u"buttonDatabaseShow")
        sizePolicy2.setHeightForWidth(
            self.buttonDatabaseShow.sizePolicy().hasHeightForWidth()
        )
        self.buttonDatabaseShow.setSizePolicy(sizePolicy2)
        self.buttonDatabaseShow.setMinimumSize(QSize(200, 200))
        self.buttonDatabaseShow.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonDatabaseShow.setStyleSheet(
            u"QPushButton:hover {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "border-radius: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border: 5px solid rgb(85, 170, 255);\n"
            "}"
        )
        icon8 = QIcon()
        icon8.addFile(
            u"pkgs/src/ui/icons/spreadsheet-cell.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.buttonDatabaseShow.setIcon(icon8)
        self.buttonDatabaseShow.setIconSize(QSize(128, 128))

        self.verticalLayout_17.addWidget(self.buttonDatabaseShow, 0, Qt.AlignHCenter)

        self.label_19 = QLabel(self.frame_14)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(
            u"margin-top: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_17.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.label_20 = QLabel(self.frame_14)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_17.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.verticalSpacer_14 = QSpacerItem(
            20, 193, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_17.addItem(self.verticalSpacer_14)

        self.horizontalLayout.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.page_db_menu)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_12 = QSpacerItem(
            20, 194, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_18.addItem(self.verticalSpacer_12)

        self.buttonShowBoxplots = QPushButton(self.frame_15)
        self.buttonShowBoxplots.setObjectName(u"buttonShowBoxplots")
        sizePolicy2.setHeightForWidth(
            self.buttonShowBoxplots.sizePolicy().hasHeightForWidth()
        )
        self.buttonShowBoxplots.setSizePolicy(sizePolicy2)
        self.buttonShowBoxplots.setMinimumSize(QSize(200, 200))
        self.buttonShowBoxplots.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonShowBoxplots.setStyleSheet(
            u"QPushButton:hover {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "border-radius: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border: 5px solid rgb(85, 170, 255);\n"
            "}"
        )
        icon9 = QIcon()
        icon9.addFile(u"pkgs/src/ui/icons/plot.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonShowBoxplots.setIcon(icon9)
        self.buttonShowBoxplots.setIconSize(QSize(128, 128))

        self.verticalLayout_18.addWidget(self.buttonShowBoxplots, 0, Qt.AlignHCenter)

        self.label_21 = QLabel(self.frame_15)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(
            u"margin-top: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_18.addWidget(self.label_21, 0, Qt.AlignHCenter)

        self.label_22 = QLabel(self.frame_15)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_18.addWidget(self.label_22, 0, Qt.AlignHCenter)

        self.verticalSpacer_15 = QSpacerItem(
            20, 193, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_18.addItem(self.verticalSpacer_15)

        self.horizontalLayout.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.page_db_menu)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_13 = QSpacerItem(
            20, 194, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_16.addItem(self.verticalSpacer_13)

        self.buttonDatabaseExport = QPushButton(self.frame_16)
        self.buttonDatabaseExport.setObjectName(u"buttonDatabaseExport")
        sizePolicy2.setHeightForWidth(
            self.buttonDatabaseExport.sizePolicy().hasHeightForWidth()
        )
        self.buttonDatabaseExport.setSizePolicy(sizePolicy2)
        self.buttonDatabaseExport.setMinimumSize(QSize(200, 200))
        self.buttonDatabaseExport.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonDatabaseExport.setStyleSheet(
            u"QPushButton:hover {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "border-radius: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border: 5px solid rgb(85, 170, 255);\n"
            "}"
        )
        icon10 = QIcon()
        icon10.addFile(
            u"pkgs/src/ui/icons/excel-file.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.buttonDatabaseExport.setIcon(icon10)
        self.buttonDatabaseExport.setIconSize(QSize(128, 128))

        self.verticalLayout_16.addWidget(self.buttonDatabaseExport, 0, Qt.AlignHCenter)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(
            u"margin-top: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_16.addWidget(self.label_23, 0, Qt.AlignHCenter)

        self.label_24 = QLabel(self.frame_16)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_16.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.verticalSpacer_16 = QSpacerItem(
            20, 193, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_16.addItem(self.verticalSpacer_16)

        self.horizontalLayout.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.page_db_menu)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.horizontalLayout_6 = QHBoxLayout(self.page_settings)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_6 = QFrame(self.page_settings)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.btn_settings = QPushButton(self.frame_6)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy2.setHeightForWidth(
            self.btn_settings.sizePolicy().hasHeightForWidth()
        )
        self.btn_settings.setSizePolicy(sizePolicy2)
        self.btn_settings.setMinimumSize(QSize(200, 200))
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setStyleSheet(
            u"QPushButton:hover {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "border-radius: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border: 5px solid rgb(85, 170, 255);\n"
            "}"
        )
        icon11 = QIcon()
        icon11.addFile(
            u"pkgs/src/ui/icons/computer.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_settings.setIcon(icon11)
        self.btn_settings.setIconSize(QSize(128, 128))

        self.verticalLayout_5.addWidget(self.btn_settings, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(
            u"margin-top: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_5.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";'
        )
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.page_settings)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.btn_tools_edit = QPushButton(self.frame_10)
        self.btn_tools_edit.setObjectName(u"btn_tools_edit")
        sizePolicy2.setHeightForWidth(
            self.btn_tools_edit.sizePolicy().hasHeightForWidth()
        )
        self.btn_tools_edit.setSizePolicy(sizePolicy2)
        self.btn_tools_edit.setMinimumSize(QSize(200, 200))
        self.btn_tools_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tools_edit.setStyleSheet(
            u"QPushButton:hover {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "border-radius: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border: 5px solid rgb(85, 170, 255);\n"
            "}"
        )
        icon12 = QIcon()
        icon12.addFile(
            u"pkgs/src/ui/icons/wheel-saw.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_tools_edit.setIcon(icon12)
        self.btn_tools_edit.setIconSize(QSize(128, 128))

        self.verticalLayout_9.addWidget(self.btn_tools_edit, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.frame_10)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(
            u"margin-top: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_9.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";'
        )
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6.addWidget(self.frame_10)

        self.frame_17 = QFrame(self.page_settings)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_17)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_17 = QSpacerItem(
            20, 177, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_19.addItem(self.verticalSpacer_17)

        self.btn_tools_replace = QPushButton(self.frame_17)
        self.btn_tools_replace.setObjectName(u"btn_tools_replace")
        sizePolicy2.setHeightForWidth(
            self.btn_tools_replace.sizePolicy().hasHeightForWidth()
        )
        self.btn_tools_replace.setSizePolicy(sizePolicy2)
        self.btn_tools_replace.setMinimumSize(QSize(200, 200))
        self.btn_tools_replace.setMaximumSize(QSize(16777215, 16777215))
        self.btn_tools_replace.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tools_replace.setStyleSheet(
            u"QPushButton:hover {\n"
            "background-color: rgba(142, 132, 180, 0.5);\n"
            "border-radius: 20px;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "border: 5px solid rgb(85, 170, 255);\n"
            "}"
        )
        icon13 = QIcon()
        icon13.addFile(
            u"pkgs/src/ui/icons/replace.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_tools_replace.setIcon(icon13)
        self.btn_tools_replace.setIconSize(QSize(128, 128))

        self.verticalLayout_19.addWidget(self.btn_tools_replace, 0, Qt.AlignHCenter)

        self.label_25 = QLabel(self.frame_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(
            u"margin-top: 10px;\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            "font-weight: bold;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_19.addWidget(self.label_25, 0, Qt.AlignHCenter)

        self.label_26 = QLabel(self.frame_17)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";'
        )
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_26, 0, Qt.AlignHCenter)

        self.verticalSpacer_18 = QSpacerItem(
            20, 176, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_19.addItem(self.verticalSpacer_18)

        self.horizontalLayout_6.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.page_settings)

        self.gridLayout.addWidget(self.stackedWidget, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u00a9 2021 Leitz GmbH & Co. KG All Rights Reserved",
                None,
            )
        )
        self.labelTitle.setText(
            QCoreApplication.translate("MainWindow", u"Power Analytics", None)
        )
        self.labelSubtitle.setText(
            QCoreApplication.translate(
                "MainWindow", u"Toolkit zur Analyse der Schnittleistung", None
            )
        )
        self.buttonAdd.setText("")
        self.buttonAnalyse.setText("")
        self.buttonDatabase.setText("")
        self.buttonReport.setText("")
        self.buttonSettings.setText("")
        self.buttonMinimize.setText("")
        self.buttonMaximize.setText("")
        self.buttonClose.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pfad", None))
        self.label_16.setText(
            QCoreApplication.translate(
                "MainWindow", u"Angeben\u00a0des Orts der\u00a0Messdatei", None
            )
        )
        self.buttonParams.setText("")
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", u"Parameter", None)
        )
        self.label_17.setText(
            QCoreApplication.translate(
                "MainWindow", u"Eingabe der dazugeh\u00f6rigen Parameter", None
            )
        )
        self.buttonDone.setText("")
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", u"Best\u00e4tigen", None)
        )
        self.label_18.setText(
            QCoreApplication.translate(
                "MainWindow", u"Weiter zum n\u00e4chsten Schritt", None
            )
        )
        self.buttonUpdateGraphs.setText(
            QCoreApplication.translate("MainWindow", u"Update", None)
        )
        self.save_to_database.setText(
            QCoreApplication.translate(
                "MainWindow", u"Hinzuf\u00fcgen zur Datenbank", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", u"Bereiche asuw\u00e4hlen", None),
        )
        self.label_14.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Statistik\u00a0zur Leistungsmessung innerhalb des\u00a0gew\u00e4hlten Bereichs [Watt]",
                None,
            )
        )
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", u"Standardabweichung", None)
        )
        self.labelMinRaw.setText("")
        self.labelMeanRaw.setText("")
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"Mittelwert", None)
        )
        self.labelMaxRaw.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Minimum", None))
        self.labelSTDRaw.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Median", None))
        self.labelMedianRaw.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Maximum", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_raw),
            QCoreApplication.translate("MainWindow", u"Rohdaten", None),
        )
        self.labelMeanMM.setText("")
        self.label_48.setText(
            QCoreApplication.translate("MainWindow", u"Standardabweichung", None)
        )
        self.label_53.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Statistik\u00a0zur Leistungsmessung innerhalb des\u00a0gew\u00e4hlten Bereichs [Watt]",
                None,
            )
        )
        self.labelMinMM.setText("")
        self.labelMedianMM.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Median", None))
        self.label_42.setText(
            QCoreApplication.translate("MainWindow", u"Minimum", None)
        )
        self.labelMaxMM.setText("")
        self.label_45.setText(
            QCoreApplication.translate("MainWindow", u"Maximum", None)
        )
        self.labelSTDMM.setText("")
        self.label_49.setText(
            QCoreApplication.translate("MainWindow", u"Mittelwert", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_mm),
            QCoreApplication.translate("MainWindow", u"Gleitender Mittelwert", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_psd),
            QCoreApplication.translate("MainWindow", u"Spektrum", None),
        )
        self.buttonDatabaseShow.setText("")
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", u"Tabellenform", None)
        )
        self.label_20.setText(
            QCoreApplication.translate(
                "MainWindow", u"Anzeigen der gesammelten Daten", None
            )
        )
        self.buttonShowBoxplots.setText("")
        self.label_21.setText(
            QCoreApplication.translate("MainWindow", u"Datenvisualisierung", None)
        )
        self.label_22.setText(
            QCoreApplication.translate(
                "MainWindow", u"Visualisierung der gesammelten\u00a0Daten", None
            )
        )
        self.buttonDatabaseExport.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_24.setText(
            QCoreApplication.translate(
                "MainWindow", u"Exportieren\u00a0als\u00a0CSV Datei", None
            )
        )
        self.btn_settings.setText("")
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", u"Einstellungen", None)
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow", u"Standardprogrammeinstellungen bearbeiten", None
            )
        )
        self.btn_tools_edit.setText("")
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", u"Werkzeuge", None)
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Hinzuf\u00fcgen, \u00e4ndern oder erg\u00e4nzen eines Werkzeuges",
                None,
            )
        )
        self.btn_tools_replace.setText("")
        self.label_25.setText(
            QCoreApplication.translate("MainWindow", u"Ersetzen", None)
        )
        self.label_26.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"Einspielen einer aktuelleren\u00a0 Werkzeugdatenbank",
                None,
            )
        )

    # retranslateUi
