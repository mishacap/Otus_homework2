from math import pi
from src.Figure import Figure

class Circle(Figure):
    def __init__(self, radius: int):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("Circle cannot be created")
        self.radius = radius

    def get_area(self):
        return round(pi * self.radius ** 2, 2)

    # @property
    def get_perimeter(self):
        return round(2 * pi * self.radius, 2)