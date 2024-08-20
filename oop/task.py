## take input from a user(name, gae, marks)
# create a class with __init__ method and also create an action method display() to print attribute
# also try to use arguments and parameters with different objects

# n = input('Name: ')
# a = int(input('Age: '))
# m = int(input('Marks: '))

class Student:
    def __init__(self, n, a, **m):
        self.name = n
        self.age = a
        self.marks = m
    
    def display(self):
        print('Hi ', self.name)
        print('Your age is ', self.age)
        print('Your marks are ', self.marks)
          
# s1 = Student('zoe', 25, 95, 65, 78) # m becomes a tuple a single * 
s1 = Student('zoe', 25, science = 75, english = 80, maths = 90) # m becomes a dictionary with double **
s1.display()
print('***********************************')
s1 = Student('kim', 25, science = 65, english = 55, maths = 97) # m becomes a dictionary with double **
s1.display()