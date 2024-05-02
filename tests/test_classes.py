from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest
from math import pi
from math import sqrt
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


@pytest.mark.parametrize("square_data_area_1", ["integer", "float"])
def test_area_square_positive(square_data_area, square_data_area_1):
    side_a, area = square_data_area(data=square_data_area_1)
    s = Square(side_a)
    assert s.get_area() == area, f"Area should be {side_a * side_a}"


@pytest.mark.parametrize("square_data_perimeter_1", ["integer", "float"])
def test_perimeter_square_positive(square_data_perimeter, square_data_perimeter_1):
    side_a, perimeter = square_data_perimeter(data=square_data_perimeter_1)
    s = Square(side_a)
    assert s.get_perimeter() == perimeter, f"Perimeter should be {4 * side_a}"


@pytest.mark.parametrize("circle_data_area_1", ["integer", "float"])
def test_area_circle_positive(circle_data_area, circle_data_area_1):
    radius, area = circle_data_area(data= circle_data_area_1)
    c = Circle(radius)
    assert c.get_area() == area, f"Area should be {pi * radius ** 2}"


@pytest.mark.parametrize("circle_data_perimeter_1", ["integer", "float"])
def test_perimeter_circle_positive(circle_data_perimeter, circle_data_perimeter_1):
    radius, perimeter = circle_data_perimeter(data=circle_data_perimeter_1)
    c = Circle(radius)
    assert c.get_perimeter() == perimeter, f"Perimeter should be {2 * pi * radius}"


@pytest.mark.parametrize("triangle_data_area_1", ["integer", "float"])
def test_area_triangle_positive(triangle_data_area, triangle_data_area_1):
    side_a, side_b, side_c, area = triangle_data_area(data=triangle_data_area_1)
    s = Triangle(side_a, side_b, side_c)
    p = (side_a + side_b + side_c) / 2
    assert s.get_area() == area, f"Area should be {sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))}"


@pytest.mark.parametrize("triangle_data_perimeter_1", ["integer", "float"])
def test_perimeter_triangle_positive(triangle_data_perimeter, triangle_data_perimeter_1):
    side_a, side_b, side_c, area = triangle_data_perimeter(data=triangle_data_perimeter_1)
    p = Triangle(side_a, side_b, side_c)
    assert p.get_perimeter() == area, f"Perimeter should be {side_a + side_b + side_c}"

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
