# Python Data Types Challenge

# Given Data:
my_list = [1, 2, 3, 4]
my_tuple = (5, 6, 7, 8)
my_string = "Hello, World!"
my_set = {1, 2, 3, 4}

# 1. Print the third element of the list.
print(my_list[2])
# 2. Print the last element of the tuple.
print(my_tuple[3])
# 3. Print the first three characters of the string.
print(my_string[:3])
# 4. Add a new element '5' to the set.
my_new_set = {5}
print(my_set | my_new_set) # combines my_new_set and my_set
# 5. Create a dictionary with keys as the elements of the list and values as the corresponding elements of the tuple.
my_dict = {1: 5, 2:6, 3:7, 4:8}
print(my_dict)
