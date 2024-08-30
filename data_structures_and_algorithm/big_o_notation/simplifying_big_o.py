# Simplify Big O
""" 1. focus on scalability n -> infinity ∞
2. consdering worst case scenario
3. remove all possible constants
4. consider different variable for different inputs
5. remove all non-dominants """

# TODO: Number 4 

num_list = [1,2,3,4,5,6,7]
char_list = ['a','b','c','d','e','f']

def randomFunction(num_list, char_list):
    for num in num_list:
        print(num)#O(n)
    for char in char_list:
        print(char)#O(m)
print(randomFunction(num_list, char_list))#O(n + m)


def randomFunction(num_list):
    for num in num_list:
        print(num)#O(n)
    for num in num_list:
        print(num)#O(n)
print(randomFunction(num_list))#O(n + n)


# Number  5
def randomFunction(num_list):
    total = 0
    all_integer = True
    
    for num in num_list:
        print(num)
    for num1 in num_list:
        for num2 in num_list:
            print(num1, num2)
            total += 1
    msg = 'Rule 5- Remove all non dominants'
    return total
print(randomFunction(num_list))
