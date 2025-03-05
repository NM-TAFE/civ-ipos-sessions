def add(number, number2):
    """
    Adds two numbers and returns the sum.

    Parameters:
    number1 (int, float, complex): The first number.
    number2 (int, float, complex): The second number.

    Returns:
    int, float, complex: The sum of the two numbers.

    Raises:
    TypeError: If inputs are not int, float, or complex.

    No error for Boolean see module below line 17
    """
    if (isinstance(number, bool) or isinstance(number2, bool)):
        return f"This is a boolean please enter a number"
    
    return number + number2