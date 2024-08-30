def all_cubes(items):
    result = []
    
    for item in items:
        # result.append(pow(item, 3)) #O(n)
        result = pow(item,3) #O(1) and remove result = []
        
    print(result)
    
items = [2,3,4,5,6,7]
all_cubes(items)