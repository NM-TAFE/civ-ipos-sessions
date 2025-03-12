def selection_sort(sorted_array):
    """Note the nested loop structure"""
    for index in range(len(sorted_array)):
        current_min_index = index
        for index_to_check in range(index+1, len(sorted_array)):
            if sorted_array[index_to_check] < sorted_array[current_min_index]:
                current_min_index = index_to_check
        sorted_array[index], sorted_array[current_min_index] = sorted_array[current_min_index], sorted_array[index]
    print(id(sorted_array))
    return sorted_array

# Example usage: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
array_to_sort =  [64, 34, 25, 12, 22, 11, 90]
print(id(array_to_sort))
print(selection_sort(array_to_sort))
