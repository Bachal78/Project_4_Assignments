"""Use the abc module to create an abstract class Shape with an abstract method area().
Inherit a class Rectangle that implements area()."""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

# Example
r = Rectangle(4, 5)
print(r.area())
