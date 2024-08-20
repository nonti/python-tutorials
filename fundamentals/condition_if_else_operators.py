# Take age from user as input, check if age between 18 and 25. if the condition it true print "you are god to go . else print
# you are not allowed"

age = int(input('what is you age?'))

if age >= 18 and age <= 25:
    print('you are god to go.')
else:
    print('you are not allowed.')

# Take number from user as input, check if number is positive ot negative. if positive then check for odd and even number else be negative
# nested if statement
i = int(input('enter your number'))

if i > 0:
    print('Positive ')
    if i % 2 == 0:
        print('Even number')
    else:
        print('Odd number')
else:
    print('Negative ')
    