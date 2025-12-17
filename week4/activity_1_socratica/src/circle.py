"""
Demonstrates Unit Testing Concepts shown in https://www.youtube.com/watch?v=1Lfv5tUGsn8
We use an example of a function that calculates the area of a circle and show that it fails for certain input values.
Given this how do we scope what input values we want and how do we document and test that the function does all that we want it to do
"""
from math import pi


def circle_area(r):
    # after running unit tests uncomment these lines then progress to adding in the snippet
    # if r < 0:
    #     raise ValueError("Radius cannot be negative.")

    return pi * r**2


# Will this function work for all values of r?
# An easy way and common testing approach is to create a list with a set of values
# we want to test and then call our function with each of those values using a for loop like so: 
# j in python is the same as i (imaginary) in maths
if __name__ == '__main__':
    radii = [2, 0, -3, 2 + 5j, True, "radius"]
    message = 'Area of circles with r = {radius} is {area}'
    for r in radii:
        A = circle_area(r)
        # format is a function we haven't seen before that fills that values in {} braces with the values of the
        # variable
        print(message.format(radius=r, area=A))
