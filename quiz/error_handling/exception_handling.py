import math

def calculate_square_root(number):
    try:
        value = float(number)
        if value < 0:
            raise ValueError('Invalid input. Please enter a positive number.')

    except ValueError as e:
        if 'could not convert' in str(e):
            return 'Invalid input. Please enter a valid number.'
        return str(e)

    return math.sqrt(value)


result1 = calculate_square_root(9)
print('Result 1:',result1)
result2 = calculate_square_root('abc')
print('Result 2: ', result2)
result3 = calculate_square_root(-4)
print('Result 3: ', result3)