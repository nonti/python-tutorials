# Python Big O Complexity Challenge

# 2. Function 'find_element_linear':
def find_element_linear(lst,element):
    for e in lst:
        if e == element:
            return True
    return False
# 3. Function 'get_first_element':
def get_first_element(lst):
     if len(lst) > 0:
         return lst[0]
     return None
# 4. Create a sample list:
sample_list = [1,2,3,4,5]
# 5. Call 'find_element_linear':
print('Linear Search Result:', find_element_linear(sample_list,3))
# 6. Call 'get_first_element':
first_element = get_first_element(sample_list)
if first_element is not None:
    print('First Element:', first_element)
else:
    print('List is empty')