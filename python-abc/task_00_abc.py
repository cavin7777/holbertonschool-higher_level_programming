from abc import ABC, abstractmethod

"""
Animal
"""


class Animal(ABC):
    """
    Animal Class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"
