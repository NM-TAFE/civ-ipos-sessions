class Queue:
    def __init__(self):
        self.queue = []
	
    def enqueue(self, item):
        self.queue.append(item)
		
    def dequeue(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]  # Return the item at the front without removing it
        else:
            return None  # Return None if the queue is empty
		
    def is_empty(self):
        return len(self.queue) == 0
