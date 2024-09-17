def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Define the sorted list and target value
sorted_list = [2, 4, 6, 8, 10, 12, 14]
target = 8

# Call the binary_search function
result = binary_search(sorted_list, target)

# Print the result
print(result)