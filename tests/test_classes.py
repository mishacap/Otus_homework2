from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest
from datetime import datetime


@pytest.mark.parametrize("rectangle_data_area_1", ["integer", "float"])
def test_area_rectangle_positive(rectangle_data_area, rectangle_data_area_1):
    side_a, side_b, area = rectangle_data_area(data=rectangle_data_area_1)
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area, f"Area should be {side_a * side_b}"


@pytest.mark.parametrize("rectangle_data_perimeter_1", ["integer", "float"])
def test_perimeter_rectangle_positive(rectangle_data_perimeter, rectangle_data_perimeter_1):
    side_a, side_b, perimeter = rectangle_data_perimeter(data=rectangle_data_perimeter_1)
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter() == perimeter, f"Perimeter should be {2 * side_a + 2 * side_b}"


@pytest.mark.parametrize("square_data_perimeter_1", ["integer", "float"])
def test_perimeter_square_positive(square_data_perimeter, square_data_perimeter_1):
    side_a, perimeter = square_data_perimeter(data=square_data_perimeter_1)
    s = Square(side_a)
    assert s.get_perimeter() == perimeter, f"Perimeter should be {4 * side_a}"


@pytest.mark.parametrize("square_data_1", ["integer", "float"])
def test_area_square_positive(square_data, square_data_1):
    side_a, area = square_data(data=square_data_1)
    r = Square(side_a)
    assert r.get_area() == area, f"Area should be {side_a * side_a}"


# def test_rectangle_negative():
#     with pytest.raises(ValueError):
#         Rectangle(-3, 5)

@pytest.mark.parametrize('rectangle_bad_data_1', [
    "side_a is 0",
    "side_b is 0",
    "side_a less than 0",
    "side_b less than 0"])
def test_rectangle_negative(rectangle_bad_data, rectangle_bad_data_1):
    side_a, side_b = rectangle_bad_data(data=rectangle_bad_data_1)
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize("square_bad_data_1", ["side is 0", "side less than 0"])
def test_square_negative(square_bad_data, square_bad_data_1):
    side_a = square_bad_data(data=square_bad_data_1)
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize("circle_bad_data_1", ["radius is 0", "radius less than 0"])
def test_circle_negative(circle_bad_data, circle_bad_data_1):
    radius = circle_bad_data(data=circle_bad_data_1)
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize("triangle_bad_data_1", ["one side is 0", "wrong size of sides"])
def test_triangle_negative(triangle_bad_data, triangle_bad_data_1):
    side_a, side_b, side_c = triangle_bad_data(data=triangle_bad_data_1)
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)

# def test_rectangle_positive_float():
#         r = Rectangle(3.5, 5.5)
#         assert r.get_area() == 19.25, f"Area should be {3.5 * 5.5}"


# def test_square_positive_int():
#     r = Square(5)
#     assert r.get_area() == 25, f"Area should be {5 * 5}"
