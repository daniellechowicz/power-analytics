from settings_window import SettingsWindow

from PySide2.QtWidgets import *
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt
import json
import os
import shutil
import sys
import unittest

app = QApplication(sys.argv)


class SettingsWindowTest(unittest.TestCase):
	def setUp(self):
		self.form = SettingsWindow()

		# Copy settings to keep the same default settings.
		shutil.copy("settings.json", "settings_temp.json")

	def get_last_settings(self):
		try:
			with open("settings.json") as json_file:
				settings = json.load(json_file)
		except:
			settings = None
		return settings

	def test_primary_settings_data_types(self):
		"""
		Testing on original settings.json.
		Data types after changing settings.json file need to be tested too.
		"""
		settings = self.get_last_settings()

		self.assertIsInstance(settings["group_name"], str)
		self.assertIsInstance(settings["channel_name"], str)
		self.assertIsInstance(settings["fontsize"], int)
		self.assertIsInstance(settings["fontsize_report"], int)
		self.assertIsInstance(settings["resolution"], int)
		self.assertIsInstance(settings["sampling_rate"], int)
		self.assertIsInstance(settings["resample_factor"], int)
		self.assertIsInstance(settings["cutoff_frequency"], int)
		self.assertIsInstance(settings["order"], int)
		self.assertIsInstance(settings["window_size"], int)
		self.assertIsInstance(settings["idle_0"], int)
		self.assertIsInstance(settings["idle_1"], int)
		self.assertIsInstance(settings["cutting_0"], int)
		self.assertIsInstance(settings["cutting_1"], int)
		self.assertIsInstance(settings["window_name"], str)
		self.assertIsInstance(settings["db_name"], str)
		self.assertIsInstance(settings["db_csv_name"], str)
		self.assertIsInstance(settings["leitz_tools"], str)
		self.assertIsInstance(settings["leitz_tools_updates"], str)
		self.assertIsInstance(settings["symbols"], list)
		self.assertIsInstance(settings["colours"], list)
		self.assertIsInstance(settings["symbol_size"], int)

	def test_secondary_settings_data_types(self):
		"""
		Testing on secondary settings.json (after changing its values).
		It is crucial for the software to work with the same data types.
		"""
		# First of all, change some settings.
		self.form.ui.le_group_name.setText("Test group name")
		self.form.ui.le_channel_name.setText("Test channel name")
		self.form.ui.le_sampling_rate.setText("999")
		self.form.ui.le_resample_factor.setText("999")
		self.form.ui.le_window_size.setText("999")
		self.form.ui.le_idle_0.setText("999")
		self.form.ui.le_idle_1.setText("999")
		self.form.ui.le_cutting_0.setText("999")
		self.form.ui.le_cutting_1.setText("999")
		self.form.ui.le_leitz_tools.setText("Test name")

		# Save entered values by pressint the button.
		save_button = self.form.ui.btnAccept
		QTest.mouseClick(save_button, Qt.LeftButton)

		settings = self.get_last_settings()

		self.assertIsInstance(settings["group_name"], str)
		self.assertIsInstance(settings["channel_name"], str)
		self.assertIsInstance(settings["sampling_rate"], int)
		self.assertIsInstance(settings["resample_factor"], int)
		self.assertIsInstance(settings["window_size"], int)
		self.assertIsInstance(settings["idle_0"], int)
		self.assertIsInstance(settings["idle_1"], int)
		self.assertIsInstance(settings["cutting_0"], int)
		self.assertIsInstance(settings["cutting_1"], int)
		self.assertIsInstance(settings["leitz_tools"], str)

	def tearDown(self):
		os.remove("settings.json")
		os.rename("settings_temp.json", "settings.json")


if __name__ == "__main__":
	unittest.main()