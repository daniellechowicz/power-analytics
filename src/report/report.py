from database.database import Database
from jinja2 import Environment, FileSystemLoader
from PySide2 import QtWidgets
from report.plot import Plot
from settings import *
import base64
import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pdfkit
import yaml


class Report:
    def __init__(self, x, y, idle, cutting, metadata, stats, measurement_file):
        self.x = x
        self.y = y
        self.idle = idle  # This is a list
        self.cutting = cutting  # This is a list
        self.metadata = metadata  # This is a dictionary
        self.stats = stats  # This is a dictionary
        self.measurement_file = measurement_file

        # Generate new filename
        self.now = datetime.datetime.now().strftime("%d-%m-%Y")
        self.filename = "Report " + self.now + ".pdf"
        self.set_path()
        if self.checkIfExists(self.filename):
            self.setAlternativeFilename()

        self.generate_image_from_data()

        # Generate document
        self.generate()

    def set_path(self):
        with open("defaults.yaml") as file:
            doc = yaml.full_load(file)
            dir = doc["root_measurement_files"]
        self.directory_path = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Wählen Sie einen Ordner für das Messprotokoll", str(dir)
        )

    def checkIfExists(self, filename):
        found = False
        for filename_ in os.listdir(self.directory_path):
            if filename_ == filename:
                found = True
        return found

    def setAlternativeFilename(self):
        exists = True
        counter = 1
        while exists:
            alternativeFilename = self.filename[:-4] + " V" + str(counter) + ".pdf"
            counter += 1
            if not self.checkIfExists(alternativeFilename):
                exists = False
        self.filename = alternativeFilename

    def generate_image_from_data(self):
        idle = {
            "start": round(self.idle[0] / SAMPLING_RATE, 2),
            "stop": round(self.idle[1] / SAMPLING_RATE, 2),
        }
        cutting = {
            "start": round(self.cutting[0] / SAMPLING_RATE, 2),
            "stop": round(self.cutting[1] / SAMPLING_RATE, 2),
        }

        plot = Plot(idle, cutting, self.x, self.y, (8, 4))
        plot.plot_raw(True, "report/figures/{}".format(self.filename[:-4] + ".png"))
        plot.plot_cutting(True, "report/figures/{}".format(self.filename[:-4] + ".png"))

    def image_to_base64_string(self, filepath: str):
        """
        Takes a filepath and converts the image saved there to its base64 encoding,
        then decodes that into a string.
        """
        with open(filepath, "rb") as f:
            return base64.b64encode(f.read()).decode()

    def generate(self):
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("report/template.html")
        # Generate html with base64 encoded string containing image
        html_string = template.render(
            {
                "logo": self.image_to_base64_string("report/logo.png"),
                "filename": self.filename,
                "measurement_file": {
                    "path": self.measurement_file,
                    "filename": os.path.basename(self.measurement_file),
                },
                "figures": [
                    self.image_to_base64_string(
                        "report/figures/{}_full.png".format(self.filename[:-4])
                    ),
                    self.image_to_base64_string(
                        "report/figures/{}_cutting.png".format(self.filename[:-4])
                    ),
                ],
                "metadata": self.metadata,
                "stats": self.stats,
            }
        )

        # Setup config
        path_wkhtmltopdf = r"report/bin/wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

        # Generate pdf
        # 2. User-defined (primary choice)
        pdfkit.from_string(
            html_string,
            os.path.join(self.directory_path, self.filename),
            configuration=config,
        )

        # Show pdf
        current_dir = os.getcwd()
        os.chdir(self.directory_path)  # os.startfile("reports/Report.pdf") did not work
        os.startfile(self.filename)
        os.chdir(current_dir)


class AutoReport:
    """
    No path specified by user. Just default directory.
    """

    def __init__(self, x, y, idle, cutting, metadata, stats, measurement_file):
        self.x = x
        self.y = y
        self.idle = idle  # This is a list
        self.cutting = cutting  # This is a list
        self.metadata = metadata  # This is a dictionary
        self.stats = stats  # This is a dictionary
        self.measurement_file = measurement_file

        # Generate new filename
        self.now = datetime.datetime.now().strftime("%d-%m-%Y")
        self.filename = "Report " + self.now + ".pdf"
        if self.checkIfExists(self.filename):
            self.setAlternativeFilename()

        self.generate_image_from_data()

        # Generate document
        self.generate()

        # Add report's name to the database.
        # This functionality will be needed in order to open
        # old reports saved in default directory.
        self.update_database_report_name()

    def checkIfExists(self, filename):
        found = False
        for filename_ in os.listdir("report/reports"):
            if filename_ == filename:
                found = True
        return found

    def setAlternativeFilename(self):
        exists = True
        counter = 1
        while exists:
            alternativeFilename = self.filename[:-4] + " V" + str(counter) + ".pdf"
            counter += 1
            if not self.checkIfExists(alternativeFilename):
                exists = False
        self.filename = alternativeFilename

    def generate_image_from_data(self):
        idle = {
            "start": round(self.idle[0] / SAMPLING_RATE, 2),
            "stop": round(self.idle[1] / SAMPLING_RATE, 2),
        }
        cutting = {
            "start": round(self.cutting[0] / SAMPLING_RATE, 2),
            "stop": round(self.cutting[1] / SAMPLING_RATE, 2),
        }

        plot = Plot(idle, cutting, self.x, self.y, (8, 4))
        plot.plot_raw(True, "report/figures/{}".format(self.filename[:-4] + ".png"))
        plot.plot_cutting(True, "report/figures/{}".format(self.filename[:-4] + ".png"))

    def image_to_base64_string(self, filepath: str):
        """
        Takes a filepath and converts the image saved there to its base64 encoding,
        then decodes that into a string.
        """
        with open(filepath, "rb") as f:
            return base64.b64encode(f.read()).decode()

    def generate(self):
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template("report/template.html")
        # Generate html with base64 encoded string containing image
        html_string = template.render(
            {
                "logo": self.image_to_base64_string("report/logo.png"),
                "filename": self.filename,
                "measurement_file": {
                    "path": self.measurement_file,
                    "filename": os.path.basename(self.measurement_file),
                },
                "figures": [
                    self.image_to_base64_string(
                        "report/figures/{}_full.png".format(self.filename[:-4])
                    ),
                    self.image_to_base64_string(
                        "report/figures/{}_cutting.png".format(self.filename[:-4])
                    ),
                ],
                "metadata": self.metadata,
                "stats": self.stats,
            }
        )

        # Setup config
        path_wkhtmltopdf = r"report/bin/wkhtmltopdf.exe"
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

        # Generate pdf
        # 1. Default (just in case)
        pdfkit.from_string(
            html_string, "report/reports/{}".format(self.filename), configuration=config
        )

    def update_database_report_name(self):
        db = Database(DB_NAME)
        # Get measurement's ID (to relate parameters with the result).
        measurement_id = db.execute_command(
            "SELECT measurement_id FROM metadata ORDER BY measurement_id DESC LIMIT 1"
        )[0]
        measurement_id = measurement_id[0]
        db.add_report_name(measurement_id, self.filename)