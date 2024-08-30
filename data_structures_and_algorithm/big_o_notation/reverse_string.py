# write a program to reverse a string

#solution a For loop
def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1
    return s1

input_str = 'kwetsimani'
print('Reverse String: ', reverse_for_loop(input_str))

# solution b while loop
def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 += s[length]
        length -= 1
    return s1

input_str = 'kwetsimani'
print('Reverse String: ', reverse_while_loop(input_str))

#solution c List reverse
def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

input_str = 'kwetsimani'

print('Reverse String: ', reverse_list(input_str))


# solution d recursion
def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]
    
input_str = 'kwetsimani'

print('Reverse Recursion: ', reverse_recursion(input_str))
