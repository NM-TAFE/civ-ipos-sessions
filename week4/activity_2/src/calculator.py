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

    if not isinstance(number, (int, float, complex)) or not isinstance(number, (int, float, complex)):
        raise TypeError('These are not valid types')
    # Complex numbers add(1 + 2j, 3 - 1j) =  4 + 1j
    # You get int, float and complex
    return number + number2
