from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return  (pow(self.radius,2) * 3.14)    
    
class Square(Shape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return  self.length * self.length
    

Shapes = [Circle(5), Square(5)]

for shape in Shapes:
    print(f"{shape.area()}")