# Exercise 1a: manually create a 2D data structure

# my_2dim_list = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]

# Random access
# print(my_2dim_list[0])
# print(my_2dim_list[1][2])

print('#'*20)

# Exercise 1b: Be careful when creating 2D data structures using multiplication

# row = [0, 1, 2]
# my_2dim_list = [row] * 3

# print("Before:", my_2dim_list)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# # Update one element in the first row
# my_2dim_list[0][0] = 99
# print(f"Row 1 location: {id(my_2dim_list[0])}")
# print(f"Row 2 location: {id(my_2dim_list[1])}")
# print(f"Row 3 location: {id(my_2dim_list[2])}")

# print("After:", my_2dim_list)   # [[99, 1, 2], [99, 1, 2], [99, 1, 2]] - WHAT!
# print('#'*20)

# Exercise 2: sequential iteration over 2D - aka sequential access

# for row in my_2dim_list:
#     for grid_square in row:
#         # check, change remove, set initial
#         print(grid_square)

# print('#'*20)

# Exercise 3: build a 2D data structure and initialise with values

def make_2d(rows, columns, value=None):
    '''
    Create a rows x cols 2D data structure
    initialised to default or starting value
    Example:
    >>> make_2d(3, 3)
    returns: [[None, None, None], [None, None, None], [None, None, None]]
    '''

    list_2d = []
    for _ in range(rows):
        elems = []
        for _ in range(columns):
            elems.append(value)
        list_2d.append(elems)

    return list_2d


# Exercise 4: Refactor to list comprehension

def make_2d_cool(rows, cols, value=None):
    '''Same function as above implemented as a list comprehension
    Example:
    >>> (make_2d_cool(3, 3, None))
    returns: [[None, None, None], [None, None, None], [None, None, None]]
    '''
    
    # Example 1 - Setting defaults - the first for loop here is on the inside
    return [[value for _ in range(cols)] for _ in range(rows)]

    # Example 2 - add watch statements
    # two_dim_list = []

    # for i in range(rows):
    #     row = [(i + 1) * (j + 1) for j in range(cols)]
    #     two_dim_list.append(row)

    # Example 3
    # This code gives us [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    # two_dim_list = [[(i + 1) * (j + 1) for j in range(cols)] for i in range(rows) ]

    # Activity: Keeping the list comprehension structure how do we change it to give?
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # return two_dim_list

# Exercise 5: list comprehension and navigating a binary data structure

height = 2
width = 2
binary_content = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B"

rgb_values = [
    (binary_content[i], binary_content[i + 1], binary_content[i + 2])
    for i in range(0, 3 * width * height, 3)
]


# Drive the code above...
print('Start','#'*20)

# --- 3 ---
# print(make_2d(3, 3))
# print(make_2d(3, 3, 42))

# print('#'*20)

# --- 4 ----
# print(make_2d_cool(3, 3, None))
# print('#'*20)

# --- 5 ---
print(rgb_values)
# print('#'*20)


# Numpy & Pandas examples - view in Pycharm
# import numpy as np
# import pandas as pd

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# arr2 = arr * 2

# df = pd.DataFrame({
#     'A':[1,2,3],
#     'B':[4,5,6],
#     'C':[7,8,9]
# })

print("END !!!!!", '#'*20)
