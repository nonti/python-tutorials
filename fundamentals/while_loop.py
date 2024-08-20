x = 0

while x < 6:
    print('Current value of x', x)
    x += 1
else:
    print('Loop finished')
    
# Keep taking input from user and print sum of all numbers until user give in put as 0

num = 1
sum = 0

print('Enter a number fot sum, Press 0 to exit')
while num != 0:
    num = int(input('Enter a number: '))
    sum = sum + num
    print('Sum till now:', sum)
else:
    print('Exiting the loop')