import math

def sum_of_logarithms(n):
    result = 0
    
    for i in range(1, n + 1):
        result += math.log(i)
    return result

n = 5
print(sum_of_logarithms(n))
