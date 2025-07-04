class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        # print(id(self.table), self.table)

    def my_hash(self, key):
        # Get the remainder of the hash table size and the hash of the key
        return hash(key) % self.size

    def insert(self, key, value):
        #  Set the key as the modules so it fits in the table
        index = self.my_hash(key)

        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for item, (k, _) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][item] = (key, value)
                    return
            self.table[index].append((key, value))

    def get(self, key):
        # re hash the letter to get the index
        index = self.my_hash(key)
        # make sure there is a value
        if self.table[index] is not None:
            # unpack and get the value we need
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def remove(self, key):
        # re hash the letter to get the index
        index = self.my_hash(key)
            # make sure there is a value
        if self.table[index] is not None:
            # make sure to check for any multiple values thet might be stored 
            # in a 2D data strcuture here (list of tuples) - hashing may place mulitple items in a key
            for item, (k, _) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][item]
                    return

# Example usage:
hash_table = HashTable(10)
hash_table.insert('a', 17)
hash_table.insert('b', 300.00)
hash_table.insert('c', "Password")
hash_table.insert('d', "AnotherPassword")
hash_table.insert('e', "123564")
hash_table.insert('f', "John Robertson")

print(hash_table)

print("Value for key 'a':", hash_table.get('a'))  # Output: Value for key 'a': 7
print("Value for key 'c':", hash_table.get('c'))  # Output: Value for key 'c': 2

# PLace breakpoint and rerun to see duplicated values
hash_table.remove('b')
print("Value for key 'b' after removal:", hash_table.get('b'))  # Output: Value for key 'b' after removal: None
