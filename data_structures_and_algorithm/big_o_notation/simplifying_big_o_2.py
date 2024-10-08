num_list = [1,2,3,4,5,6,7]

def randomFunction(num_list):
    total = 0 #O(1)
    all_integer = True #O(1)
    
    for num in num_list:
        print(num) #O(n)
    
    for num1 in num_list:
        for num2 in num_list:
            print(num1, num2) #O(n^2)
            total += 1 #O(n^2)
    
    msg = 'Rule 5- Remove all non dominants' #O(1)
    return total #O(1)
print(randomFunction(num_list)) #O(4 +n + 2n^2) =>  (n^2)