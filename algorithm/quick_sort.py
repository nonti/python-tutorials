def quick_sort(my_arr):
    qshelper(my_arr, 0, len(my_arr) -1)
    return my_arr
def qshelper(my_arr, start, end ):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while right >= left:
        if my_arr[left] > my_arr[pivot] and my_arr[right] < my_arr[pivot]:
            my_arr[left], my_arr[right] = my_arr[right], my_arr[left]
        
        if my_arr[left] <= my_arr[pivot]:
            left += 1
        
        if my_arr[right] >= my_arr[pivot]:
            right -= 1
            
    # swap condition
    my_arr[pivot], my_arr[right] = my_arr[right], my_arr[pivot]
    
    qshelper(my_arr, start, right - 1)
    qshelper(my_arr, right + 1, end)
             
input_list = [3, 7, 2, 1, 6, 4, 5]
output_list = quick_sort(input_list)
print(output_list)