from collections import deque

class Queue:
    def __init__(self):
        self.queue= deque()

    def peek(self):
        if not self.is_empty():
            return self.queue[0] # Return the item at the front without removing it
        else:
            return None# Return None if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0
    
class Stack:
    def __init__(self):
        self.stack= deque()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None# Return None if the queue is empty
    
    def is_empty(self):
        return len(self.stack) == 0

# Example usage:
my_queue =Queue()
my_stack =Stack()
my_queue.queue.append(1)
my_stack.stack.append(2)
# my_queue.queue.append(3)
my_queue.queue.extendleft([-1, -2, -3])
my_stack.stack.extend([4,5,6])

my_queue

print("Popped item:", my_stack.stack.pop()) # Output: Popped item: 3
print("Popped item:", my_queue.queue.popleft()) # Output: Popped item: 2    