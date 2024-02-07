'''different ways to reuse the same code
as a module'''
import greeter
greeter.greet()

# import greeter as g
# g.greet()

# from greeter import greet
# greet()

# Addition - Activity create a acalculator class in the module
# from greeter import greet,Calculator
# greet()

# returning a score to a user
calculator = greeter.Calculator()
result = calculator.add(3, 5)

print(f"Result of addition: {result}")