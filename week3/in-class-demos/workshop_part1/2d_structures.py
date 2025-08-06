
#
# # Exercise 1: manually create a 2D data structure
# #        elem    0  1  2      row
#
# # my_2dim_list = [
# #     [0, 1, 2],
# #     [3, 4, 5],
# #     [6, 7, 8]
# # ]
#
# # 0 1 2
# # 3 4 5
# # 6 7 8
#
# # random
# # print(my_2dim_list[0])
# # print(my_2dim_list[1][2])
#
#
# # Exercise 2:
# # sequential iteration over 2D
# for row in my_2dim_list:
#     for grid_square in row:
#         # check, change remove, set initial
#         print(grid_square)
# #
# # # Example of a 4D list (list of list of list of lists)
# # data = [
# #     [
# #         [
# #             [1, 2], [3, 4]
# #         ],
# #         [
# #             [5, 6], [7, 8]
# #         ]
# #     ],
# #     [
# #         [
# #             [9, 10], [11, 12]
# #         ],
# #         [
# #             [13, 14], [15, 16]
# #         ]
# #     ]
# # ]
# #
# # # Traversing through the 4D list
# # for i in range(len(data)):
# #     for j in range(len(data[i])):
# #         for k in range(len(data[i][j])):
# #             for l in range(len(data[i][j][k])):
# #                 print(f"data[{i}][{j}][{k}][{l}] = {data[i][j][k][l]}")
#
# # # 4D structure: List of Dicts -> List -> Dict -> Values
# data = [
#     {
#         "group1": [
#             {"id": 1, "value": "A"},
#             {"id": 2, "value": "B"}
#         ],
#         "group2": [
#             {"id": 3, "value": "C"},
#             {"id": 4, "value": "Team Lead"}
#         ]
#     },
#
#     {
#         "group3": [
#             {"id": 5, "value": "E"},
#             {"id": 6, "value": "F"}
#         ],
#         "group4": [
#             {"id": 7, "value": "G"},
#             {"id": 8, "value": "Team Lead"}
#         ]
#     }
# ]
# #
# # # Traversing the 4D structure
# # for i, dictionary in enumerate(data):
# #     for key, sublist in dictionary.items():
# #         for j, subdict in enumerate(sublist):
# #             for sub_key, value in subdict.items():
# #                 print(f"data[{i}]['{key}'][{j}]['{sub_key}'] = {value}")
#
#
# # Exercise 3:
# # Dynamically build a 2D data structure and initialise with values
# def make_2d(rows, columns, value=None):
#     '''Create a rows x cols 2D data structure
#     initialised to _value_
#     Example:
#     # >>> make_2d(3, 3)
#     [[None, None, None], [None, None, None], [None, None, None]]
#     '''
#     list_2d = []
#     for _ in range(rows):
#         elems = []
#         for _ in range(columns):
#             elems.append(value)
#         list_2d.append(elems)
#
#
# # Exercise 3a:
# # Refactor to list comprehension
# def make_2d_cool(rows, cols, value=None):
#     '''Same function as above implemented as a list comprehension
#     '''
#     # Example 1
#     # return [[value for _ in range(cols)]
#     #         for _ in range(rows)]
#     # two_dim_list = []
#
#     # # Example 2 - add watch statements
#     # for i in range(rows):
#     #     row = [(i + 1) * (j + 1) for j in range(cols)]
#     #     two_dim_list.append(row)
#     # Example 3
#     two_dim_list = [[(i + 1) * (j + 1) for j in range(cols)] for i in range(rows) ]
#
#     return two_dim_list
#
#     # Example 3
#
#     # Example 4
#
# # Drive the code above...
# # print('#'*50)
# print(make_2d_cool(3, 3, None))
# # print('#'*50)
# # print(make_2d(3, 3, 42))
# # print(make_2d(3, 3))
#

# Numpy & Pandas examples - view in Pycharm
import numpy as np
import pandas as pd

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2 = arr * 2

df = pd.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
})

print()

