
def some_function(some_variable):
    return some_variable + 2

def some_other_function(some1_variable):

    some1_variable = str(some1_variable)
    print(f'{some1_variable=}') # = sign in an f-string is super useful - it formats the variable name followed by its value in the string.

    some1_variable = int(some1_variable) 
    return some_function(some1_variable)

some_other_function(42)