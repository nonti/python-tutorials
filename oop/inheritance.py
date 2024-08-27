class Polygon:
    __width = None
    __height = None
    
    def set_value(self, width, height):
        self.__width = width
        self.__height = height
        
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height

class Square(Polygon):
    def area(self):
        return self.get_width() * self.get_height()
    

s = Square()
s.set_value(8, 15)
print(s.area())

class Triangle(Polygon):
    def area(self):
        return  self.get_width() * self.get_height() * 0.5

t = Triangle()
t.set_value(12, 5)
print(t.area())