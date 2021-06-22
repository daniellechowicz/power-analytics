# -*- coding: utf-8 -*-

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from pyqtgraph import PlotWidget
from scipy import signal
import ctypes
import json
import numpy as np
import os
import pyqtgraph as pg
import shutil
import sys
import yaml

# Views
from ui.ui_main import Ui_MainWindow
from database_window import DatabaseWindow
from parameters_window import ParametersWindow
from multivariate_visualization_window import MultivariateVisualizationWindow
from settings_window import SettingsWindow
from tools_edit_window import ToolsEditWindow

# Backend modules
from measurement import Measurement
from database.database import Database
from database.models import Metadata
from helpers.replace import Replace
from report.report import Report

# Settings and constants
from settings import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_initial_view()
        self.setup_default_variables()
        self.setup_graphs()
        self.define_callbacks()

        # Drag functionality enabled
        self.oldPos = self.pos()
        self.showMaximized()

    def setup_ui(self):
        self.setWindowIcon(QtGui.QIcon("ui/icons/lighting.svg"))
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Power Analytics | Startseite", None
            )
        )

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Set current index at page nr 0
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.tabWidget.setCurrentIndex(0)

    def setup_default_variables(self):
        self.path_imported = False
        self.x_init = 0
        self.y_init = 0
        self.full_screen = True
        self.idle_region = 0
        self.cutting_region = 0

    def setup_graphs(self, initial=True):
        # If used for the first time, setup the range selection graphics view as well
        if initial:
            self.ui.graphicsViewRangeSelection.setBackground("w")

        # Setup the rest of the views
        self.ui.graphicsViewRaw.setBackground("w")
        self.ui.graphicsViewMM.setBackground("w")
        self.ui.graphicsViewPSD.setBackground("w")

    def reset_graphs(self, clear_range_selection=True):
        # Do not clear the first graphics view after updating the remaining views
        if clear_range_selection:
            self.ui.graphicsViewRangeSelection.clear()

        self.ui.graphicsViewRaw.clear()
        self.ui.graphicsViewMM.clear()
        self.ui.graphicsViewPSD.clear()

    def define_callbacks(self):
        # Frame size manipulation
        self.ui.buttonMaximize.clicked.connect(lambda: self.change_mode())
        self.ui.buttonMinimize.clicked.connect(lambda: self.showMinimized())
        self.ui.buttonClose.clicked.connect(lambda: sys.exit())

        # Main stacked widget
        self.ui.buttonAdd.clicked.connect(
            lambda: self.update_main_labels(
                1,
                "Import",
                "Dateneingabe über den zu analysierenden Prozess",
            )
        )
        self.ui.buttonAnalyse.clicked.connect(
            lambda: self.update_main_labels(
                2,
                "Analyse",
                "Datenauswahl und -kontrolle für die Datenauswertung",
            )
        )
        self.ui.buttonDatabase.clicked.connect(
            lambda: self.update_main_labels(
                3,
                "Datenbank",
                "Vergleich der Messdaten mit früheren Messungen",
            )
        )
        self.ui.buttonReport.clicked.connect(lambda: self.generate_report())
        self.ui.buttonSettings.clicked.connect(
            lambda: self.update_main_labels(
                4,
                "Einstellungen",
                "Einstellungen für Software- und Werkzeugeigenschaften in der Datenbank",
            )
        )

        # Data import
        self.ui.buttonPathImport.clicked.connect(lambda: self.get_path())
        self.ui.buttonParams.clicked.connect(lambda: ParametersWindow().show())
        self.ui.buttonDone.clicked.connect(lambda: self.get_data())

        # Database
        self.ui.buttonDatabaseShow.clicked.connect(lambda: self.get_database_window())
        self.ui.buttonShowBoxplots.clicked.connect(
            lambda: MultivariateVisualizationWindow().show()
        )
        self.ui.buttonDatabaseExport.clicked.connect(
            lambda: DatabaseWindow(DB_NAME, False).save()
        )
        self.ui.buttonUpdateGraphs.clicked.connect(self.update_graphs)

        # Settings
        self.ui.btn_settings.clicked.connect(lambda: SettingsWindow().show())
        self.ui.btn_tools_edit.clicked.connect(lambda: ToolsEditWindow().show())
        self.ui.btn_tools_replace.clicked.connect(lambda: self.replace_tools_CSV())

    def change_mode(self):
        if self.full_screen is False:
            self.ui.centralwidget.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 61, 74, 255), stop:1 rgba(71, 74, 120, 255)); border-radius: 0px;"
            )
            self.showMaximized()
            self.full_screen = True
        else:
            self.ui.centralwidget.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(50, 61, 74, 255), stop:1 rgba(71, 74, 120, 255)); border-radius: 10px;"
            )
            self.showNormal()
            self.full_screen = False

    def update_main_labels(self, page_index, title, subtitle):
        self.ui.stackedWidget.setCurrentIndex(page_index)
        self.ui.labelTitle.setText(title)
        self.ui.labelSubtitle.setText(subtitle)

    def get_metadata(self):
        try:
            with open("metadata.json") as json_file:
                metadata = json.load(json_file)
        except:
            metadata = None

        return metadata

    def save_default_path(self, path=None):
        with open("defaults.yaml", "w") as file:
            if path == None:
                doc = yaml.dump(
                    {
                        "root_measurement_files": os.path.join(
                            os.path.join(os.environ["USERPROFILE"]), "Desktop"
                        )
                    },
                    file,
                )
            else:
                doc = yaml.dump({"root_measurement_files": path}, file)

    def get_path(self):
        try:
            self.save_default_path(self.path)
        except:
            self.save_default_path()

        with open("defaults.yaml") as file:
            doc = yaml.full_load(file)
            dir = doc["root_measurement_files"]

        self.path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Pfad des Importfiles", str(dir)
        )

        if self.path == "" or self.path.endswith((".tdms", ".TDMS")) is False:
            ctypes.windll.user32.MessageBoxW(
                0,
                "Falscher Pfad angegeben – bitte noch einmal versuchen",
                "Power Analytics | Datenimport",
                0 | 0x40,
            )
        else:
            self.path_imported = True

    def tool_exists(self):
        metadata = self.get_metadata()
        tool_id = metadata["tool_id"]
        d = np.loadtxt(
            f"database/{LEITZ_TOOLS}", delimiter=";", dtype=str, skiprows=1, usecols=0
        )
        if tool_id in d:
            return True
        else:
            return False

    def get_data(self):
        if self.path_imported is False:
            ctypes.windll.user32.MessageBoxW(
                0,
                "Es wurde kein Messfile importiert – bitte zuerst Messdaten importieren",
                "Power Analytics | Datenimport",
                0 | 0x40,
            )
            return

        # Check whether the tool (with specified tool ID) is present in the database
        # If it is not present in the database, stop execution of the function
        if not self.tool_exists():
            ctypes.windll.user32.MessageBoxW(
                0,
                "Die angegebene Werkzeug-ID-Nummer existiert nicht - tragen Sie das Werkzeug in die Datenbank ein",
                "Power Analytics | Parameter",
                0 | 0x40,
            )
            return

        # Otherwise, new datasets will be appended to the existing graph
        self.reset_graphs()

        # Analysis can be started
        self.msr = Measurement(
            self.path,
            GROUP_NAME,
            CHANNEL_NAME,
            SAMPLING_RATE,
        )

        # Upload data and move to another page when finished
        self.x_init, self.y_init = self.msr.moving_average(WINDOW_SIZE)

        # Go to another page automatically
        self.update_main_labels(
            2,
            "Analyse",
            "Datenauswahl und -kontrolle für die Datenauswertung",
        )

        # Change to "Range selection" again
        self.ui.tabWidget.setCurrentIndex(0)

        # Select ranges for idle running and cutting
        # These ranges will be shared among all the figures
        # Resample - otherwise inconvenient use due to overload
        resampled_y = signal.resample(self.y_init, int(len(self.y_init) / 100))
        resampled_x = np.linspace(
            0, len(resampled_y) / (SAMPLING_RATE / 100), len(resampled_y)
        )
        self.setup_range_widget(resampled_x, resampled_y)

    def setup_range_widget(self, x, y):
        lr_idle = pg.LinearRegionItem(
            [int(x[-1] * 0.1), int(x[-1] * 0.3)],
            brush=(255, 96, 55, 100),
            pen=(255, 51, 0),
        )
        lr_idle.setZValue(-10)

        lr_cutting = pg.LinearRegionItem(
            [int(x[-1] * 0.4), int(x[-1] * 0.6)],
            brush=(82, 255, 152, 100),
            pen=(17, 255, 0),
        )
        lr_cutting.setZValue(-10)

        # Setup graphs
        p1 = self.ui.graphicsViewRangeSelection.addPlot(
            title="Bereichsauswahl", row=0, col=0
        )
        p1.setLabel(
            "left",
            '<span style="color: black; font-size: {}px">Leistungsaufnahme [kW]</span>'.format(
                FONTSIZE
            ),
        )
        p1.setLabel(
            "bottom",
            '<span style="color: black; font-size: {}px">Zeit [s]</span>'.format(
                FONTSIZE
            ),
        )

        p2 = self.ui.graphicsViewRangeSelection.addPlot(
            title="Leerlaufbereich", row=1, col=0
        )
        p2.setLabel(
            "left",
            '<span style="color: black; font-size: {}px">Leistungsaufnahme [kW]</span>'.format(
                FONTSIZE
            ),
        )
        p2.setLabel(
            "bottom",
            '<span style="color: black; font-size: {}px">Zeit [s]</span>'.format(
                FONTSIZE
            ),
        )

        p3 = self.ui.graphicsViewRangeSelection.addPlot(
            title="Schnittbereich", row=2, col=0
        )
        p3.setLabel(
            "left",
            '<span style="color: black; font-size: {}px">Leistungsaufnahme [kW]</span>'.format(
                FONTSIZE
            ),
        )
        p3.setLabel(
            "bottom",
            '<span style="color: black; font-size: {}px">Zeit [s]</span>'.format(
                FONTSIZE
            ),
        )

        # Add items to the graphics view
        p1.addItem(lr_idle)
        p1.addItem(lr_cutting)

        # Plot data
        p1.plot(x, y, pen=(0, 0, 0, 100))
        p2.plot(x, y, pen=(0, 0, 0, 100))
        p3.plot(x, y, pen=(0, 0, 0, 100))

        # Define callbacks
        def updateIdlePlot():
            p2.setXRange(*lr_idle.getRegion(), padding=0)

            # Since the default unit were seconds, multiply the variable by the applied sampling rate
            self.idle_region = [
                lr_idle.getRegion()[0] * SAMPLING_RATE,
                lr_idle.getRegion()[1] * SAMPLING_RATE,
            ]

        def updateidle_region():
            lr_idle.setRegion(p2.getViewBox().viewRange()[0])

        def updateCuttingPlot():
            p3.setXRange(*lr_cutting.getRegion(), padding=0)

            # Since the default unit were seconds, multiply the variable by the applied sampling rate
            self.cutting_region = [
                lr_cutting.getRegion()[0] * SAMPLING_RATE,
                lr_cutting.getRegion()[1] * SAMPLING_RATE,
            ]

        def updatecutting_region():
            lr_cutting.setRegion(p3.getViewBox().viewRange()[0])

        # Connect linear regions' callbacks with above functions
        lr_idle.sigRegionChanged.connect(updateIdlePlot)
        lr_cutting.sigRegionChanged.connect(updateCuttingPlot)
        p2.sigXRangeChanged.connect(updateidle_region)
        p3.sigXRangeChanged.connect(updatecutting_region)
        updateIdlePlot()
        updateCuttingPlot()

    def update_graphs(self):
        self.reset_graphs(clear_range_selection=False)
        self.setup_graphs(initial=False)

        # Import the data
        # Resample the data - 2 MS are too heavy for my computer to import at once
        # Resampling factor can be changed in settings.py
        # Raw
        x, y = self.msr.raw()
        x = signal.resample(x, int(len(x) / RESAMPLE_FACTOR))
        y = signal.resample(y, int(len(y) / RESAMPLE_FACTOR))
        labels = [
            self.ui.labelMinRaw,
            self.ui.labelMaxRaw,
            self.ui.labelMeanRaw,
            self.ui.labelMedianRaw,
            self.ui.labelSTDRaw,
        ]
        self.plot(self.ui.graphicsViewRaw, labels, x, y, True)

        # Moving median
        x, y = self.msr.moving_median(WINDOW_SIZE)
        x = signal.resample(x, int(len(x) / RESAMPLE_FACTOR))
        y = signal.resample(y, int(len(y) / RESAMPLE_FACTOR))
        labels = [
            self.ui.labelMinMM,
            self.ui.labelMaxMM,
            self.ui.labelMeanMM,
            self.ui.labelMedianMM,
            self.ui.labelSTDMM,
        ]
        self.plot(self.ui.graphicsViewMM, labels, x, y)

        # PSD
        x, y = self.msr.power_spectral_density()
        self.plot_psd(self.ui.graphicsViewPSD, x, y)

        # When completed, change widget's page
        self.ui.tabWidget.setCurrentIndex(1)

        if self.ui.save_to_database.isChecked():
            m = self.get_metadata()
            db = Database(DB_NAME)

            # Insert parameters to the database
            db.insert_into_metadata(
                m["author"],
                m["date"],
                m["material"],
                m["moisture_content"],
                m["cutting_direction"],
                m["rotational_speed"],
                m["feed_speed"],
                m["feed_per_tooth"],
                m["cutting_speed"],
                m["cutting_width"],
                m["cutting_depth"],
                m["cutting_angle"],
                m["mean_chip_thickness"],
                m["mean_chip_length"],
                m["tool_id"],
                m["classification_no"],
                m["strategic_business_unit"],
                m["tool_diameter"],
                m["tool_cutting_width"],
                m["bore_diameter"],
                m["no_of_wings"],
                m["total_no_of_wings"],
                m["cutting_material"],
                m["cutting_material_quality"],
                m["body_material"],
                m["n_max"],
                m["n_opt"],
                m["rake_angle"],
                m["comments"],
            )

            # Get measurement's ID (to relate parameters with the result)
            measurement_id = db.execute_command(
                "SELECT measurement_id FROM metadata ORDER BY measurement_id DESC LIMIT 1"
            )[0]
            measurement_id = measurement_id[0]

            # Get result
            _, res = self.msr.moving_average(WINDOW_SIZE)
            res = res[int(self.cutting_region[0]) : int(self.cutting_region[1])]
            res = round(np.mean(res), 3)

            # Add the result stats to the database
            db.insert_into_stats(
                res,
                measurement_id,
            )

    def plot(self, graphicsView, labels, x, y, raw=False):
        # Truncate the data accordingly to the defined regions
        # Indices can be changed in settings.py
        x = x[int(self.cutting_region[0]) : int(self.cutting_region[1])]
        y = y[int(self.cutting_region[0]) : int(self.cutting_region[1])]

        p1 = graphicsView.addPlot(row=0, col=0)
        p1.setLabel(
            "left",
            '<span style="color: black; font-size: {}px">Leistungsaufnahme [kW]</span>'.format(
                FONTSIZE
            ),
        )
        p1.setLabel(
            "bottom",
            '<span style="color: black; font-size: {}px">Zeit [s]</span>'.format(
                FONTSIZE
            ),
        )

        p1.plot(x, y, pen=pg.mkPen(color=(0, 0, 0), width=0.5))
        p1.addLegend()

        # Plot raw data in background (in order to compare filtering performance)
        if not raw:
            x_raw, y_raw = self.msr.raw()
            x_raw = signal.resample(x_raw, int(len(x_raw) / RESAMPLE_FACTOR))
            y_raw = signal.resample(y_raw, int(len(y_raw) / RESAMPLE_FACTOR))

            # Truncate the data again
            x_raw = x_raw[int(self.cutting_region[0]) : int(self.cutting_region[1])]
            y_raw = y_raw[int(self.cutting_region[0]) : int(self.cutting_region[1])]

            p1.plot(
                x_raw,
                y_raw,
                pen=pg.mkPen(color=(0, 255, 0, 100), width=0.5),
                name="Rohdaten",
            )

        labels[0].setText("%.1f" % np.min(y))
        labels[1].setText("%.1f" % np.max(y))
        labels[2].setText("%.1f" % np.mean(y))
        labels[3].setText("%.1f" % np.median(y))
        labels[4].setText("%.2f" % np.std(y))

    def plot_psd(self, graphicsView, x, y):
        p1 = graphicsView.addPlot(row=0, col=0)
        p1.setLabel(
            "left",
            '<span style="color: black; font-size: {}px">Magnitude [-]</span>'.format(
                FONTSIZE
            ),
        )
        p1.setLabel(
            "bottom",
            '<span style="color: black; font-size: {}px">Frequenz [Hz]</span>'.format(
                FONTSIZE
            ),
        )
        p1.plot(x, y, pen=(0, 0, 0, 100))

    def get_stats(self, y):
        y_idle = y[int(self.idle_region[0]) : int(self.idle_region[1])]
        y_cutting_idle = y[int(self.cutting_region[0]) : int(self.cutting_region[1])]
        y_cutting = y_cutting_idle - np.mean(y_idle)

        stats = {
            "idle": {
                "min": "%.2f" % np.min(y_idle),
                "max": "%.2f" % np.max(y_idle),
                "mean": "%.2f" % np.mean(y_idle),
                "median": "%.2f" % np.median(y_idle),
                "std": "%.3f" % np.std(y_idle),
            },
            "cutting_idle": {
                "min": "%.2f" % np.min(y_cutting_idle),
                "max": "%.2f" % np.max(y_cutting_idle),
                "mean": "%.2f" % np.mean(y_cutting_idle),
                "median": "%.2f" % np.median(y_cutting_idle),
                "std": "%.3f" % np.std(y_cutting_idle),
            },
            "cutting": {
                "min": "%.2f" % np.min(y_cutting) if np.min(y_cutting) > 0 else "0.00",
                "max": "%.2f" % np.max(y_cutting) if np.max(y_cutting) > 0 else "0.00",
                "mean": "%.2f" % np.mean(y_cutting)
                if np.mean(y_cutting) > 0
                else "0.00",
                "median": "%.2f" % np.median(y_cutting)
                if np.median(y_cutting) > 0
                else "0.00",
                "std": "%.3f" % np.std(y_cutting) if np.std(y_cutting) > 0 else "0.000",
            },
        }

        return stats

    def get_database_window(self):
        try:
            DatabaseWindow(DB_NAME).show()
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Datei {DB_NAME} konnte nicht geöffnet werden ({e})",
                "Power Analytics | Datenbank",
                0 | 0x40,
            )

    def replace_tools_CSV(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Geben Sie den Pfad der Ersatzdatei an",
            str(dir),
            "(*.csv, *.CSV)",
        )

        if path == "" or path.endswith((".csv", ".CSV")) is False:
            ctypes.windll.user32.MessageBoxW(
                0,
                "Falscher Pfad angegeben – bitte noch einmal versuchen",
                "Power Analytics | Update",
                0 | 0x40,
            )
        else:
            shutil.copy(path, f"database/{LEITZ_TOOLS}")
            r = Replace()
            ctypes.windll.user32.MessageBoxW(
                0,
                "Datei wurde erfolgreich ersetzt",
                "Power Analytics | Update",
                0 | 0x40,
            )

    def get_permission_dialog(self, text, title, utype):
        user32 = ctypes.WinDLL("user32", use_last_error=True)
        msg_box = user32.MessageBoxW
        result = msg_box(None, text, title, utype)
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())
        return result

    def generate_report(self):
        # Ask for permission
        YES_NO = 4
        YES = 6
        result = self.get_permission_dialog(
            "Wollen sie wirklich ein Protokoll erstellen? Dies kann ein paar Sekunden dauern...",
            "Power Analytics | Protokoll",
            YES_NO,
        )

        if result == YES:
            try:
                Report(
                    self.x_init,
                    self.y_init,
                    self.idle_region,
                    self.cutting_region,
                    self.get_metadata(),
                    self.get_stats(self.y_init),
                    self.path,
                )
            except Exception as e:
                ctypes.windll.user32.MessageBoxW(
                    0,
                    f"Protokoll konnte nicht generiert werden ({e})",
                    "Power Analytics | Protokoll",
                    0 | 0x40,
                )

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
