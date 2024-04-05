from math import pi
from Figure import Figure

class Circle(Figure):
    def __init__(self, radius: int):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("Нельзя создать окружность")
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2

    # @property
    def get_perimeter(self):
        return 2 * pi * self.radius