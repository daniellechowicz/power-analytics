from main_window import MainWindow

from PySide2.QtWidgets import *
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt
import sys
import unittest

app = QApplication(sys.argv)


class MainWindowTest(unittest.TestCase):
	def setUp(self):
		self.form = MainWindow()

	def test_default_labels(self):
		self.assertEqual(self.form.ui.labelTitle.text(), "Power Analytics")
		self.assertEqual(self.form.ui.labelSubtitle.text(), "Toolkit zur Analyse der Schnittleistung")

	def test_title_and_subtitle_labels(self):
		# Data import.
		btn = self.form.ui.buttonAdd
		QTest.mouseClick(btn, Qt.LeftButton)
		self.assertEqual(self.form.ui.labelTitle.text(), "Import")
		self.assertEqual(self.form.ui.labelSubtitle.text(), "Dateneingabe über den zu analysierenden Prozess")

		# Analysis.
		btn = self.form.ui.buttonAnalyse
		QTest.mouseClick(btn, Qt.LeftButton)
		self.assertEqual(self.form.ui.labelTitle.text(), "Analyse")
		self.assertEqual(self.form.ui.labelSubtitle.text(), "Datenauswahl und -kontrolle für die Datenauswertung")

		# Database.
		btn = self.form.ui.buttonDatabase
		QTest.mouseClick(btn, Qt.LeftButton)
		self.assertEqual(self.form.ui.labelTitle.text(), "Datenbank")
		self.assertEqual(self.form.ui.labelSubtitle.text(), "Vergleich der Messdaten mit früheren Messungen")

		# Settings.
		btn = self.form.ui.buttonSettings
		QTest.mouseClick(btn, Qt.LeftButton)
		self.assertEqual(self.form.ui.labelTitle.text(), "Einstellungen")
		self.assertEqual(self.form.ui.labelSubtitle.text(), "Einstellungen für Software- und Werkzeugeigenschaften in der Datenbank")


if __name__ == "__main__":
    unittest.main()