#!/usr/bin/python3
"""Task 2 Duck typing"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Class Shape"""

    @abstractmethod
    def area(self):
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass


class Circle(Shape):
    """Class Circle"""

    def __init__(self, radius):
        """Initiate radius"""
        self.radius = radius

    def area(self):
        """Area circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Perimeter Circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Initiate width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Area rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Perimeter rectangle"""
        return 2 * (self.height + self.width)


def shape_info(shape):
    """Duck Typing"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
