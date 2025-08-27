import unittest
from src.greeter import greet as johnGreeter

class TestGreeter(unittest.TestCase):
    def test_greeter(self):
        self.assertEqual(johnGreeter('John'), 'Hello John')
        self.assertNotEqual(johnGreeter('Juan'), 'Hello John')

if __name__ == "__main__":
    unittest.main()