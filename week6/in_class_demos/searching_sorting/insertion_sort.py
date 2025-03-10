def insertion_sort(sorted_array):
    """
    NOte: The nested loop structure and how is differs through the use of while
    How the simple len() and range() methods combine to make a powerful mechanism"
    """
    # Outerloop moves up each item in the array
    for index in range(1, len(sorted_array)):
        key = sorted_array[index]
        # We create a new indexing variable to check the item before  
        # and continue to movethe item down if is smaller
        sorting_index = index - 1
        while sorting_index >= 0 and key < sorted_array[sorting_index]:
            sorted_array[sorting_index + 1] = sorted_array[sorting_index]
            sorting_index -= 1
        sorted_array[sorting_index + 1] = key
    print(id(sorted_array))
    return sorted_array

# Example usage: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
array_to_sort = [28,42,37,11,77,93,97,8]
print(id(array_to_sort))
print(insertion_sort(array_to_sort))
