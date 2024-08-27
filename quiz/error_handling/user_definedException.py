# Python User-Defined Exception Challenge

class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Function to Validate Age:
def validate_age(age):
    try:
        if age < 18:
            raise InvalidAgeError('Age must be 18 or above')
        else:
            print('Age is valid')
    except InvalidAgeError as e:
        print('InvalidAgeError:',e)

validate_age(22)
validate_age(16)