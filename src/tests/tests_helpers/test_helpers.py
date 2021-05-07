"""
The following class can only be called from the root folder (i.e. "src").
To run the class, open the terminal and type: python -m unittest tests.tests_helpers.test_helpers.Testing
"""

import unittest

from helpers.helpers import translate


class Testing(unittest.TestCase):
    def test_translate(self):
        # General tests
        self.assertEqual(translate("No square brackets at the end []"), "no_square_brackets_at_the_end")
        self.assertEqual(translate("[No square brackets and no content in square brackets]"), "")

        # Specific tests
        self.assertEqual(translate("Material"), "material")
        self.assertEqual(translate("Moisture content [%]"), "moisture_content")
        self.assertEqual(translate("Cutting direction"), "cutting_direction")
        self.assertEqual(translate("Mean chip thickness [mm]"), "mean_chip_thickness")
        self.assertEqual(translate("Total number of wings"), "total_no_of_wings")


if __name__ == "__main__":
    unittest.main()
