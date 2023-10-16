import math


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_area(self):
        area = math.pi * self._radius**2
        return area

