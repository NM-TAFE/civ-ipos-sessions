import bisect

# Example of Python sorting
unsorted_list = [5, 2, 7, 1, 9, 3]
sorted_list = sorted(unsorted_list)
print("Sorted list:", sorted_list)  # Result: [1, 2, 3, 5, 7, 9]

# Example of using the bisect module
# Inserting a new element into a sorted list (in order)
bisect.insort(sorted_list, 6)
print("Sorted list after insertion:", sorted_list) # Result: [1, 2, 3, 5, 6, 7, 9]

# Performing binary search in a sorted list
# Retrun the index of the item to be found(if found)
index = bisect.bisect_left(sorted_list, 5) # Result:  3
print("Index of 5 in the sorted list:", index)
