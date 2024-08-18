from array import array

class CustomArray:
    def __init__(self, data):
        self.array = array(data)

    def read(self, index):
        # Access an element in the array by index.
        # This operation is O(1) (constant time) because arrays support random access.
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def insert(self, index, value):
        # Inserting an element at a specific index requires shifting elements.
        # This operation is O(n) as we need to shift some or all elements.
        self.array.insert(index, value)

    def delete(self, index):
        # Deleting an element at a specific index also requires shifting elements.
        # This operation is O(n) as we need to shift some or all elements to fill the gap.
        del self.array[index]

    def search(self, value):
        # Searching for a value in an unsorted array typically requires a linear search.
        # This operation is O(n) because it may need to check each element in the array.
        return self.array.index(value)
