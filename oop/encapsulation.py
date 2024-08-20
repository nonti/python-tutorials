class Speed:
    def __init__(self):
        self.speed = 10
        # double underscore it is private
        self.__new_speed = 80 # private only accessible in its own class and is modifiable
    def get_new_speed(self): # getter method
        return self.__new_speed
    
    def set_new_speed(self, new_speed): # setter method
        self.__new_speed = new_speed
     
  
s = Speed()
# s.speed = 60
print(s.get_new_speed)
s.set_new_speed(70)

# s.__new_speed = 100
print(s.get_new_speed())
