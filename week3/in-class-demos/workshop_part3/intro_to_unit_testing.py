'''Basic unit test and how to get it working
in PyCharm'''

# Put in src/ folder as greeter.py
# **Remember** to mark directory src/ as
# Sources Root within PyCharm
def greet():
    return 'Hello, World!'

print(greet())

# Put in tests/ folder as test_greeter.py
# remember to mark directory tests/ as:
# Test Sources within pycharm
#
# import unittest


# class TestGreeting(unittest.TestCase):
#     def test_greets_hello_world(self):
#         self.assertEqual("Hello, World!", greet())