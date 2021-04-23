# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from src.ui.ui_visualization import Ui_Visualization

from src.database.read import Read
from src.helpers.calculate_parameters import (
    get_cutting_speed,
    get_feed_per_tooth,
    get_mean_chip_thickness,
    get_mean_chip_length,
)
from src.settings import *
from src.helpers.helpers import get_labels
import ctypes
import json
import numpy as np
import os
import pyqtgraph as pg


class MultivariateVisualizationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Visualization()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_initial_view()
        self.setup_headers()
        self.setup_indices()
        self.setup_callbacks()
        self.setup_labels_from_metadata()
        self.showMaximized()

        # Database init
        self.db = Read(os.path.join("pkgs/src/database", DB_NAME))

    def setup_ui(self):
        self.setWindowIcon(QtGui.QIcon("pkgs/src/ui/icons/lighting.svg"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Power Analytics | Datenvisualisierung", None
            )
        )

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.graphics_view.setBackground("w")

    def setup_headers(self):
        self.headers = {
            0: "rotational_speed",
            1: "feed_speed",
            2: "feed_per_tooth",
            3: "cutting_speed",
            4: "cutting_width",
            5: "cutting_depth",
            6: "cutting_angle",
            7: "tool_diameter",
            8: "tool_cutting_width",
            9: "no_of_wings",
            10: "total_no_of_wings",
            11: "rake_angle",
        }

    def setup_indices(self):
        self.indices = {
            0: "material",
            1: "cutting_direction",
            2: "cutting_material",
            3: "body_material",
        }

    def setup_callbacks(self):
        # QGroupBox -> QFrame -> QPushButton
        # "groupBox_2" is the one I have to use
        for widget_1 in self.ui.groupBox_2.children():
            if isinstance(widget_1, QFrame):
                for widget_2 in widget_1.children():
                    if isinstance(widget_2, QPushButton):
                        button_text = widget_2.text()
                        row_id = int(button_text.split("_")[0])
                        column_id = int(button_text.split("_")[1])

                        # Get corresponding variables
                        categorical_var = self.indices[row_id]
                        numerical_var = self.headers[column_id]

                        # Explained here:
                        # https://stackoverflow.com/questions/4578861/connecting-slots-and-signals-in-pyqt4-in-a-loop
                        helper = lambda cat, num: (
                            lambda: self.plot_chosen_combination(cat, num)
                        )
                        widget_2.clicked.connect(helper(categorical_var, numerical_var))

        # Close button
        self.ui.btn_close.clicked.connect(lambda: self.close())

    def setup_labels_from_metadata(self):
        try:
            with open("pkgs/src/metadata.json") as json_file:
                self.metadata = json.load(json_file)
        except:
            self.metadata = None

        try:
            for key, value in self.metadata.items():
                # QGroupBox -> QFrame -> QLabel
                # "groupBox_4" is the one I have to use
                for widget_1 in self.ui.groupBox_4.children():
                    if isinstance(widget_1, QGroupBox):
                        for widget_2 in widget_1.children():
                            if isinstance(widget_2, QFrame):
                                for widget_3 in widget_2.children():
                                    if isinstance(widget_3, QLabel):
                                        if key + "_l" == widget_3.objectName():
                                            widget_3.setText(value)
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Datenvisualisierung konnte nicht gestartet werden ({e})",
                "Power Analytics | Datenvisualisierung",
                0,
            )

    def update_metadata(self, key, value):
        for old_key, _ in self.metadata.items():
            if old_key == key:
                self.metadata[key] = value

    def get_query(self):
        # Set parameters that need to be calculated separately
        self.metadata["cutting_speed"] = get_cutting_speed(
            float(self.metadata["tool_diameter"]),
            float(self.metadata["rotational_speed"]),
        )

        self.metadata["feed_per_tooth"] = get_feed_per_tooth(
            float(self.metadata["feed_speed"]),
            float(self.metadata["rotational_speed"]),
            int(self.metadata["no_of_wings"]),
        )

        self.metadata["mean_chip_thickness"] = get_mean_chip_thickness(
            float(self.metadata["cutting_angle"]),
            float(self.metadata["tool_diameter"]),
            float(self.metadata["cutting_depth"]),
            float(self.metadata["feed_per_tooth"]),
        )

        self.metadata["mean_chip_length"] = get_mean_chip_length(
            float(self.metadata["tool_diameter"]), float(self.metadata["cutting_depth"])
        )

        self.query = f"""
        SELECT mean 
        FROM metadata 
        INNER JOIN stats ON metadata.measurement_id=stats.measurement_id
        WHERE (
            material="{self.metadata["material"]}"
            AND moisture_content={self.metadata["moisture_content"]}
            AND cutting_direction="{self.metadata["cutting_direction"]}"
            AND rotational_speed={self.metadata["rotational_speed"]}
            AND feed_speed={self.metadata["feed_speed"]}
            AND feed_per_tooth={self.metadata["feed_per_tooth"]}
            AND cutting_speed={self.metadata["cutting_speed"]}
            AND cutting_width={self.metadata["cutting_width"]}
            AND cutting_depth={self.metadata["cutting_depth"]}
            AND cutting_angle={self.metadata["cutting_angle"]}
            AND mean_chip_thickness={self.metadata["mean_chip_thickness"]}
            AND mean_chip_length={self.metadata["mean_chip_length"]}
            AND tool_id="{self.metadata["tool_id"]}"
            AND tool_diameter={self.metadata["tool_diameter"]}
            AND tool_cutting_width={self.metadata["tool_cutting_width"]}
            AND no_of_wings={self.metadata["no_of_wings"]}
            AND total_no_of_wings={self.metadata["total_no_of_wings"]}
            AND cutting_material="{self.metadata["cutting_material"]}"
            AND body_material="{self.metadata["body_material"]}"
            AND rake_angle="{self.metadata["rake_angle"]}"
        );
        """

    def plot_chosen_combination(self, categorical_var, numerical_var):
        # Clear the window (if not, it will append to the previous one)
        self.ui.graphics_view.clear()

        win = self.ui.graphics_view.addPlot(row=0, col=0)
        win.addLegend()

        # Setup X- and Y-axis labels
        win.setLabel(
            "left",
            '<span style="color: black; font-size: {}px">Power consumption [W]</span>'.format(
                FONTSIZE
            ),
        )
        win.setLabel(
            "bottom",
            '<span style="color: black; font-size: {}px">{}</span>'.format(
                FONTSIZE, get_labels()[numerical_var]
            ),
        )

        # Scatter labels (do not repeat if already set)
        labels = []

        for i, n_var in enumerate(self.db.get_unique_values(numerical_var)):
            self.update_metadata(numerical_var, n_var)
            for j, c_var in enumerate(self.db.get_unique_values(categorical_var)):
                self.update_metadata(categorical_var, c_var)
                self.get_query()
                y = []
                for result in self.db.cursor.execute(self.query).fetchall():
                    y.append(result[0])

                if c_var not in labels:
                    labels.append(c_var)
                    label = f"{c_var}"
                else:
                    label = None

                win.plot(
                    x=[n_var] * len(y),
                    y=y,
                    symbolPen=COLOURS[j],
                    symbolBrush=COLOURS[j],
                    symbol=SYMBOLS[j],
                    symbolSize=SYMBOL_SIZE,
                    name=label,
                )
