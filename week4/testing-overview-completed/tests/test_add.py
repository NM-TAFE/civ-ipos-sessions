# file: test_add.py
import unittest

from src.add import add
# from src.add import add

class TestAddFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertAlmostEqual(add(2.5, 3.5), 6.0)
        self.assertEqual(add(2 + 1j, 3 - 1j), 5 + 0j)

    def test_invalid_type_raises_error(self):
        with self.assertRaises(TypeError):
            add("2", 3)
            add(2, "3")
            add([2], 3)
            add(2, None)

if __name__ == '__main__':
    unittest.main()






















# class TestAddFunction(unittest.TestCase):
#
#     def test_integer_numbers(self):
#         result = add(2, 3)
#         self.assertEqual(result, 5)
#
#     def test_float_numbers(self):
#         result = add(2.5, 3.5)
#         self.assertAlmostEqual(result, 6.0)
#
#     def test_complex_numbers(self):
#         result = add(2 + 1j, 3 - 1j)
#         self.assertEqual(result, 5 + 0j)
#
#     def test_invalid_type_raises_error(self):
#         with self.assertRaises(TypeError):
#             add("2", 3)
#
#         with self.assertRaises(TypeError):
#             add(2, "3")
#
#         with self.assertRaises(TypeError):
#             add([2], 3)
#
#         with self.assertRaises(TypeError):
#             add(2, None)

# python -m unittest test_add.TestAddFunction.test_add
