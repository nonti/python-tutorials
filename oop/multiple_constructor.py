class Student:
  # only use on constructor 
  # self is a standard keyword
    def __init__(self, n):
        self.name = n
        print('2nd  __init__ method', self.name)
        
    def display(self):
        print('Hi', self.name)

s1 = Student('zoe')
s1.display()