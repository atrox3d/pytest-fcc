from source.shapes import Shape


import math


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius


    def area(self):
        return math.pi * self.radius **2

    def perimeter(self):
        return math.pi * 2 * self.radius