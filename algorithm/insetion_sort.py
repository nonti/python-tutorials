def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        last = i - 1
        
        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last = last - 1
        
        arr[last + 1] = key

arr = [7, 2, 4, 1, 5, 3]
insertion_sort(arr)

print(arr)