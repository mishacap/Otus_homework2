from src.Rectangle import Rectangle
    
    
class Square(Rectangle):
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError("Square cannot be created")
        super().__init__(side_a, side_a)
