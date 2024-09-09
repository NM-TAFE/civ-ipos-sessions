# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             return None

#     def is_empty(self):
#         return len(self.stack) == 0

# # Example usage:
# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)

# print("Popped item:", my_stack.pop())  # Output: Popped item: 3
# print("Popped item:", my_stack.pop())  # Output: Popped item: 2

# using deque class
from collections import deque

class Stack:
    def __init__(self):
        # Initialise an empty deque
        self.stack = deque() 

    def is_empty(self):
        # Return True if the stack is empty, otherwise False
        return len(self.stack) == 0  
    
# Example usage:
my_stack = Stack()
my_stack.stack.append(1)
my_stack.stack.append(2)
my_stack.stack.append(3)

print("Popped item:", my_stack.stack.pop())  # Output: Popped item: 3
print("Popped item:", my_stack.stack.pop())  # Output: Popped item: 2