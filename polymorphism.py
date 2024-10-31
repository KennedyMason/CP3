import math
from abc import ABC, abstractmethod # Imports library

# Polymorphism (having many different forms) functions or methods can do multiple things based on given inputs.

class Shape(ABC):   # There wil never be and instance of Shape, so the ABC lets the computer know that an instance of Shape is not possible.
    
    def __init__(self, x):
        self.x = x

    @abstractmethod
    def area(self):
        return 0
    

class Square(Shape):

    def area(self):
        return self.x * self.x
    

class Circle(Shape):

    def area(self):
        return round(math.pi * self.x ** 2, 2)
    

class Rectangle(Shape):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def area(self):
        return self.x * self.y
    

    
shapes = [Square(4), Circle(4), Rectangle(5,3)]

for shape in shapes:
    if isinstance(shape, Shape):
        print(shape.area())


