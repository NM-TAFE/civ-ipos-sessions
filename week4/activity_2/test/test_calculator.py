import unittest
from src.calculator import add

class TestaddFunction(unittest.TestCase):
    # Types
    # int
    # act
    def test_integer_addition(self):
        self.assertEqual(add(2, 2), 4)

    # float
    def test_float_addition(self):
        self.assertIsInstance(add(2.3,2.5), float)
        self.assertEqual(add(2.5, 3.1), 5.6)
        # self.assertIsInstance(obj, (int, float))

    # complex
    def test_complex_addition(self):
        self.assertEqual(add(1 + 2j, 3 - 1j), 4 + 1j)

    # use case - whats left???
    # string
    # boolean
    # collections othe robject
    # null values
    def test_invalid_types(self):
        invalid_types =  ['2', True, {'a': False}, None]
        # arrange
        with self.assertRaises(TypeError):
            # act - string
            add("2", 3)
      
        self.assertEqual(add(False, 3), "This is a boolean please enter a number")

        with self.assertRaises(TypeError):
            # act - string
            add(None, 3)

        with self.assertRaises(TypeError):
            # act - string
            add([3,4,5], 3)
            
if __name__ == "__main__":
    unittest.main()