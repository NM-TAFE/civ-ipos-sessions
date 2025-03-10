def binary_search(day_to_search, target):
    """
    Binary search that calculates the middle index mid and compares the temperature 
    at index mid with the target temperature.
    # Consider:
    # How can this be applied to a grid data structure
    # What action can we take to resolve the fact it only find the first occurence & disregards the others
    """
    left, right = 0, len(day_to_search)-1

    while left <= right:
        mid_point = (left + right) // 2
        if day_to_search[mid_point] == target:
            return mid_point
        elif day_to_search[mid_point] < target:
            left =  mid_point + 1
        else:
            right = mid_point - 1
        # Note the number of ids printed
        print(id(day_to_search))

temperatures = [17, 21, 22, 22, 23, 23, 24, 25, 25, 25, 24, 23, 22, 21, 20, 19, 18, 18, 17, 16, 16, 15, 14, 13]
print(id(temperatures))

target_temperature = 22
index = binary_search(temperatures, target_temperature)

# If the temperature is not found after the loop, returns -1 to indicate 
# that the temperature is not present in the list of hourly temperatures.
if index != -1:
    print(f"Temperature {target_temperature} found at hour {index + 1}")
else:
    print(f"Temperature {target_temperature} not found in the hourly temperatures")
