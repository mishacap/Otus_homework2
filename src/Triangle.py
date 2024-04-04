import math
import Figure

class Triangle(Figure):
    def __init__(self, side_a: int, side_b: int, side_c: int, name):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c