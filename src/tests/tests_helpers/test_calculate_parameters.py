# coding=utf-8
""" Input and output data based on "Berechnung Schnittparameter" sheet """

import sys

sys.path.append("../..")

import numpy as np
import unittest

from helpers.calculate_parameters import *


class Testing(unittest.TestCase):
    def test_cutting_speed(self):
        # Tool diameter
        self.assertEqual(get_cutting_speed(165, 6945), 60)
        self.assertEqual(get_cutting_speed(165.0, 6945), 60)
        self.assertNotEqual(get_cutting_speed(164, 6945), 60)
        self.assertNotEqual(get_cutting_speed(166, 6945), 60)

        # Rotational speed
        self.assertEqual(get_cutting_speed(165, 6945), 60)
        self.assertEqual(get_cutting_speed(165, 6945.0), 60)
        self.assertNotEqual(get_cutting_speed(165, 6800), 60)
        self.assertNotEqual(get_cutting_speed(165, 7000), 60)

    def test_feed_per_tooth(self):
        self.assertEqual(get_feed_per_tooth(17, 13890, 1), 1.224)
        self.assertEqual(get_feed_per_tooth(14, 11575, 1), 1.210)
        self.assertEqual(get_feed_per_tooth(11, 9260, 1), 1.188)
        self.assertEqual(get_feed_per_tooth(8, 6945, 1), 1.152)
        self.assertEqual(get_feed_per_tooth(6, 4630, 1), 1.296)
        self.assertEqual(get_feed_per_tooth(3, 2315, 1), 1.296)
        self.assertEqual(get_feed_per_tooth(17, 13890, 2), 0.612)
        self.assertEqual(get_feed_per_tooth(14, 11575, 2), 0.605)
        self.assertEqual(get_feed_per_tooth(11, 9260, 2), 0.594)
        self.assertEqual(get_feed_per_tooth(8, 6945, 2), 0.576)
        self.assertEqual(get_feed_per_tooth(6, 4630, 2), 0.648)
        self.assertEqual(get_feed_per_tooth(3, 2315, 2), 0.648)

    def test_feed_speed(self):
        # Equal to...
        self.assertEqual(get_feed_speed(1.224, 13890, 1), 17)
        self.assertEqual(get_feed_speed(1.210, 11575, 1), 14)
        self.assertEqual(get_feed_speed(1.188, 9260, 1), 11)
        self.assertEqual(get_feed_speed(1.152, 6945, 1), 8)
        self.assertEqual(get_feed_speed(1.296, 4630, 1), 6)
        self.assertEqual(get_feed_speed(1.296, 2315, 1), 3)
        self.assertEqual(get_feed_speed(0.612, 13890, 2), 17)
        self.assertEqual(get_feed_speed(0.605, 11575, 2), 14)
        self.assertEqual(get_feed_speed(0.594, 9260, 2), 11)
        self.assertEqual(get_feed_speed(0.576, 6945, 2), 8)
        self.assertEqual(get_feed_speed(0.648, 4630, 2), 6)
        self.assertEqual(get_feed_speed(0.648, 2315, 2), 3)

        # Not equal to...
        self.assertNotEqual(get_feed_speed(1.224, 13890, 1), 16)
        self.assertNotEqual(get_feed_speed(1.210, 11575, 1), 13)
        self.assertNotEqual(get_feed_speed(1.188, 9260, 1), 10)
        self.assertNotEqual(get_feed_speed(1.152, 6945, 1), 7)
        self.assertNotEqual(get_feed_speed(1.296, 4630, 1), 5)
        self.assertNotEqual(get_feed_speed(1.296, 2315, 1), 2)
        self.assertNotEqual(get_feed_speed(0.612, 13890, 2), 16)
        self.assertNotEqual(get_feed_speed(0.605, 11575, 2), 13)
        self.assertNotEqual(get_feed_speed(0.594, 9260, 2), 12)
        self.assertNotEqual(get_feed_speed(0.576, 6945, 2), 7)
        self.assertNotEqual(get_feed_speed(0.648, 4630, 2), 5)
        self.assertNotEqual(get_feed_speed(0.648, 2315, 2), 2)

    def test_engagement_angle(self):
        self.assertEqual(get_engagement_angle(165, 10), 28.5)
        self.assertNotEqual(get_engagement_angle(150, 10), 28.5)

    def test_mean_chip_thickness(self):
        self.assertEqual(get_mean_chip_thickness(90, 165, 10, 1.224), 0.298)
        self.assertEqual(get_mean_chip_thickness(90, 165, 10, 1.210), 0.295)
        self.assertEqual(get_mean_chip_thickness(90, 165, 10, 1.188), 0.289)
        self.assertEqual(get_mean_chip_thickness(90, 165, 10, 1.152), 0.281)
        self.assertEqual(get_mean_chip_thickness(90, 165, 10, 1.296), 0.316)
        self.assertEqual(get_mean_chip_thickness(90, 165, 10, 1.296), 0.316)

    def test_mean_chip_length(self):
        self.assertEqual(get_mean_chip_length(165, 10), 41.04)


if __name__ == "__main__":
    unittest.main()
