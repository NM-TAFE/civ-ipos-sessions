# Put in tests/ folder as test_greeter.py
# remember to mark directory tests/ as:
# Test Sources within pycharm
# python -m unittest discover

# # Seeting you path in visual studio
# import sys
# import os
#
# # Determine the absolute path to your module directory
# module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/ROBERJ/Downloads/workshop_part3/workshop_part3'))

# Prepend the module path to sys.path
# sys.path.insert(0, module_path)
# from src/greeter import greet
from src.greeter import greet
from src import greeter as g
import unittest


class TestGreeting(unittest.TestCase):
    def test_greets_hello_world(self):
        self.assertEqual("Hello, World!", greet())
