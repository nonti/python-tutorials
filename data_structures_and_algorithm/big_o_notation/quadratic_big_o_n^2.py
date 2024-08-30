num_list = [1,2,3,4,5,6,7] #O(n)
num_list2 = [5,6,7,8,9]#O(m)

def randomFunction(num_list):
    total = 0
    
    for num in num_list2:
        for num2 in num_list:
            print(num, num2)
            total += 1
    return total
print(randomFunction(num_list))
        