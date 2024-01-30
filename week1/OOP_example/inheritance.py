# Inheritance
# the practice of creating a new class from an existing class. 
# The new class inherits all the properties and methods of the existing class. 
# Here is an example where we create a new class 
# called ScientificCalculator that inherits from the Calculator class:

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b


class ScientificCalculator(Calculator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def power(self):
        return self.a ** self.b


class ProgrammerCalculator(Calculator):
    def __init__(self, a, b):
        super().__init__(a, b)

    def bitwise_and(self):
        return self.a & self.b
