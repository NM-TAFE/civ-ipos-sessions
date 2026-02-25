import unittest
from src.greeter import greet

class TestGreeter(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet('John'), 'Hello John')

if __name__ == "__main__":
    unittest.main()