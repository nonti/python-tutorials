# Python Abstract Class Challenge
from abc import ABC, abstractmethod
import math
# 1. Abstract Class:
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
# 2. Concrete Class: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
# 3. Concrete Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * self.radius**2

# 4. Create instances:
rectangle = Rectangle(5, 10)
circle = Circle(7)
print(rectangle.calculate_area())
print(circle.calculate_area())