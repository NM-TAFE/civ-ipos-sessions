class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        # Get the remainde rof the hash table size and the hash of the key
        return hash(key) % self.size

    def insert(self, key, value):
        #  Set the key as the modules so it fits in the table
        index = self.hash(key)

        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, _) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        # re hash the letter to get the index
        index = self.hash(key)
        # make sure there is a value
        if self.table[index] is not None:
            # unpack and get the value we need
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def remove(self, key):
        # re hash the letter to get the index
        index = self.hash(key)
            # make sure there is a value
        if self.table[index] is not None:
            # make sure to check for any multiple values thet might be stored 
            # in a 2D data strcuture here (list of tuples) - hashing may place mulitple items in a key
            for i, (k, _) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return

# Example usage:
ht = HashTable(10)
ht.insert('a', 1)
ht.insert('b', 2)
ht.insert('c', 3)

print("Value for key 'a':", ht.get('a'))  # Output: Value for key 'a': 1
print("Value for key 'd':", ht.get('d'))  # Output: Value for key 'd': None

# PLace breakpoint and rerun to see duplicated values
ht.remove('b')
print("Value for key 'b' after removal:", ht.get('b'))  # Output: Value for key 'b' after removal: None
