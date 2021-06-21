from tool_add_window import ToolAddWindow
from settings import *

from numpy import nan
from PySide2.QtWidgets import *
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt
import os
import pandas as pd
import shutil
import sys
import unittest

app = QApplication(sys.argv)


class ToolAddWindowTest(unittest.TestCase):
    def setUp(self):
        self.form = ToolAddWindow()
        self.save_button = self.form.ui.pushButton_2

        # Copy the files to keep the same default records there.
        # tools.csv
        shutil.copy(
            os.path.join("database", LEITZ_TOOLS),
            os.path.join("database", LEITZ_TOOLS[:-4] + "_temp.csv"),
        )

        # tools_updates.csv
        shutil.copy(
            os.path.join("database", LEITZ_TOOLS_UPDATES),
            os.path.join("database", LEITZ_TOOLS_UPDATES[:-4] + "_temp.csv"),
        )

    def clear_fields(self):
        """
        Empty all the fields in preparation - by default, the values
        are taken from metadata.json file. It should be tested as well.
        """
        self.form.ui.le_tool_id.clear()
        self.form.ui.le_classification_number.clear()
        self.form.ui.le_strategic_business_number.clear()
        self.form.ui.le_tool_diameter.clear()
        self.form.ui.le_bore_diameter.clear()
        self.form.ui.le_tool_cutting_width.clear()
        self.form.ui.le_no_of_wings.clear()
        self.form.ui.le_total_no_of_wings.clear()
        self.form.ui.le_cutting_material.clear()
        self.form.ui.le_cutting_material_quality.clear()
        self.form.ui.le_body_material.clear()
        self.form.ui.le_n_max.clear()
        self.form.ui.le_n_opt.clear()
        self.form.ui.le_rake_angle.clear()

    def get_last_record(self, column):
        last_records = pd.read_csv(os.path.join("database", LEITZ_TOOLS), delimiter=";")
        last_record = last_records.tail(1)[column].values[0]
        return last_record

    @unittest.skip
    def test_tool_id_field(self):
        COLUMN = "Identnummer"

        # Integer.
        self.form.ui.le_tool_id.setText("123")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, 123)

        # String.
        self.form.ui.le_tool_id.setText("String only")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, "String only")

        # String & integer.
        self.form.ui.le_tool_id.setText("String only 123")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, "String only 123")

        # Special characters.
        self.form.ui.le_tool_id.setText("!@#$%^&*()_")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, "!@#$%^&*()_")

    @unittest.skip
    def test_classification_number_field(self):
        COLUMN = "Klassifizierungsnummer"

        # Integer.
        self.form.ui.le_classification_number.setText("123")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, 123)

        # String.
        self.form.ui.le_classification_number.setText("String only")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, "String only")

        # String & integer.
        self.form.ui.le_classification_number.setText("String only 123")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, "String only 123")

        # Special characters.
        self.form.ui.le_classification_number.setText("!@#$%^&*()_")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, "!@#$%^&*()_")

    @unittest.skip
    def test_strategic_business_number_field(self):
        COLUMN = "SGE"

        # Integer.
        self.form.ui.le_strategic_business_number.setText("123")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, 123)

        # String.
        self.form.ui.le_strategic_business_number.setText("String only")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, "String only")

        # String & integer.
        self.form.ui.le_strategic_business_number.setText("String only 123")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, "String only 123")

        # Special characters.
        self.form.ui.le_strategic_business_number.setText("!@#$%^&*()_")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, "!@#$%^&*()_")

    def test_tool_diameter_field(self):
        COLUMN = "D"

        # Integer.
        self.clear_fields()
        QTest.keyClicks(self.form.ui.le_tool_diameter, "123")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertEqual(last_record, 123)

        # String.
        self.clear_fields()
        QTest.keyClicks(self.form.ui.le_tool_diameter, "String")
        QTest.mouseClick(self.save_button, Qt.LeftButton)
        last_record = self.get_last_record(COLUMN)
        self.assertNotEqual(last_record, "String")

    def tearDown(self):
        # tools.csv
        os.remove(os.path.join("database", LEITZ_TOOLS))
        os.rename(
            os.path.join("database", LEITZ_TOOLS[:-4] + "_temp.csv"),
            os.path.join("database", LEITZ_TOOLS),
        )

        # tools_updates.csv
        os.remove(os.path.join("database", LEITZ_TOOLS_UPDATES))
        os.rename(
            os.path.join("database", LEITZ_TOOLS_UPDATES[:-4] + "_temp.csv"),
            os.path.join("database", LEITZ_TOOLS_UPDATES),
        )


if __name__ == "__main__":
    unittest.main()
