'''Considering reuse (modularisation)
when creating python programs'''

def greet():
    print("Hello, world!")

# Additional activity - create a calculator class and re-use this by instantiating it in the main.py


class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b



# So as not to contaminate your global
# namespace, it is good practice to use a
# main function.
# so that we can reuse our code as both a
# module and a script

def main():
    greet()

# we can use an if statement to ensure
# that some code is only executed when name is __main__

if __name__ == "__main__":
    print(__name__)
    main()