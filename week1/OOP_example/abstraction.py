# Abstraction
# the practice of hiding the implementation details of a class from the outside world. 
# after creating the abstract class we can reuse abstract classes and methods. 
# here is an example using an abstract class called AbstractCalculator:

from abc import ABC, abstractmethod

class AbstractCalculator(ABC):
    @abstractmethod
    def calculate(self):
        pass


class Calculator(AbstractCalculator):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b


class ScientificCalculator(AbstractCalculator):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a ** self.b
