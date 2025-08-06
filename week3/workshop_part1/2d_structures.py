# Exercise 1: manually create a 2D data structure
# my_2dim_list = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]

# # random access
# print(my_2dim_list[0])
# print(my_2dim_list[1][2])

# Exercise 2: sequential iteration over 2D - aka sequential access
# for row in my_2dim_list:
#     for grid_square in row:
#         # check, change remove, set initial
#         print(grid_square)

# Exercise 3: build a 2D data structure and initialise with values
def make_2d(rows, columns, value=None):
    '''
    # Create a rows x cols 2D data structure
    # initialised to default or starting value
    # Example:
    # >>> make_2d(3, 3)
    # returns: [[None, None, None], [None, None, None], [None, None, None]]
    '''
    list_2d = []
    for _ in range(rows):
        elems = []
        for _ in range(columns):
            elems.append(value)
        list_2d.append(elems)

    return list_2d


# Exercise 3a: Refactor to list comprehension
def make_2d_cool(rows, cols, value=None):
    '''Same function as above implemented as a list comprehension
    '''
    # Example 1
    # return [[value for _ in range(cols)] for _ in range(rows)]

    two_dim_list = []

    # Example 2 - add watch statements
    # for i in range(rows):
    #     row = [(i + 1) * (j + 1) for j in range(cols)]
    #     two_dim_list.append(row)

    # Example 3
    # This code gives us [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    two_dim_list = [[(i + 1) * (j + 1) for j in range(cols)] for i in range(rows) ]

    # Keeping the list comprehension structure how do we change it to give:
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    return two_dim_list

# Drive the code above...
# print('#'*20)
#--- 3 ---
# print(make_2d(3, 3))
# print(make_2d(3, 3, 42))

# print('#'*20)
# --- 3a ----
print(make_2d_cool(3, 3, None))
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

# print()

