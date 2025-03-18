# class Queue:
#     def __init__(self):
#         self.queue =  []

#     def enqueue(self,item):
#         self.queue.append(item)

#     def dequeue(self):
#         if self.is_empty():
#             return None 
#         else:
#             return self.queue.pop()

#     def peek(self):
#         if self.is_empty():
#             return None 
#         else:
#             return self.queue[0]

#     def is_empty(self):
#         return len(self.queue) == 0
    
# # Example usage:
# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)

# print("Popped item:", my_queue.dequeue())  # Output: Popped item: 3
# print("Popped item:", my_queue.dequeue())  # Output: Popped item: 2


from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def peek(self):
        if not self.is_empty():
            return self.queue[0]  # Return the item at the front without removing it
        else:
            return None  # Return None if the queue is empty
           
    def is_empty(self):
        return len(self.queue) == 0

# Example usage:
my_queue = Queue()
my_queue.queue.append(1)
my_queue.queue.append(2)
my_queue.queue.append(3)
my_queue.queue.extendleft([-1, -2, -3])
my_queue.queue.extend([4,5,6])

print("Popped item:", my_queue.queue.popleft())  # Output: Popped item: 3
print("Popped item:", my_queue.queue.popleft())  # Output: Popped item: 2