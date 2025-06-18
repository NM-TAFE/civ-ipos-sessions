class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        # check if its empty
        if not self.is_empty():
            # if pop the item of the end
            return self.stack.pop()
        # if it is return nothing
        else: 
            return None

    def is_empty(self):
        return len(self.stack) == 0
    
# Example usage:
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Popped item:", my_stack.pop())  # Output: Popped item: 3
print("Popped item:", my_stack.pop())  # Output: Popped item: 2
