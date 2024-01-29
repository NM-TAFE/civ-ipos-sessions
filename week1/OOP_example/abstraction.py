# ├── main.py
# └── calculator.py

# Abstraction is the practice of hiding the implementation details of a class from the outside world. 
# In Python, we can achieve abstraction by using abstract classes and methods. 
# Here is an example of how we can use abstraction to create an abstract class called AbstractCalculator:

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
