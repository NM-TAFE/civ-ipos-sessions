# Polymorphism
# the practice of using a single interface to represent multiple types of objects. 
# In Python, we combine inheritance and method overriding. 
# Here is an example where we create a list of calculators 
# that can perform different operations:

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b


class ScientificCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a ** self.b


calculators = [
    Calculator(2, 3),
    ScientificCalculator(2, 3)
]

for calculator in calculators:
    print(calculator.calculate())
