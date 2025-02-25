import unittest
# arrange
from src.greeter import greet

#act
class TestGreeting(unittest.TestCase):
    def test_greets_hello_world(self):
        #assert

        self.assertEqual('Hello, World!', greet())