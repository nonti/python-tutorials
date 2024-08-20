class Student:
    def __init__(self): # internally defined 
        self.name = 'nonty'
        self.age = 25
        self.mark = 88    
        # print('__init__ is called') 
        
        #talk is an instance method   
    def talk(self): # self refers to  
      print('Name -', self.name)
      print('Age -', self.age)
      print('Mark -', self.mark)

s1 = Student() # constructor 
s1.name = 'zoe'
print(s1.name)
s1.talk()

s2 = Student()
print(s2.name)
