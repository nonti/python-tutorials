result = None
x = int(input('Number1: '))
y = int(input('Number2: '))
try:
	result = x / y
except Exception as e:
    print('Error with our code:', e)
    print(type(e))

print('Result:  ', result)