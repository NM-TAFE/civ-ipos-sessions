# Exercise 1: manually create a 2D data structure
#        elem    0  1  2      row
my_2dim_list = [[0,1,2],  #0
                [4,5,6],  #1
                [7,8,9]   #2
]

print(my_2dim_list[0])
print(my_2dim_list[0][0])


# Exercise 2:
# sequential iteration over 2D
for row in my_2dim_list:
    for elem in row:
        print(elem, end=' ')
    print()


# Exercise 3:
# Dynamically build a 2D data structure and initialise with values
def make_2d(rows, cols, value=None):
    '''Create a rows x cols 2D data structure
    initialised to _value_
    Example:
    >>> make_2d(3, 3)
    [[None, None, None], [None, None, None], [None, None, None]]
    '''
    list_2d = []
    for _ in range(rows):
        elems = []
        for _ in range(cols):
            elems.append(value)
        list_2d.append(elems)
    return list_2d



# Exercise 3a:
# Refactor to list comprehension
def make_2d_cool(rows, cols, value=None):
    '''Same function as above implemented as a list comprehension
    '''
    # Example 1
    # return [[value for _ in range(cols)]
    #             for _ in range(rows) ]

    # two_dim_list = []

    # # Example 2 - add watch statements
    # for i in range(rows):
    #     row = [(i+1)*(j+1)for j in range(cols)]
    #     two_dim_list.append(row)

    # return two_dim_list


    # Example 3
    two_dim_list =  [[(i+1)*(j+1) for j in range(cols)] for i in range(rows)]

    # # Example 4
    # w, h = 3, 3

    # two_dim_list = [[None for _ in range(w)] for _ in range(h)]

    # print(two_dim_list)
    return two_dim_list

# Drive the code above...
# print('#'*50)
# print(make_2d_cool(3, 3, 11))
# print('#'*50)
# print(make_2d(3, 3, 42))
# print(make_2d(3, 3))

# Optional
# correct answer to initialising a list with sequential values

## Numpy & Pandas examples
# import numpy as numpy

# arr = np.array([1,2,3],[4,5,6],[7,8,9])

# arr2 = arr * 2

# import pandas as pandas

# df = pd.DataFrame({
#     'A':[1,2,3],
#     'B':[4,5,6],
#     'C':[7,8,9]
# })