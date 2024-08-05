# we can also use the naming circle_test.py but name must include the term test and underscore + name of file we are testing
# to run a unit test from console: python -m unittest (must be in project folder)
import unittest  # unit testing framework
from math import pi

from src.circle import \
    circle_area  # importing the function we wrote in the other file


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        # assertAlmostEqual checks that results are the same to 7 decimal points
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)

    # uncomment these at end of video and add the snippet in snippet.py to circle.py to pass these tests
    # def test_types(self):
    #     self.assertRaises(TypeError, circle_area, 3 + 5j)
    #     self.assertRaises(TypeError, circle_area, True)
    #     self.assertRaises(TypeError, circle_area, 'radius')
