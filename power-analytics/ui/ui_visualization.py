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


class Ui_Visualization(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 800)
        MainWindow.setStyleSheet(
            u"QWidget {\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 101, 190, 255), stop:1 rgba(81, 47, 154, 255));\n"
            "}"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(
            u"QFrame {\n"
            "margin-top: 10px;\n"
            "margin-right: 10px;\n"
            "background-color: rgb(255, 255, 255);\n"
            "border-radius: 10px;\n"
            "}"
        )
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.graphics_view = GraphicsLayoutWidget(self.frame_3)
        self.graphics_view.setObjectName(u"graphics_view")

        self.verticalLayout_20.addWidget(self.graphics_view)

        self.horizontalLayout.addWidget(self.frame_3)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(
            u"QGroupBox {\n"
            "background-color: rgb(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QLabel {\n"
            "background-color: rgb(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 9pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}"
        )
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setSpacing(18)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 9)
        self.groupBox_18 = QGroupBox(self.groupBox_4)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.groupBox_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_21)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_18.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_18)

        self.material_l = QLabel(self.frame_21)
        self.material_l.setObjectName(u"material_l")
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.material_l.setFont(font)
        self.material_l.setAlignment(Qt.AlignCenter)
        self.material_l.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.material_l)

        self.label_20 = QLabel(self.frame_21)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_20.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.label_20)

        self.moisture_content_l = QLabel(self.frame_21)
        self.moisture_content_l.setObjectName(u"moisture_content_l")
        self.moisture_content_l.setFont(font)
        self.moisture_content_l.setAlignment(Qt.AlignCenter)
        self.moisture_content_l.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.moisture_content_l)

        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_22.addWidget(self.label_19)

        self.label_21 = QLabel(self.frame_21)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_22.addWidget(self.label_21)

        self.label_27 = QLabel(self.frame_21)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_22.addWidget(self.label_27)

        self.label_23 = QLabel(self.frame_21)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_22.addWidget(self.label_23)

        self.label_25 = QLabel(self.frame_21)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_22.addWidget(self.label_25)

        self.label_29 = QLabel(self.frame_21)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_22.addWidget(self.label_29)

        self.verticalLayout_18.addWidget(self.frame_21)

        self.horizontalLayout_3.addWidget(self.groupBox_18)

        self.groupBox_21 = QGroupBox(self.groupBox_4)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_21)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.groupBox_21)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_19)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_22 = QLabel(self.frame_19)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_22.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_22)

        self.cutting_direction_l = QLabel(self.frame_19)
        self.cutting_direction_l.setObjectName(u"cutting_direction_l")
        self.cutting_direction_l.setFont(font)
        self.cutting_direction_l.setAlignment(Qt.AlignCenter)
        self.cutting_direction_l.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.cutting_direction_l)

        self.label_26 = QLabel(self.frame_19)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_26.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_26)

        self.rotational_speed_l = QLabel(self.frame_19)
        self.rotational_speed_l.setObjectName(u"rotational_speed_l")
        self.rotational_speed_l.setFont(font)
        self.rotational_speed_l.setAlignment(Qt.AlignCenter)
        self.rotational_speed_l.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.rotational_speed_l)

        self.label_24 = QLabel(self.frame_19)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_24.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_24)

        self.feed_speed_l = QLabel(self.frame_19)
        self.feed_speed_l.setObjectName(u"feed_speed_l")
        self.feed_speed_l.setFont(font)
        self.feed_speed_l.setAlignment(Qt.AlignCenter)
        self.feed_speed_l.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.feed_speed_l)

        self.label_28 = QLabel(self.frame_19)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_28.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_28)

        self.feed_per_tooth_l = QLabel(self.frame_19)
        self.feed_per_tooth_l.setObjectName(u"feed_per_tooth_l")
        self.feed_per_tooth_l.setFont(font)
        self.feed_per_tooth_l.setAlignment(Qt.AlignCenter)
        self.feed_per_tooth_l.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.feed_per_tooth_l)

        self.label_30 = QLabel(self.frame_19)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_30.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_30)

        self.cutting_speed_l = QLabel(self.frame_19)
        self.cutting_speed_l.setObjectName(u"cutting_speed_l")
        self.cutting_speed_l.setFont(font)
        self.cutting_speed_l.setAlignment(Qt.AlignCenter)
        self.cutting_speed_l.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.cutting_speed_l)

        self.horizontalLayout_4.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.groupBox_21)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_20)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_32 = QLabel(self.frame_20)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_32.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_32)

        self.cutting_width_l = QLabel(self.frame_20)
        self.cutting_width_l.setObjectName(u"cutting_width_l")
        self.cutting_width_l.setFont(font)
        self.cutting_width_l.setAlignment(Qt.AlignCenter)
        self.cutting_width_l.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.cutting_width_l)

        self.label_36 = QLabel(self.frame_20)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_36.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_36)

        self.cutting_depth_l = QLabel(self.frame_20)
        self.cutting_depth_l.setObjectName(u"cutting_depth_l")
        self.cutting_depth_l.setFont(font)
        self.cutting_depth_l.setAlignment(Qt.AlignCenter)
        self.cutting_depth_l.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.cutting_depth_l)

        self.label_34 = QLabel(self.frame_20)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_34.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_34)

        self.shear_angle_l = QLabel(self.frame_20)
        self.shear_angle_l.setObjectName(u"shear_angle_l")
        self.shear_angle_l.setFont(font)
        self.shear_angle_l.setAlignment(Qt.AlignCenter)
        self.shear_angle_l.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.shear_angle_l)

        self.label_38 = QLabel(self.frame_20)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_38.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_38)

        self.mean_chip_thickness_l = QLabel(self.frame_20)
        self.mean_chip_thickness_l.setObjectName(u"mean_chip_thickness_l")
        self.mean_chip_thickness_l.setFont(font)
        self.mean_chip_thickness_l.setAlignment(Qt.AlignCenter)
        self.mean_chip_thickness_l.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.mean_chip_thickness_l)

        self.label_40 = QLabel(self.frame_20)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_40.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_40)

        self.mean_chip_length_l = QLabel(self.frame_20)
        self.mean_chip_length_l.setObjectName(u"mean_chip_length_l")
        self.mean_chip_length_l.setFont(font)
        self.mean_chip_length_l.setAlignment(Qt.AlignCenter)
        self.mean_chip_length_l.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.mean_chip_length_l)

        self.horizontalLayout_4.addWidget(self.frame_20)

        self.horizontalLayout_3.addWidget(self.groupBox_21)

        self.groupBox_2 = QGroupBox(self.groupBox_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.groupBox_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_42 = QLabel(self.frame_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_42.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_42)

        self.tool_id_l = QLabel(self.frame_4)
        self.tool_id_l.setObjectName(u"tool_id_l")
        self.tool_id_l.setFont(font)
        self.tool_id_l.setAlignment(Qt.AlignCenter)
        self.tool_id_l.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.tool_id_l)

        self.label_45 = QLabel(self.frame_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_45.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_45)

        self.classification_no_l = QLabel(self.frame_4)
        self.classification_no_l.setObjectName(u"classification_no_l")
        self.classification_no_l.setFont(font)
        self.classification_no_l.setAlignment(Qt.AlignCenter)
        self.classification_no_l.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.classification_no_l)

        self.label_46 = QLabel(self.frame_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_46.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_46)

        self.strategic_business_unit_l = QLabel(self.frame_4)
        self.strategic_business_unit_l.setObjectName(u"strategic_business_unit_l")
        self.strategic_business_unit_l.setFont(font)
        self.strategic_business_unit_l.setAlignment(Qt.AlignCenter)
        self.strategic_business_unit_l.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.strategic_business_unit_l)

        self.label_48 = QLabel(self.frame_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_48.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_48)

        self.tool_diameter_l = QLabel(self.frame_4)
        self.tool_diameter_l.setObjectName(u"tool_diameter_l")
        self.tool_diameter_l.setFont(font)
        self.tool_diameter_l.setAlignment(Qt.AlignCenter)
        self.tool_diameter_l.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.tool_diameter_l)

        self.label_49 = QLabel(self.frame_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_49.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_49)

        self.tool_cutting_width_l = QLabel(self.frame_4)
        self.tool_cutting_width_l.setObjectName(u"tool_cutting_width_l")
        self.tool_cutting_width_l.setFont(font)
        self.tool_cutting_width_l.setAlignment(Qt.AlignCenter)
        self.tool_cutting_width_l.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.tool_cutting_width_l)

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_18 = QFrame(self.groupBox_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_18)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_52 = QLabel(self.frame_18)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_52.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_52)

        self.no_of_wings_l = QLabel(self.frame_18)
        self.no_of_wings_l.setObjectName(u"no_of_wings_l")
        self.no_of_wings_l.setFont(font)
        self.no_of_wings_l.setAlignment(Qt.AlignCenter)
        self.no_of_wings_l.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.no_of_wings_l)

        self.label_54 = QLabel(self.frame_18)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_54.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_54)

        self.total_no_of_wings_l = QLabel(self.frame_18)
        self.total_no_of_wings_l.setObjectName(u"total_no_of_wings_l")
        self.total_no_of_wings_l.setFont(font)
        self.total_no_of_wings_l.setAlignment(Qt.AlignCenter)
        self.total_no_of_wings_l.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.total_no_of_wings_l)

        self.label_56 = QLabel(self.frame_18)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_56.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_56)

        self.cutting_material_l = QLabel(self.frame_18)
        self.cutting_material_l.setObjectName(u"cutting_material_l")
        self.cutting_material_l.setFont(font)
        self.cutting_material_l.setAlignment(Qt.AlignCenter)
        self.cutting_material_l.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.cutting_material_l)

        self.label_58 = QLabel(self.frame_18)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_58.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_58)

        self.cutting_material_quality_l = QLabel(self.frame_18)
        self.cutting_material_quality_l.setObjectName(u"cutting_material_quality_l")
        self.cutting_material_quality_l.setFont(font)
        self.cutting_material_quality_l.setAlignment(Qt.AlignCenter)
        self.cutting_material_quality_l.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.cutting_material_quality_l)

        self.label_60 = QLabel(self.frame_18)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_60.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.label_60)

        self.body_material_l = QLabel(self.frame_18)
        self.body_material_l.setObjectName(u"body_material_l")
        self.body_material_l.setFont(font)
        self.body_material_l.setAlignment(Qt.AlignCenter)
        self.body_material_l.setWordWrap(True)

        self.verticalLayout_19.addWidget(self.body_material_l)

        self.horizontalLayout_5.addWidget(self.frame_18)

        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_62 = QLabel(self.frame_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_62.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_62)

        self.n_max_l = QLabel(self.frame_2)
        self.n_max_l.setObjectName(u"n_max_l")
        self.n_max_l.setFont(font)
        self.n_max_l.setAlignment(Qt.AlignCenter)
        self.n_max_l.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.n_max_l)

        self.label_64 = QLabel(self.frame_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_64.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_64)

        self.n_opt_l = QLabel(self.frame_2)
        self.n_opt_l.setObjectName(u"n_opt_l")
        self.n_opt_l.setFont(font)
        self.n_opt_l.setAlignment(Qt.AlignCenter)
        self.n_opt_l.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.n_opt_l)

        self.label_66 = QLabel(self.frame_2)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_66.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_66)

        self.rake_angle_l = QLabel(self.frame_2)
        self.rake_angle_l.setObjectName(u"rake_angle_l")
        self.rake_angle_l.setFont(font)
        self.rake_angle_l.setAlignment(Qt.AlignCenter)
        self.rake_angle_l.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.rake_angle_l)

        self.label_31 = QLabel(self.frame_2)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_21.addWidget(self.label_31)

        self.bore_diameter_l = QLabel(self.frame_2)
        self.bore_diameter_l.setObjectName(u"bore_diameter_l")
        self.bore_diameter_l.setFont(font)
        self.bore_diameter_l.setAlignment(Qt.AlignCenter)
        self.bore_diameter_l.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.bore_diameter_l)

        self.label_35 = QLabel(self.frame_2)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_21.addWidget(self.label_35)

        self.label_37 = QLabel(self.frame_2)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_21.addWidget(self.label_37)

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.horizontalLayout.addWidget(self.groupBox_4)

        self.verticalLayout.addWidget(self.frame)

        self.choice_groupbox = QGroupBox(self.centralwidget)
        self.choice_groupbox.setObjectName(u"choice_groupbox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.choice_groupbox.sizePolicy().hasHeightForWidth()
        )
        self.choice_groupbox.setSizePolicy(sizePolicy)
        self.choice_groupbox.setMinimumSize(QSize(0, 300))
        self.choice_groupbox.setMaximumSize(QSize(16777215, 300))
        self.choice_groupbox.setStyleSheet(
            u"QGroupBox {\n"
            "background-color: rgb(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QFrame {\n"
            "background-color: rgb(255, 255, 255, 0);\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "background-color: rgb(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 9pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QPushButton {\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 101, 190, 255), stop:1 rgba(81, 48, 154, 50));\n"
            "border-radius: 10px;\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "color: rgb(255, 255, 255, 0);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "background-color: rgb(0, 255, 213, 0.5);\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton:pressed {\n"
            "background-color: rgb(0, 255, 213);\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "}"
        )
        self.horizontalLayout_2 = QHBoxLayout(self.choice_groupbox)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.choice_groupbox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.material_l2 = QLabel(self.frame_5)
        self.material_l2.setObjectName(u"material_l2")
        self.material_l2.setStyleSheet(u"")
        self.material_l2.setAlignment(Qt.AlignCenter)
        self.material_l2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.material_l2, 0, Qt.AlignHCenter)

        self.cutting_direction_l2 = QLabel(self.frame_5)
        self.cutting_direction_l2.setObjectName(u"cutting_direction_l2")
        self.cutting_direction_l2.setStyleSheet(u"")
        self.cutting_direction_l2.setAlignment(Qt.AlignCenter)
        self.cutting_direction_l2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.cutting_direction_l2, 0, Qt.AlignHCenter)

        self.cutting_material_l2 = QLabel(self.frame_5)
        self.cutting_material_l2.setObjectName(u"cutting_material_l2")
        self.cutting_material_l2.setStyleSheet(u"")
        self.cutting_material_l2.setAlignment(Qt.AlignCenter)
        self.cutting_material_l2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.cutting_material_l2, 0, Qt.AlignHCenter)

        self.body_material_l2 = QLabel(self.frame_5)
        self.body_material_l2.setObjectName(u"body_material_l2")
        self.body_material_l2.setAlignment(Qt.AlignCenter)
        self.body_material_l2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.body_material_l2, 0, Qt.AlignHCenter)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.choice_groupbox)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rotational_speed_l2 = QLabel(self.frame_6)
        self.rotational_speed_l2.setObjectName(u"rotational_speed_l2")
        self.rotational_speed_l2.setLayoutDirection(Qt.LeftToRight)
        self.rotational_speed_l2.setAlignment(Qt.AlignCenter)
        self.rotational_speed_l2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.rotational_speed_l2, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(
            self.pushButton_3.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_3.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(
            self.pushButton_4.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_4.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.horizontalLayout_2.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.choice_groupbox)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.feed_speed_l2 = QLabel(self.frame_7)
        self.feed_speed_l2.setObjectName(u"feed_speed_l2")
        self.feed_speed_l2.setAlignment(Qt.AlignCenter)
        self.feed_speed_l2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.feed_speed_l2)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(
            self.pushButton_5.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_5.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(
            self.pushButton_6.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_6.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(
            self.pushButton_7.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_7.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_7)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2.setHeightForWidth(
            self.pushButton_8.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_8.setSizePolicy(sizePolicy2)

        self.verticalLayout_4.addWidget(self.pushButton_8)

        self.horizontalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.choice_groupbox)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.feed_per_tooth_l2 = QLabel(self.frame_8)
        self.feed_per_tooth_l2.setObjectName(u"feed_per_tooth_l2")
        self.feed_per_tooth_l2.setAlignment(Qt.AlignCenter)
        self.feed_per_tooth_l2.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.feed_per_tooth_l2, 0, Qt.AlignHCenter)

        self.pushButton_9 = QPushButton(self.frame_8)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy2.setHeightForWidth(
            self.pushButton_9.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_9.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_8)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy2.setHeightForWidth(
            self.pushButton_10.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_10.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy2.setHeightForWidth(
            self.pushButton_11.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_11.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_8)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy2.setHeightForWidth(
            self.pushButton_12.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_12.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.pushButton_12)

        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.choice_groupbox)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.cutting_speed_l2 = QLabel(self.frame_9)
        self.cutting_speed_l2.setObjectName(u"cutting_speed_l2")
        self.cutting_speed_l2.setAlignment(Qt.AlignCenter)
        self.cutting_speed_l2.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.cutting_speed_l2)

        self.pushButton_13 = QPushButton(self.frame_9)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy2.setHeightForWidth(
            self.pushButton_13.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_13.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_9)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy2.setHeightForWidth(
            self.pushButton_14.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_14.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.frame_9)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy2.setHeightForWidth(
            self.pushButton_15.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_15.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.frame_9)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy2.setHeightForWidth(
            self.pushButton_16.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_16.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.pushButton_16)

        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.choice_groupbox)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.cutting_width_l2 = QLabel(self.frame_10)
        self.cutting_width_l2.setObjectName(u"cutting_width_l2")
        self.cutting_width_l2.setAlignment(Qt.AlignCenter)
        self.cutting_width_l2.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.cutting_width_l2)

        self.pushButton_17 = QPushButton(self.frame_10)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy2.setHeightForWidth(
            self.pushButton_17.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_17.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_10)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy2.setHeightForWidth(
            self.pushButton_18.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_18.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.frame_10)
        self.pushButton_19.setObjectName(u"pushButton_19")
        sizePolicy2.setHeightForWidth(
            self.pushButton_19.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_19.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.frame_10)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy2.setHeightForWidth(
            self.pushButton_20.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_20.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.pushButton_20)

        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.choice_groupbox)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cutting_depth_l2 = QLabel(self.frame_11)
        self.cutting_depth_l2.setObjectName(u"cutting_depth_l2")
        self.cutting_depth_l2.setAlignment(Qt.AlignCenter)
        self.cutting_depth_l2.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.cutting_depth_l2)

        self.pushButton_21 = QPushButton(self.frame_11)
        self.pushButton_21.setObjectName(u"pushButton_21")
        sizePolicy2.setHeightForWidth(
            self.pushButton_21.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_21.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_11)
        self.pushButton_22.setObjectName(u"pushButton_22")
        sizePolicy2.setHeightForWidth(
            self.pushButton_22.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_22.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.frame_11)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy2.setHeightForWidth(
            self.pushButton_23.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_23.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.frame_11)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy2.setHeightForWidth(
            self.pushButton_24.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_24.setSizePolicy(sizePolicy2)

        self.verticalLayout_8.addWidget(self.pushButton_24)

        self.horizontalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.choice_groupbox)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.shear_angle_l2 = QLabel(self.frame_12)
        self.shear_angle_l2.setObjectName(u"shear_angle_l2")
        self.shear_angle_l2.setAlignment(Qt.AlignCenter)
        self.shear_angle_l2.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.shear_angle_l2)

        self.pushButton_25 = QPushButton(self.frame_12)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy2.setHeightForWidth(
            self.pushButton_25.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_25.setSizePolicy(sizePolicy2)

        self.verticalLayout_9.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.frame_12)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy2.setHeightForWidth(
            self.pushButton_26.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_26.setSizePolicy(sizePolicy2)

        self.verticalLayout_9.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.frame_12)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy2.setHeightForWidth(
            self.pushButton_27.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_27.setSizePolicy(sizePolicy2)

        self.verticalLayout_9.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.frame_12)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy2.setHeightForWidth(
            self.pushButton_28.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_28.setSizePolicy(sizePolicy2)

        self.verticalLayout_9.addWidget(self.pushButton_28)

        self.horizontalLayout_2.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.choice_groupbox)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tool_diameter_l2 = QLabel(self.frame_13)
        self.tool_diameter_l2.setObjectName(u"tool_diameter_l2")
        self.tool_diameter_l2.setAlignment(Qt.AlignCenter)
        self.tool_diameter_l2.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.tool_diameter_l2)

        self.pushButton_29 = QPushButton(self.frame_13)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy2.setHeightForWidth(
            self.pushButton_29.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_29.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.frame_13)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy2.setHeightForWidth(
            self.pushButton_30.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_30.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.pushButton_30)

        self.pushButton_31 = QPushButton(self.frame_13)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy2.setHeightForWidth(
            self.pushButton_31.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_31.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.pushButton_31)

        self.pushButton_32 = QPushButton(self.frame_13)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy2.setHeightForWidth(
            self.pushButton_32.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_32.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.pushButton_32)

        self.horizontalLayout_2.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.choice_groupbox)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tool_cutting_width_l2 = QLabel(self.frame_14)
        self.tool_cutting_width_l2.setObjectName(u"tool_cutting_width_l2")
        self.tool_cutting_width_l2.setAlignment(Qt.AlignCenter)
        self.tool_cutting_width_l2.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.tool_cutting_width_l2)

        self.pushButton_33 = QPushButton(self.frame_14)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy2.setHeightForWidth(
            self.pushButton_33.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_33.setSizePolicy(sizePolicy2)

        self.verticalLayout_11.addWidget(self.pushButton_33)

        self.pushButton_34 = QPushButton(self.frame_14)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy2.setHeightForWidth(
            self.pushButton_34.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_34.setSizePolicy(sizePolicy2)

        self.verticalLayout_11.addWidget(self.pushButton_34)

        self.pushButton_35 = QPushButton(self.frame_14)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy2.setHeightForWidth(
            self.pushButton_35.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_35.setSizePolicy(sizePolicy2)

        self.verticalLayout_11.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.frame_14)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy2.setHeightForWidth(
            self.pushButton_36.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_36.setSizePolicy(sizePolicy2)

        self.verticalLayout_11.addWidget(self.pushButton_36)

        self.horizontalLayout_2.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.choice_groupbox)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy1.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy1)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.no_of_wings_l2 = QLabel(self.frame_15)
        self.no_of_wings_l2.setObjectName(u"no_of_wings_l2")
        self.no_of_wings_l2.setAlignment(Qt.AlignCenter)
        self.no_of_wings_l2.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.no_of_wings_l2)

        self.pushButton_37 = QPushButton(self.frame_15)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy2.setHeightForWidth(
            self.pushButton_37.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_37.setSizePolicy(sizePolicy2)

        self.verticalLayout_12.addWidget(self.pushButton_37)

        self.pushButton_38 = QPushButton(self.frame_15)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy2.setHeightForWidth(
            self.pushButton_38.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_38.setSizePolicy(sizePolicy2)

        self.verticalLayout_12.addWidget(self.pushButton_38)

        self.pushButton_39 = QPushButton(self.frame_15)
        self.pushButton_39.setObjectName(u"pushButton_39")
        sizePolicy2.setHeightForWidth(
            self.pushButton_39.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_39.setSizePolicy(sizePolicy2)

        self.verticalLayout_12.addWidget(self.pushButton_39)

        self.pushButton_40 = QPushButton(self.frame_15)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy2.setHeightForWidth(
            self.pushButton_40.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_40.setSizePolicy(sizePolicy2)

        self.verticalLayout_12.addWidget(self.pushButton_40)

        self.horizontalLayout_2.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.choice_groupbox)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.total_no_of_wings_l2 = QLabel(self.frame_16)
        self.total_no_of_wings_l2.setObjectName(u"total_no_of_wings_l2")
        self.total_no_of_wings_l2.setAlignment(Qt.AlignCenter)
        self.total_no_of_wings_l2.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.total_no_of_wings_l2)

        self.pushButton_41 = QPushButton(self.frame_16)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy2.setHeightForWidth(
            self.pushButton_41.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_41.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.pushButton_41)

        self.pushButton_42 = QPushButton(self.frame_16)
        self.pushButton_42.setObjectName(u"pushButton_42")
        sizePolicy2.setHeightForWidth(
            self.pushButton_42.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_42.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.pushButton_42)

        self.pushButton_43 = QPushButton(self.frame_16)
        self.pushButton_43.setObjectName(u"pushButton_43")
        sizePolicy2.setHeightForWidth(
            self.pushButton_43.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_43.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.pushButton_43)

        self.pushButton_44 = QPushButton(self.frame_16)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy2.setHeightForWidth(
            self.pushButton_44.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_44.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.pushButton_44)

        self.horizontalLayout_2.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.choice_groupbox)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy1.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy1)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_17)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.rake_angle_l2 = QLabel(self.frame_17)
        self.rake_angle_l2.setObjectName(u"rake_angle_l2")
        self.rake_angle_l2.setAlignment(Qt.AlignCenter)
        self.rake_angle_l2.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.rake_angle_l2)

        self.pushButton_45 = QPushButton(self.frame_17)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy2.setHeightForWidth(
            self.pushButton_45.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_45.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.pushButton_45)

        self.pushButton_46 = QPushButton(self.frame_17)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy2.setHeightForWidth(
            self.pushButton_46.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_46.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.pushButton_46)

        self.pushButton_47 = QPushButton(self.frame_17)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy2.setHeightForWidth(
            self.pushButton_47.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_47.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.pushButton_47)

        self.pushButton_48 = QPushButton(self.frame_17)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy2.setHeightForWidth(
            self.pushButton_48.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_48.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.pushButton_48)

        self.horizontalLayout_2.addWidget(self.frame_17)

        self.frame_22 = QFrame(self.choice_groupbox)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_22)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.bore_diameter_l2 = QLabel(self.frame_22)
        self.bore_diameter_l2.setObjectName(u"bore_diameter_l2")
        self.bore_diameter_l2.setAlignment(Qt.AlignCenter)
        self.bore_diameter_l2.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.bore_diameter_l2)

        self.pushButton_49 = QPushButton(self.frame_22)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy2.setHeightForWidth(
            self.pushButton_49.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_49.setSizePolicy(sizePolicy2)

        self.verticalLayout_23.addWidget(self.pushButton_49)

        self.pushButton_50 = QPushButton(self.frame_22)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy2.setHeightForWidth(
            self.pushButton_50.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_50.setSizePolicy(sizePolicy2)

        self.verticalLayout_23.addWidget(self.pushButton_50)

        self.pushButton_51 = QPushButton(self.frame_22)
        self.pushButton_51.setObjectName(u"pushButton_51")
        sizePolicy2.setHeightForWidth(
            self.pushButton_51.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_51.setSizePolicy(sizePolicy2)

        self.verticalLayout_23.addWidget(self.pushButton_51)

        self.pushButton_52 = QPushButton(self.frame_22)
        self.pushButton_52.setObjectName(u"pushButton_48")
        sizePolicy2.setHeightForWidth(
            self.pushButton_52.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_52.setSizePolicy(sizePolicy2)

        self.verticalLayout_23.addWidget(self.pushButton_52)

        self.horizontalLayout_2.addWidget(self.frame_22)

        self.verticalLayout.addWidget(self.choice_groupbox)

        self.btn_close = QPushButton(self.centralwidget)
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

        self.verticalLayout.addWidget(self.btn_close)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"MainWindow", None)
        )
        self.groupBox_4.setTitle(
            QCoreApplication.translate("MainWindow", u"Angewandte Parameter", None)
        )
        self.groupBox_18.setTitle(
            QCoreApplication.translate("MainWindow", u"Werkstoff", None)
        )
        self.label_18.setText(
            QCoreApplication.translate("MainWindow", u"Werkstoff", None)
        )
        self.material_l.setText("")
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", u"Feuchtigkeit [%]", None)
        )
        self.moisture_content_l.setText("")
        self.label_19.setText("")
        self.label_21.setText("")
        self.label_27.setText("")
        self.label_23.setText("")
        self.label_25.setText("")
        self.label_29.setText("")
        self.groupBox_21.setTitle(
            QCoreApplication.translate("MainWindow", u"Prozess", None)
        )
        self.label_22.setText(
            QCoreApplication.translate("MainWindow", u"Schnittrichtung", None)
        )
        self.cutting_direction_l.setText("")
        self.label_26.setText(
            QCoreApplication.translate("MainWindow", u"Drehzahl [U/min]", None)
        )
        self.rotational_speed_l.setText("")
        self.label_24.setText(
            QCoreApplication.translate(
                "MainWindow", u"Vorschubgeschwindigkeit [m/min]", None
            )
        )
        self.feed_speed_l.setText("")
        self.label_28.setText(
            QCoreApplication.translate("MainWindow", u"Zahnvorschub\u00a0[mm]", None)
        )
        self.feed_per_tooth_l.setText("")
        self.label_30.setText(
            QCoreApplication.translate(
                "MainWindow", u"Schnittgeschwindigkeit [m/s]", None
            )
        )
        self.cutting_speed_l.setText("")
        self.label_32.setText(
            QCoreApplication.translate("MainWindow", u"SB - Werkstück [mm]", None)
        )
        self.cutting_width_l.setText("")
        self.label_36.setText(
            QCoreApplication.translate("MainWindow", u"Schnitttiefe [mm]", None)
        )
        self.cutting_depth_l.setText("")
        self.label_34.setText(
            QCoreApplication.translate("MainWindow", u"Achswinkel λ [\u00b0]", None)
        )
        self.shear_angle_l.setText("")
        self.label_38.setText(
            QCoreApplication.translate("MainWindow", u"Mittlere Spandicke [mm]", None)
        )
        self.mean_chip_thickness_l.setText("")
        self.label_40.setText(
            QCoreApplication.translate(
                "MainWindow", u"Mittlere Spanl\u00e4nge [mm]", None
            )
        )
        self.mean_chip_length_l.setText("")
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", u"Werkzeug", None)
        )
        self.label_42.setText(
            QCoreApplication.translate("MainWindow", u"ID-Nummer", None)
        )
        self.tool_id_l.setText("")
        self.label_45.setText(
            QCoreApplication.translate("MainWindow", u"Klassifizierungsnummer", None)
        )
        self.classification_no_l.setText("")
        self.label_46.setText(
            QCoreApplication.translate(
                "MainWindow", u"Strategische Geschäftszahl", None
            )
        )
        self.strategic_business_unit_l.setText("")
        self.label_48.setText(
            QCoreApplication.translate("MainWindow", u"Werkzeugdurchmesser [mm]", None)
        )
        self.tool_diameter_l.setText("")
        self.label_49.setText(
            QCoreApplication.translate("MainWindow", u"Schneidenbreite [mm]", None)
        )
        self.tool_cutting_width_l.setText("")
        self.label_52.setText(
            QCoreApplication.translate("MainWindow", u"Schneidenzahl", None)
        )
        self.no_of_wings_l.setText("")
        self.label_54.setText(
            QCoreApplication.translate("MainWindow", u"Gesamtschneidenanzahl", None)
        )
        self.total_no_of_wings_l.setText("")
        self.label_56.setText(
            QCoreApplication.translate("MainWindow", u"Schneidenwerkstoff", None)
        )
        self.cutting_material_l.setText("")
        self.label_58.setText(
            QCoreApplication.translate("MainWindow", u"PCD Qualit\u00e4t", None)
        )
        self.cutting_material_quality_l.setText("")
        self.label_60.setText(
            QCoreApplication.translate("MainWindow", u"Grundk\u00f6rpermaterial", None)
        )
        self.body_material_l.setText("")
        self.label_62.setText(
            QCoreApplication.translate("MainWindow", u"Max. Drehzahl [U/min]", None)
        )
        self.n_max_l.setText("")
        self.label_64.setText(
            QCoreApplication.translate("MainWindow", u"Optimale Drehzahl [U/min]", None)
        )
        self.n_opt_l.setText("")
        self.label_66.setText(
            QCoreApplication.translate("MainWindow", u"Spanwinkel γ [\u00b0]", None)
        )
        self.rake_angle_l.setText("")
        self.label_31.setText("Bohrungsdurchmesser [mm]")
        self.bore_diameter_l.setText("")
        self.label_35.setText("")
        self.label_37.setText("")
        self.choice_groupbox.setTitle(
            QCoreApplication.translate("MainWindow", u"Parameterauswahl", None)
        )
        self.label.setText("")
        self.material_l2.setText(
            QCoreApplication.translate("MainWindow", u"Werkstoff", None)
        )
        self.cutting_direction_l2.setText(
            QCoreApplication.translate("MainWindow", u"Schnittrichtung", None)
        )
        self.cutting_material_l2.setText(
            QCoreApplication.translate("MainWindow", u"Schneidenwerkstoff", None)
        )
        self.body_material_l2.setText(
            QCoreApplication.translate("MainWindow", u"Grundk\u00f6rpermaterial", None)
        )
        self.rotational_speed_l2.setText(
            QCoreApplication.translate("MainWindow", u"Drehzahl", None)
        )
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"0_0", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"1_0", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate("MainWindow", u"2_0", None)
        )
        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", u"3_0", None)
        )
        self.feed_speed_l2.setText(
            QCoreApplication.translate("MainWindow", u"Vorschub-geschwindigkeit", None)
        )
        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", u"0_1", None)
        )
        self.pushButton_6.setText(
            QCoreApplication.translate("MainWindow", u"1_1", None)
        )
        self.pushButton_7.setText(
            QCoreApplication.translate("MainWindow", u"2_1", None)
        )
        self.pushButton_8.setText(
            QCoreApplication.translate("MainWindow", u"3_1", None)
        )
        self.feed_per_tooth_l2.setText(
            QCoreApplication.translate("MainWindow", u"Zahnvorschub", None)
        )
        self.pushButton_9.setText(
            QCoreApplication.translate("MainWindow", u"0_2", None)
        )
        self.pushButton_10.setText(
            QCoreApplication.translate("MainWindow", u"1_2", None)
        )
        self.pushButton_11.setText(
            QCoreApplication.translate("MainWindow", u"2_2", None)
        )
        self.pushButton_12.setText(
            QCoreApplication.translate("MainWindow", u"3_2", None)
        )
        self.cutting_speed_l2.setText(
            QCoreApplication.translate("MainWindow", u"Schnitt-geschwindigkeit", None)
        )
        self.pushButton_13.setText(
            QCoreApplication.translate("MainWindow", u"0_3", None)
        )
        self.pushButton_14.setText(
            QCoreApplication.translate("MainWindow", u"1_3", None)
        )
        self.pushButton_15.setText(
            QCoreApplication.translate("MainWindow", u"2_3", None)
        )
        self.pushButton_16.setText(
            QCoreApplication.translate("MainWindow", u"3_3", None)
        )
        self.cutting_width_l2.setText(
            QCoreApplication.translate("MainWindow", u"SB - Werkstück", None)
        )
        self.pushButton_17.setText(
            QCoreApplication.translate("MainWindow", u"0_4", None)
        )
        self.pushButton_18.setText(
            QCoreApplication.translate("MainWindow", u"1_4", None)
        )
        self.pushButton_19.setText(
            QCoreApplication.translate("MainWindow", u"2_4", None)
        )
        self.pushButton_20.setText(
            QCoreApplication.translate("MainWindow", u"3_4", None)
        )
        self.cutting_depth_l2.setText(
            QCoreApplication.translate("MainWindow", u"Schnitttiefe", None)
        )
        self.pushButton_21.setText(
            QCoreApplication.translate("MainWindow", u"0_5", None)
        )
        self.pushButton_22.setText(
            QCoreApplication.translate("MainWindow", u"1_5", None)
        )
        self.pushButton_23.setText(
            QCoreApplication.translate("MainWindow", u"2_5", None)
        )
        self.pushButton_24.setText(
            QCoreApplication.translate("MainWindow", u"3_5", None)
        )
        self.shear_angle_l2.setText(
            QCoreApplication.translate("MainWindow", u"Achswinkel λ", None)
        )
        self.pushButton_25.setText(
            QCoreApplication.translate("MainWindow", u"0_6", None)
        )
        self.pushButton_26.setText(
            QCoreApplication.translate("MainWindow", u"1_6", None)
        )
        self.pushButton_27.setText(
            QCoreApplication.translate("MainWindow", u"2_6", None)
        )
        self.pushButton_28.setText(
            QCoreApplication.translate("MainWindow", u"3_6", None)
        )
        self.tool_diameter_l2.setText(
            QCoreApplication.translate("MainWindow", u"Werkzeug-durchmesser", None)
        )
        self.pushButton_29.setText(
            QCoreApplication.translate("MainWindow", u"0_7", None)
        )
        self.pushButton_30.setText(
            QCoreApplication.translate("MainWindow", u"1_7", None)
        )
        self.pushButton_31.setText(
            QCoreApplication.translate("MainWindow", u"2_7", None)
        )
        self.pushButton_32.setText(
            QCoreApplication.translate("MainWindow", u"3_7", None)
        )
        self.tool_cutting_width_l2.setText(
            QCoreApplication.translate("MainWindow", u"Schneidenbreite", None)
        )
        self.pushButton_33.setText(
            QCoreApplication.translate("MainWindow", u"0_8", None)
        )
        self.pushButton_34.setText(
            QCoreApplication.translate("MainWindow", u"1_8", None)
        )
        self.pushButton_35.setText(
            QCoreApplication.translate("MainWindow", u"2_8", None)
        )
        self.pushButton_36.setText(
            QCoreApplication.translate("MainWindow", u"3_8", None)
        )
        self.no_of_wings_l2.setText(
            QCoreApplication.translate("MainWindow", u"Schneidenzahl", None)
        )
        self.pushButton_37.setText(
            QCoreApplication.translate("MainWindow", u"0_9", None)
        )
        self.pushButton_38.setText(
            QCoreApplication.translate("MainWindow", u"1_9", None)
        )
        self.pushButton_39.setText(
            QCoreApplication.translate("MainWindow", u"2_9", None)
        )
        self.pushButton_40.setText(
            QCoreApplication.translate("MainWindow", u"3_9", None)
        )
        self.total_no_of_wings_l2.setText(
            QCoreApplication.translate("MainWindow", u"Gesamt-schneidenanzahl", None)
        )
        self.pushButton_41.setText(
            QCoreApplication.translate("MainWindow", u"0_10", None)
        )
        self.pushButton_42.setText(
            QCoreApplication.translate("MainWindow", u"1_10", None)
        )
        self.pushButton_43.setText(
            QCoreApplication.translate("MainWindow", u"2_10", None)
        )
        self.pushButton_44.setText(
            QCoreApplication.translate("MainWindow", u"3_10", None)
        )
        self.rake_angle_l2.setText(
            QCoreApplication.translate("MainWindow", u"Spanwinkel", None)
        )
        self.pushButton_45.setText(
            QCoreApplication.translate("MainWindow", u"0_11", None)
        )
        self.pushButton_46.setText(
            QCoreApplication.translate("MainWindow", u"1_11", None)
        )
        self.pushButton_47.setText(
            QCoreApplication.translate("MainWindow", u"2_11", None)
        )
        self.pushButton_48.setText(
            QCoreApplication.translate("MainWindow", u"3_11", None)
        )

        self.bore_diameter_l2.setText(
            QCoreApplication.translate("MainWindow", u"Bohrungs-durchmesser", None)
        )
        self.pushButton_49.setText(
            QCoreApplication.translate("MainWindow", u"0_12", None)
        )
        self.pushButton_50.setText(
            QCoreApplication.translate("MainWindow", u"1_12", None)
        )
        self.pushButton_51.setText(
            QCoreApplication.translate("MainWindow", u"2_12", None)
        )
        self.pushButton_52.setText(
            QCoreApplication.translate("MainWindow", u"3_12", None)
        )

        self.btn_close.setText(
            QCoreApplication.translate("MainWindow", u"Schlie\u00dfen", None)
        )

    # retranslateUi
