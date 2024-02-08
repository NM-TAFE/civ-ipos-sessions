# Put in tests/ folder as test_greeter.py
# remember to mark directory tests/ as:
# Test Sources within pycharm
# from greeter import greet
import unittest

from src import greeter as g

class TestGreeting(unittest.TestCase):
    def test_greets_hello_world(self):
        self.assertEqual("Hello, World!", g.greet())
