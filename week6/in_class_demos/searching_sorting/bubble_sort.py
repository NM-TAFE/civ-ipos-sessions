# Note the nested loop!
def bubble_sort(sorted_array):
    """
    Sorting function which uses a nested loop to compare numbers 
    whilst reading the array from left to right
    """
    number = len(sorted_array)
    for index in range(number):
        # Splits the array in smaller and smaller chunk from left to right
        for chunk in range(0, number-index-1):
            if sorted_array[chunk] > sorted_array[chunk+1]:
                sorted_array[chunk], sorted_array[chunk+1] = sorted_array[chunk+1], sorted_array[chunk]
    print(id(sorted_array))
    return sorted_array

# Example usage: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
array_to_sort = [64, 34, 25, 12, 22, 11, 90]
print(id(array_to_sort))
print(bubble_sort(array_to_sort))
