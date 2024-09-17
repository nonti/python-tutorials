def  merge_sort(my_arr):
    if(len(my_arr)) == 1:
        return my_arr
    
    middle = len(my_arr) // 2
    left_half = my_arr[:middle]
    print(left_half)
    right_half = my_arr[middle:]
    
    left_result = merge_sort(left_half)
    right_result = merge_sort(right_half)
    
    return merge(left_result, right_result)

def merge(left_result, right_result):
    result = [None] * (len(left_result) + len(right_result))
    x = j = k = 0
    
    while x < len(left_result) and j < len(right_result):
        if left_result[x] <= right_result[j]:
            result[k] = left_result[x]
            x += 1
        else:
            result[k] = right_result[j]
            j += 1
        k += 1
        
    while x < len(left_result):
        result[k] = left_result[x]
        x += 1
        k += 1
        
    while j < len(right_result):
        result[k] = right_result[j]
        j += 1
        k += 1
        
    return result

input_list = [3, 7, 2, 1, 6, 4, 5]
input_list[:] = merge_sort(input_list)  # Modify the original list in place
print(input_list) 
        