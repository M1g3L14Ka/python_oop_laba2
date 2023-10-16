import math


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_area(self):
        area = math.pi * self._radius**2
        return area

    def get_circumference(self):
        circumference = 2 * math.pi * self._radius
        return circumference

