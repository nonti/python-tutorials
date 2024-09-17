def bubblesort(arr):
    for iter in range(len(arr)):
        for index in range(0, len(arr) -1 - iter):
            if arr[index] > arr[index +1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                # print(arr)

arr = [5, 2, 9, 1, 5, 6]
bubblesort(arr)

print(arr)