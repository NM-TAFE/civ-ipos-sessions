import greeter
greeter.greet()

# use an alias - consider why might we do this?
# import greeter as g
# g.greet()


# sometimes we only want to import what we need
# from greeter import greet
# greet()

# Additional Activity create a calculator class in the module
calculator = greeter.Calculator()
result = calculator.add(3, 5)
# Use the new class to return a score to a user


print(f"Result of addition:{result}")


