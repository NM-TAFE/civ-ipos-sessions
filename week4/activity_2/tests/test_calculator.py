import unittest

# TODO Use  the absolute import
from src.calculator import add


class TestaddFunction(unittest.TestCase):
    pass
    # Types
    def test_types(self):
        with self.assertRaises(TypeError):
            add(2,"3")
        with self.assertRaises(TypeError):
            add(2, [3])
        with self.assertRaises(TypeError):
            add(2, {"value":3})

    # float
    def test_float(self):
        self.assertEqual(add(2.5,2.6), 5.1, "This is the float test not working")

    # complex
    def test_complex(self):
        # pass
        self.assertEqual(add(1 + 2j, 3 - 1j), 4 + 1j)

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
