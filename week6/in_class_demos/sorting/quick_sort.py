def quick_sort(numbers):
    # already sorted
    if len(numbers) <= 1:
        return numbers
    
    # choose a pivot value e.g. the middle element
    pivot_value = numbers[len(numbers) // 2]
    
    # less than pivot
    smaller_than_pivot = [num for num in numbers if num < pivot_value]  

    # equal to pivot
    equal_to_pivot = []     
    for num in numbers:
        if num == pivot_value:
            equal_to_pivot.append(num) 

    # greater than pivot
    greater_than_pivot = []
    
    for num in numbers: 
        if num > pivot_value:
            greater_tahn_pivot.append(num)
    
    # recursion
    return quick_sort(smaller_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

# Example usage: https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/visualize/
print(quick_sort([64, 34, 25, 12, 22, 11, 90]))
