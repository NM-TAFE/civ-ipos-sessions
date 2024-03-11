# #example 1
# #!/usr/bin/env python3

# filename = __file__
# # import pdb; pdb.set_trace()
# breakpoint()
# print(f'path = {filename}')


# #example 2
# import os

# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     import pdb; pdb.set_trace()
#     return head


# filename = __file__
# print(f'path = {get_path(filename)}')

# example 3 - n, s, path, l, ll
# import os

# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     return head


# filename = __file__
# import pdb; pdb.set_trace()
# filename_path = get_path(filename)
# print(f'path = {filename_path}')