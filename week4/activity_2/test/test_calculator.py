import unittest
from src.calculator import add

class TestaddFunction(unittest.TestCase):

    pass
    # Types
    def test_integer_addiotn(self):
        self.assertEqual(add(2,3), 5)

    # float
    def test_decimal_addition(self):
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)
    # complex
    def test_complex_addition(self):
        self.assertEqual(add(1 + 2j, 3 - 1j),4 + 1j)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            add("2", 3)
        with self.assertRaises(TypeError):
            add([3], 3)
    def other_types(self):
        with self.assertRaises(TypeError):
            add(True, 3)
        with self.assertRaises(TypeError):
            add((1), 3)

    # TODO use case - whats left to test???
    # string
    # boolean
    # collections other objects
    # null values

        # arrange

            # act - type
    
            # act - type
  
        # assert

if __name__ == "__main__":
    unittest.main()