from abc import ABC, abstractmethod

"""
Shape
"""


class Shape(ABC):
    """
    Class Shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Class Circle
    """
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

def shape_info(thing):
    print("Area:", thing.area())
    print("Perimeter:", thing.perimeter())
