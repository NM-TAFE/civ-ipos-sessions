def add(x, y):
    """Calculate the sum of two numbers."""
    if type(x) not in (int, float, complex) or type(y) not in (int, float, complex):
        raise TypeError("Arguments must be integers, floats, or complex numbers.")
    return x + y

