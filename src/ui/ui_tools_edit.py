# -*- coding: utf-8 -*-
# WARNING! l_tool_material => l_body_material

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


class Ui_ToolsEdit(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(564, 799)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_shadow = QFrame(self.centralwidget)
        self.frame_shadow.setObjectName(u"frame_shadow")
        self.frame_shadow.setStyleSheet(
            u"QFrame {\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 101, 190, 255), stop:1 rgba(81, 47, 154, 255));\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            "QGroupBox {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}"
        )
        self.frame_shadow.setFrameShape(QFrame.StyledPanel)
        self.frame_shadow.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_shadow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, 18, 18, 18)
        self.label = QLabel(self.frame_shadow)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "margin-bottom: 10px;"
        )
        self.label_2.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_29 = QLabel(self.frame_shadow)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setStyleSheet(
            u"QLabel {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 9pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}"
        )

        self.verticalLayout_2.addWidget(self.label_29)

        self.frame = QFrame(self.frame_shadow)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n" "margin-bottom: 10px;"
        )
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 0))
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
            ""
        )

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(107, 0))
        self.btn_search.setMaximumSize(QSize(107, 16777215))
        self.btn_search.setStyleSheet(
            u"QPushButton {\n"
            "height: 20px;\n"
            "font-size: 9pt;\n"
            'font-family: "Segoe UI Light";\n'
            "padding-bottom: 2.5px;\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 12.5px;\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "color: rgb(220, 220, 220);\n"
            "border: 2px solid rgb(220, 220, 220);\n"
            "background-color: rgba(220, 220, 220, 0.5);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "color: rgb(0, 255, 213);\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "color: rgb(0, 255, 213);\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "background-color: rgba(0, 255, 213, 0.5);\n"
            "}\n"
            ""
        )

        self.horizontalLayout.addWidget(self.btn_search)

        self.btn_add = QPushButton(self.frame)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(107, 0))
        self.btn_add.setMaximumSize(QSize(107, 16777215))
        self.btn_add.setStyleSheet(
            u"QPushButton {\n"
            "height: 20px;\n"
            "font-size: 9pt;\n"
            'font-family: "Segoe UI Light";\n'
            "padding-bottom: 2.5px;\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 12.5px;\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "color: rgb(220, 220, 220);\n"
            "border: 2px solid rgb(220, 220, 220);\n"
            "background-color: rgba(220, 220, 220, 0.5);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "color: rgb(0, 255, 213);\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "color: rgb(0, 255, 213);\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "background-color: rgba(0, 255, 213, 0.5);\n"
            "}\n"
            ""
        )

        self.horizontalLayout.addWidget(self.btn_add)

        self.btn_show_all = QPushButton(self.frame)
        self.btn_show_all.setObjectName(u"btn_show_all")
        self.btn_show_all.setMinimumSize(QSize(107, 0))
        self.btn_show_all.setMaximumSize(QSize(107, 16777215))
        self.btn_show_all.setStyleSheet(
            u"QPushButton {\n"
            "height: 20px;\n"
            "font-size: 9pt;\n"
            'font-family: "Segoe UI Light";\n'
            "padding-bottom: 2.5px;\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 12.5px;\n"
            "background-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QPushButton:disabled {\n"
            "color: rgb(220, 220, 220);\n"
            "border: 2px solid rgb(220, 220, 220);\n"
            "background-color: rgba(220, 220, 220, 0.5);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "color: rgb(0, 255, 213);\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "color: rgb(0, 255, 213);\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "background-color: rgba(0, 255, 213, 0.5);\n"
            "}\n"
            ""
        )

        self.horizontalLayout.addWidget(self.btn_show_all)

        self.verticalLayout_2.addWidget(self.frame)

        self.groupBox = QGroupBox(self.frame_shadow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(
            u"QLabel {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 9pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}"
        )
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.l_bore_diameter = QLabel(self.groupBox)
        self.l_bore_diameter.setObjectName(u"l_bore_diameter")
        self.l_bore_diameter.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_bore_diameter, 7, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setWordWrap(True)

        self.gridLayout.addWidget(self.label_20, 8, 4, 1, 1)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setWordWrap(True)

        self.gridLayout.addWidget(self.label_15, 6, 1, 1, 1)

        self.l_body_material = QLabel(self.groupBox)
        self.l_body_material.setObjectName(u"l_body_material")
        self.l_body_material.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_body_material, 9, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setWordWrap(True)

        self.gridLayout.addWidget(self.label_19, 8, 1, 1, 1)

        self.l_cutting_material_quality = QLabel(self.groupBox)
        self.l_cutting_material_quality.setObjectName(u"l_cutting_material_quality")
        self.l_cutting_material_quality.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_cutting_material_quality, 9, 4, 1, 1)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setWordWrap(True)

        self.gridLayout.addWidget(self.label_16, 8, 0, 1, 1)

        self.l_cutting_material = QLabel(self.groupBox)
        self.l_cutting_material.setObjectName(u"l_cutting_material")
        self.l_cutting_material.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_cutting_material, 9, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setWordWrap(True)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.l_tool_diameter = QLabel(self.groupBox)
        self.l_tool_diameter.setObjectName(u"l_tool_diameter")
        self.l_tool_diameter.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_tool_diameter, 7, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.gridLayout.addWidget(self.label_8, 6, 4, 1, 1)

        self.l_cutting_width = QLabel(self.groupBox)
        self.l_cutting_width.setObjectName(u"l_cutting_width")
        self.l_cutting_width.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_cutting_width, 7, 4, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.l_classification_number = QLabel(self.groupBox)
        self.l_classification_number.setObjectName(u"l_classification_number")
        self.l_classification_number.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_classification_number, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.l_strategic_business_number = QLabel(self.groupBox)
        self.l_strategic_business_number.setObjectName(u"l_strategic_business_number")
        self.l_strategic_business_number.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_strategic_business_number, 1, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setWordWrap(True)

        self.gridLayout.addWidget(self.label_23, 4, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setWordWrap(True)

        self.gridLayout.addWidget(self.label_24, 4, 4, 1, 1)

        self.l_n_max = QLabel(self.groupBox)
        self.l_n_max.setObjectName(u"l_n_max")
        self.l_n_max.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_n_max, 5, 1, 1, 1)

        self.l_n_opt = QLabel(self.groupBox)
        self.l_n_opt.setObjectName(u"l_n_opt")
        self.l_n_opt.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_n_opt, 5, 4, 1, 1)

        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"")
        self.label_27.setWordWrap(True)

        self.gridLayout.addWidget(self.label_27, 4, 0, 1, 1)

        self.l_rake_angle = QLabel(self.groupBox)
        self.l_rake_angle.setObjectName(u"l_rake_angle")
        self.l_rake_angle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_rake_angle, 5, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setWordWrap(True)

        self.gridLayout.addWidget(self.label_11, 0, 4, 1, 1)

        self.l_no_of_wings = QLabel(self.groupBox)
        self.l_no_of_wings.setObjectName(u"l_no_of_wings")
        self.l_no_of_wings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.l_no_of_wings, 1, 4, 1, 1)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_shadow)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet(
            u"QFrame {\n" "background-color: rgba(0, 0, 0, 0);\n" "}"
        )
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.groupBox_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")
        sizePolicy1.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy1)
        self.label_30.setStyleSheet(
            u"QLabel {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 9pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}"
        )
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_30.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_30)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
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

        self.verticalLayout_4.addWidget(self.comboBox)

        self.horizontalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_31 = QLabel(self.frame_4)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)
        self.label_31.setStyleSheet(
            u"QLabel {\n"
            "background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 9pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}"
        )
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_31.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_31)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
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
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lineEdit_2)

        self.horizontalLayout_3.addWidget(self.frame_4)

        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.frame_5 = QFrame(self.frame_shadow)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(
            u"QFrame {\n" "background-color: rgba(0, 0, 0, 0);\n" "}"
        )
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.btn_close = QPushButton(self.frame_5)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setStyleSheet(
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

        self.horizontalLayout_2.addWidget(self.btn_close)

        self.btn_update = QPushButton(self.frame_5)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setStyleSheet(
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

        self.horizontalLayout_2.addWidget(self.btn_update)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.verticalLayout.addWidget(self.frame_shadow)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.label.setText(QCoreApplication.translate("MainWindow", u"Werkzeuge", None))
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", u"Werkzeugparameter in der Datenbank bearbeiten", None
            )
        )
        self.label_29.setText(
            QCoreApplication.translate("MainWindow", u"Suche nach ID", None)
        )
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"ID-Nummer", None)
        )
        self.btn_search.setText(
            QCoreApplication.translate("MainWindow", u"Suchen", None)
        )
        self.btn_add.setText(
            QCoreApplication.translate("MainWindow", u"Hinzuf\u00fcgen", None)
        )
        self.btn_show_all.setText(
            QCoreApplication.translate("MainWindow", u"Alle anzeigen", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", u"Verf\u00fcgbare Parameter", None)
        )
        self.l_bore_diameter.setText("")
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", u"PCD Qualit\u00e4t", None)
        )
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", u"Bohrungsdurchmesser [mm]", None)
        )
        self.l_body_material.setText("")
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", u"Grundk\u00f6rpermaterial", None)
        )
        self.l_cutting_material_quality.setText("")
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", u"Schneidenwerkstoff", None)
        )
        self.l_cutting_material.setText("")
        self.label_7.setText(
            QCoreApplication.translate("MainWindow", u"Werkzeugdurchmesser [mm]", None)
        )
        self.l_tool_diameter.setText("")
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", u"Schneidenbreite [mm]", None)
        )
        self.l_cutting_width.setText("")
        self.label_3.setText(
            QCoreApplication.translate("MainWindow", u"Klassifizierungsnummer", None)
        )
        self.l_classification_number.setText("")
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow", u"Strategische Gesch\u00e4ftszahl", None
            )
        )
        self.l_strategic_business_number.setText("")
        self.label_23.setText(
            QCoreApplication.translate("MainWindow", u"Max. Drehzahl [U/min]", None)
        )
        self.label_24.setText(
            QCoreApplication.translate("MainWindow", u"Optimale Drehzahl [U/min]", None)
        )
        self.l_n_max.setText("")
        self.l_n_opt.setText("")
        self.label_27.setText(
            QCoreApplication.translate("MainWindow", u"Spanwinkel γ [\u00b0]", None)
        )
        self.l_rake_angle.setText("")
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow", u"Schneidenzahl | SZ - Gesamt", None
            )
        )
        self.l_no_of_wings.setText("")
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", u"Bearbeiten", None)
        )
        self.label_30.setText(
            QCoreApplication.translate(
                "MainWindow", u"W\u00e4hlen Sie einen Parameter zum Aktualisieren", None
            )
        )
        self.label_31.setText(
            QCoreApplication.translate(
                "MainWindow", u"Zu aktualisierender Wert des Parameters", None
            )
        )
        self.lineEdit_2.setPlaceholderText("")
        self.btn_close.setText(
            QCoreApplication.translate("MainWindow", u"Schlie\u00dfen", None)
        )
        self.btn_update.setText(
            QCoreApplication.translate("MainWindow", u"Best\u00e4tigen", None)
        )

    # retranslateUi
