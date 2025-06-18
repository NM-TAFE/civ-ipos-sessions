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