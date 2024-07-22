"""Demonstrates Unit Testing Concepts shown in https://www.youtube.com/watch?v=1Lfv5tUGsn8
We use an example of a function that calculates the area of a circle and show that it fails for certain input values.
Given this how do we scope what input values we want and how do we document and test that the function does all that we want it to do"""
from math import pi


def circle_area(r):
    # after running unit tests uncomment these lines then progress to adding in the snippet
    # if r < 0:
    #     raise ValueError("Radius cannot be negative.")

    return pi * r**2


# Will this function work for all values of r? Clearly not. An easy way to demonstrate this is to create a list with
# a set of values we want to test and then call our function with each of those values using a for loop like so: j in
# python is the same as i (imaginary) in maths
if __name__ == '__main__':
    radii = [2, 0, -3, 2 + 5j, True, "radius"]
    message = 'Area of circles with r = {radius} is {area}'
    for r in radii:
        A = circle_area(r)
        # format is a function we haven't seen before that fills that values in {} braces with the values of the
        # variable
        print(message.format(radius=r, area=A))

# The following is a reproduction of the values outputted when we run this code (commented-out): Area of circles with
# r = 2 is 12.566370614359172 Area of circles with r = 0 is 0.0 Area of circles with r = -3 is 28.274333882308138
# Area of circles with r = (2+5j) is (-65.97344572538566+62.83185307179586j) Area of circles with r = True is
# 3.141592653589793 Traceback (most recent call last): File
# "/Users/raf/Library/CloudStorage/OneDrive-Personal/Work/code/testing-overview/circle.py", line 17, in <module> A =
# circle_area(r) File "/Users/raf/Library/CloudStorage/OneDrive-Personal/Work/code/testing-overview/circle.py",
# line 8, in circle_area return pi * r**2 TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
# ---end of output---
