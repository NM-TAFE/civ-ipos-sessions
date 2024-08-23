# # example 1
# #!/usr/bin/env python3

# filename = __file__
# import pdb; pdb.set_trace()
# breakpoint()
# print(f'path = {filename}')


# #example 2
# l (list): Display the source code around the current line.
# p head: Print the value of head.
# p tail: Print the value of tail.
# n: Move to the next line in the current function.
# r (return): Continue execution until the current function returns.

# import os

# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     breakpoint()
#     head, tail = os.path.split(filename)
#     import pdb; pdb.set_trace()

#     return head


# filename = __file__
# print(f'path = {get_path(filename)}')

# # example 3
# n: Step to the next line in the current scope.
# s: Step into the get_path function.
# p head, p tail: Print the current value of head and tail.
# c: Continue running the script until the next breakpoint or the end of the program.
# ll: Long listing of the current function, displaying the entire source code for context.
# q: Quit the debugger.

# import os

# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     return head


# import pdb; pdb.set_trace()
# filename = __file__
# filename_path = get_path(filename)
# print(f'path = {filename_path}')