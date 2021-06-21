from parameters_window import ParametersWindow

from PySide2.QtWidgets import *
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt
import json
import sys
import unittest

app = QApplication(sys.argv)


class ParametersWindowTest(unittest.TestCase):
    def setUp(self):
        self.form = ParametersWindow()

    def setFormToZero(self):
        """
        Empty all the fields in preparation - by default, the values
        are taken from metadata.json file. It should be tested as well.
        """
        self.form.ui.le_author.clear()
        self.form.ui.le_material.clear()
        self.form.ui.le_moisture_content.clear()
        self.form.ui.le_cutting_direction.clear()
        self.form.ui.le_rotational_speed.clear()
        self.form.ui.le_feed_speed.clear()
        self.form.ui.le_cutting_width.clear()
        self.form.ui.le_cutting_depth.clear()
        self.form.ui.le_cutting_angle.clear()
        self.form.ui.le_tool_id.clear()
        self.form.ui.le_comments.clear()

    def get_last_used(self):
        try:
            with open("metadata.json") as json_file:
                metadata = json.load(json_file)
        except:
            metadata = None
        return metadata

    def test_line_edits_no_metadata(self):
        """
        Testing line edits with no metadata.json available.
        The idea of this test is to test type validators.
        Just the most crucial fields are tested.
        """

        # Moisture content field.
        # Integer type validator - this is why, whenever "." or "," is typed,
        # the field will ignore it forcing end user to adjust data type.
        self.setFormToZero()
        QTest.keyClicks(self.form.ui.le_moisture_content, "12.3")
        self.assertEqual(self.form.ui.le_moisture_content.text(), "123")

        self.setFormToZero()
        QTest.keyClicks(self.form.ui.le_moisture_content, "12,3")
        self.assertEqual(self.form.ui.le_moisture_content.text(), "123")

        self.setFormToZero()
        QTest.keyClicks(self.form.ui.le_moisture_content, "1.2.3.4.5")
        self.assertEqual(self.form.ui.le_moisture_content.text(), "12345")

        # Rotational speed.
        # Float type validator.
        self.setFormToZero()
        QTest.keyClicks(self.form.ui.le_rotational_speed, "1,0")
        self.assertEqual(self.form.ui.le_rotational_speed.text(), "1,0")

    def test_line_edits_with_metadata(self):
        metadata = self.get_last_used()

        self.assertEqual(self.form.ui.le_author.text(), metadata["author"])
        self.assertEqual(self.form.ui.le_material.text(), metadata["material"])
        self.assertEqual(
            self.form.ui.le_moisture_content.text(), metadata["moisture_content"]
        )
        self.assertEqual(
            self.form.ui.le_cutting_direction.text(), metadata["cutting_direction"]
        )
        self.assertEqual(
            self.form.ui.le_rotational_speed.text(), metadata["rotational_speed"]
        )
        self.assertEqual(self.form.ui.le_feed_speed.text(), metadata["feed_speed"])
        self.assertEqual(
            self.form.ui.le_cutting_width.text(), metadata["cutting_width"]
        )
        self.assertEqual(
            self.form.ui.le_cutting_depth.text(), metadata["cutting_depth"]
        )
        self.assertEqual(
            self.form.ui.le_cutting_angle.text(), metadata["cutting_angle"]
        )
        self.assertEqual(self.form.ui.le_tool_id.text(), metadata["tool_id"])
        self.assertEqual(self.form.ui.le_comments.text(), metadata["comments"])


if __name__ == "__main__":
    unittest.main()
