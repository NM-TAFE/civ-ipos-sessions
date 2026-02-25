def add(number1, number2):
    if not isinstance(number1, (int, float, complex)) or not isinstance(number2, (int, float, complex)):
        raise TypeError("Both arguments must be integer, float of complex")

    return number1 + number2
    # pass