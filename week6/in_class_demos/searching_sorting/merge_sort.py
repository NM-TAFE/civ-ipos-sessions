def merge_sort(sorted_array):
    if len(sorted_array) > 1:
        # Split the list for further sorting
        mid_point = len(sorted_array) // 2
        split_left = sorted_array[:mid_point]
        split_right = sorted_array[mid_point:]

        merge_sort(split_left)
        merge_sort(split_right)

        left_index = right_index = key = 0

        while left_index < len(split_left) and right_index < len(split_right):
            # Compare the two index items from each array and sort them in the original array
            if split_left[left_index] < split_right[right_index]:
                sorted_array[key] = split_left[left_index]
                left_index += 1
            else:
                sorted_array[key] = split_right[right_index]
                right_index += 1
            key += 1

        while left_index < len(split_left):
            sorted_array[key] = split_left[left_index]
            left_index += 1
            key += 1

        while right_index < len(split_right):
            sorted_array[key] = split_right[right_index]
            right_index += 1
            key += 1
        
    # Note the ids here.
    print(id(sorted_array))
    return sorted_array

# Example usage: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
array_to_sort = [64, 34, 25, 12, 22, 11, 90]
print(id(array_to_sort))
print(merge_sort(array_to_sort))
