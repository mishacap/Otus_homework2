from src.Rectangle import Rectangle
from src.Square import Square
import pytest
from datetime import datetime


def test_rectangle_positive_int():
    r = Rectangle(3, 5)
    assert r.get_area() == 15, f"Area should be {3 * 5}"


def test_square_positive_int():
    r = Square(5)
    assert r.get_area() == 25, f"Area should be {5 * 5}"

# def test_rectangle_positive_float():
#         r = Rectangle(3.5, 5.5)
#         assert r.get_area() == 19.25, f"Area should be {3.5 * 5.5}"
