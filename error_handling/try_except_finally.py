result = None
x = int(input('NUmber 1:'))
y = int(input('Number 2:'))

try: # Run this code
    result = x / y
except Exception as e: # Execute this code when there is an exception
    print(e)
else: # No exception? run this code
    print('Inside else')
finally: # always run this code
    print('Inside finally')

print('-----New----')
print('Result = ', result)