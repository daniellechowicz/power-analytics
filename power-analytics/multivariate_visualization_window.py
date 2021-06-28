# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_visualization import Ui_Visualization

from database.read import Read
from settings import *
from helpers.helpers import get_full_name
import ctypes
import json
import os
import pyqtgraph as pg


class MultivariateVisualizationWindow(QMainWindow):

    HEADERS = {
        0: "rotational_speed",
        1: "feed_speed",
        2: "feed_per_tooth",
        3: "cutting_speed",
        4: "cutting_width",
        5: "cutting_depth",
        6: "shear_angle",
        7: "tool_diameter",
        8: "tool_cutting_width",
        9: "no_of_wings",
        10: "total_no_of_wings",
        11: "rake_angle",
        12: "bore_diameter",
    }

    INDICES = {
        0: "material",
        1: "cutting_direction",
        2: "cutting_material",
        3: "body_material",
    }

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Visualization()
        self.ui.setupUi(self)
        self.setup_user_interface()
        self.set_raw_metadata()
        self.setup_callbacks()
        self.showMaximized()

        # Initialize database object.
        self.db = Read(os.path.join(Strings.DIRECTORY_DATABASE, DB_NAME))

    def setup_user_interface(self):
        self.setWindowIcon(QtGui.QIcon("ui/icons/lighting.svg"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow",
                f"{Strings.APP_NAME} | {Strings.DIALOG_VISUALIZATION}",
                None,
            )
        )

        # Remove title bar.
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.graphics_view.setBackground("w")

        # Setup labels accordingly to the chosen parameters.
        self.setup_labels_from_metadata()

    def setup_labels_from_metadata(self):
        self.set_metadata()
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
                f"Datenvisualisierung konnte nicht gestartet werden.",
                f"{Strings.APP_NAME} | {Strings.DIALOG_VISUALIZATION}",
                0 | 0x40,
            )

    def setup_callbacks(self):
        """
        Since this functionality contains multitude of different buttons,
        setting the callbacks manually would be really intimidating.
        Therefore, it was decided to set them up using the loop. However,
        slighly different approach has to be applied in order to achieve that.
        Follow the link given below to find out more.
        """

        self.ui.btn_close.clicked.connect(lambda: self.close())

        # QGroupBox -> QFrame -> QPushButton
        # "choice_groupbox" is the one I have to use.
        for widget_1 in self.ui.choice_groupbox.children():
            if isinstance(widget_1, QFrame):
                for widget_2 in widget_1.children():
                    if isinstance(widget_2, QPushButton):
                        button_text = widget_2.text()
                        row_id = int(button_text.split("_")[0])
                        column_id = int(button_text.split("_")[1])

                        # Get corresponding variables.
                        categorical_var = self.INDICES[row_id]
                        numerical_var = self.HEADERS[column_id]

                        # Explained here:
                        # https://stackoverflow.com/questions/4578861/connecting-slots-and-signals-in-pyqt4-in-a-loop
                        helper = lambda cat, num: (
                            lambda: self.plot_chosen_combination(cat, num)
                        )
                        widget_2.clicked.connect(helper(categorical_var, numerical_var))

    def set_metadata(self):
        try:
            with open("metadata.json") as json_file:
                self.metadata = json.load(json_file)
        except:
            self.metadata = None

    def update_metadata(self, key, value):
        for old_key, _ in self.metadata.items():
            if old_key == key:
                self.metadata[key] = value

    def set_raw_metadata(self):
        """
        Used for plotting current measurement value.
        The function above does the same, but within plotting function,
        the metadata is being updated, which makes it quite difficult to work with.
        """

        try:
            with open("metadata.json") as json_file:
                self.metadata_raw = json.load(json_file)
        except:
            self.metadata_raw = None

    def set_query(self):
        self.query = f"""
        SELECT mean_cutting_no_idle 
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
            AND shear_angle={self.metadata["shear_angle"]}
            AND mean_chip_thickness={self.metadata["mean_chip_thickness"]}
            AND mean_chip_length={self.metadata["mean_chip_length"]}
            AND tool_diameter={self.metadata["tool_diameter"]}
            AND tool_cutting_width={self.metadata["tool_cutting_width"]}
            AND no_of_wings={self.metadata["no_of_wings"]}
            AND total_no_of_wings={self.metadata["total_no_of_wings"]}
            AND cutting_material="{self.metadata["cutting_material"]}"
            AND body_material="{self.metadata["body_material"]}"
            AND rake_angle={self.metadata["rake_angle"]}
            AND bore_diameter={self.metadata["bore_diameter"]}
        );
        """

    def plot_chosen_combination(self, categorical_var, numerical_var):
        # Clear the window (if not, it would append to the previous view).
        self.ui.graphics_view.clear()

        win = self.ui.graphics_view.addPlot(row=0, col=0)
        win.addLegend()

        # Setup X- and Y-axis labels.
        win.setLabel(
            "left",
            '<span style="color: black; font-size: {}px">Leistungsaufnahme [kW]</span>'.format(
                FONTSIZE
            ),
        )
        win.setLabel(
            "bottom",
            '<span style="color: black; font-size: {}px">{}</span>'.format(
                FONTSIZE, get_full_name(numerical_var)
            ),
        )

        # Every time button is pressed, reset the metadata.
        self.set_metadata()

        # Scatter labels (do not repeat if already set).
        labels = []
        CURRENT_DRAWN = False

        # Get and loop through all the names of the columns within the database
        # which contain numerical values only.
        for i, n_var in enumerate(self.db.get_unique_values(numerical_var)):
            self.update_metadata(numerical_var, n_var)

            # Get and loop through all the names of the columns within the database
            # which contain categorical values only.
            for j, c_var in enumerate(self.db.get_unique_values(categorical_var)):
                self.update_metadata(categorical_var, c_var)

                self.set_query()

                y = []
                for result in self.db.cursor.execute(self.query).fetchall():
                    y.append(result[0])

                if c_var not in labels:
                    labels.append(c_var)
                    label = f"{c_var}"
                else:
                    label = None

                win.plot(
                    x=[self.metadata[numerical_var]] * len(y),
                    y=y,
                    symbolPen=COLOURS[j],
                    symbolBrush=COLOURS[j],
                    symbol=SYMBOLS[j],
                    symbolSize=SYMBOL_SIZE,
                    name=label,
                )

                # Draw just once.
                # Get the last record and plot it differently if it is equal to "y".
                last_record = self.db.cursor.execute(
                    "SELECT mean_cutting_no_idle FROM stats ORDER BY measurement_id DESC LIMIT 1;"
                ).fetchall()[0][0]

                # Due to all the updates that were made,
                # the following condition is necessary.
                if float(n_var) == float(self.metadata_raw[numerical_var]):
                    # Did it this way on purpose - otherwise,
                    # the symbol would be moved to background,
                    # what can cause lack of readability.
                    if CURRENT_DRAWN is False:
                        win.plot(
                            x=[self.metadata[numerical_var]],
                            y=[last_record],
                            symbolPen="c",
                            symbolBrush="c",
                            symbol="o",
                            symbolSize=SYMBOL_SIZE,
                            name="Aktuelle Messung",
                        )
                    else:
                        win.plot(
                            x=[self.metadata[numerical_var]],
                            y=[last_record],
                            symbolPen="c",
                            symbolBrush="c",
                            symbol="o",
                            symbolSize=SYMBOL_SIZE,
                            name=None,
                        )
                    CURRENT_DRAWN = True
