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


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(794, 427)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setGeometry(QRect(9, 9, 780, 418))
        self.dropShadowFrame.setAutoFillBackground(False)
        self.dropShadowFrame.setStyleSheet(u"")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.dropShadowFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(72, 72))
        self.label.setMaximumSize(QSize(72, 72))
        self.label.setPixmap(
            QPixmap(u"pkgs/src/ui/splash_screen/logo.png")
        )
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignRight)

        self.verticalSpacer = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout.addItem(self.verticalSpacer)

        self.labelTitle = QLabel(self.dropShadowFrame)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(
            u"font-size: 60px;\n"
            'font-family: "Segoe UI";\n'
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(98, 114, 164);"
        )

        self.verticalLayout.addWidget(self.labelTitle, 0, Qt.AlignHCenter)

        self.labelDescription = QLabel(self.dropShadowFrame)
        self.labelDescription.setObjectName(u"labelDescription")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelDescription.sizePolicy().hasHeightForWidth()
        )
        self.labelDescription.setSizePolicy(sizePolicy)
        self.labelDescription.setStyleSheet(
            u"font-size: 26px;\n"
            'font-family: "Segoe UI";\n'
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(98, 114, 164);"
        )

        self.verticalLayout.addWidget(self.labelDescription, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame = QFrame(self.dropShadowFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(
            100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setStyleSheet(
            u"QProgressBar {\n"
            "background-color: rgb(98, 114, 164);\n"
            "color: rgb(255, 255, 255);\n"
            "border-style: none;\n"
            "border-radius: 10px;\n"
            "text-align: center;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk {\n"
            "border-radius: 10px;\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(183, 137, 104, 255), stop:1 rgba(225, 181, 154, 255));\n"
            "}"
        )
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.horizontalSpacer_2 = QSpacerItem(
            100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.labelCredits = QLabel(self.dropShadowFrame)
        self.labelCredits.setObjectName(u"labelCredits")
        self.labelCredits.setStyleSheet(
            u"font-size: 16px;\n"
            'font-family: "Segoe UI";\n'
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(98, 114, 164);"
        )

        self.verticalLayout.addWidget(self.labelCredits, 0, Qt.AlignRight)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(9, 9, 780, 418))
        self.label_4.setPixmap(
            QPixmap(u"pkgs/src/ui/splash_screen/background.jpg")
        )
        self.label_4.setScaledContents(True)
        SplashScreen.setCentralWidget(self.centralwidget)
        self.label_4.raise_()
        self.dropShadowFrame.raise_()

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)

    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(
            QCoreApplication.translate("SplashScreen", u"MainWindow", None)
        )
        self.label.setText("")
        self.labelTitle.setText(
            QCoreApplication.translate(
                "SplashScreen",
                u'<html><head/><body><p><span style=" font-weight:600;">POWER </span>ANALYTICS</p></body></html>',
                None,
            )
        )
        self.labelDescription.setText(
            QCoreApplication.translate(
                "SplashScreen",
                u'<html><head/><body><p><span style=" font-weight:600;">GAINING</span> KNOWLEDGE</p></body></html>',
                None,
            )
        )
        self.labelCredits.setText(
            QCoreApplication.translate(
                "SplashScreen",
                u'<html><head/><body><p><span style=" font-weight:600;">Created by</span> Kompetenzzentrum Holz GmbH</p></body></html>',
                None,
            )
        )
        self.label_4.setText("")

    # retranslateUi
