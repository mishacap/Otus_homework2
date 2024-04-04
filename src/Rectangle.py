from Figure import class Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b, name):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Нельзя создать прямоугольник")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_b * self.side_b

    def get_perimetr(self):
        return 2 * (self.side_a + self.side_b)

