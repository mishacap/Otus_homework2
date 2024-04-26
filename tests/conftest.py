import pytest


@pytest.fixture()
def rectangle_data_area():

    def _wrapper(data: str):
        if data == "integer":
            return 3, 5, 15
        if data == "float":
            return 3.5, 5.5, 19.25

    yield _wrapper


@pytest.fixture()
def rectangle_data_perimeter():

    def _wrapper(data: str):
        if data == "integer":
            return 6, 7, 26
        if data == "float":
            return 8.2, 9.4, 35.2

    yield _wrapper


@pytest.fixture()
def square_data_perimeter():

    def _wrapper(data: str):
        if data == "integer":
            return 10, 40
        if data == "float":
            return 11.4, 45.6

    yield _wrapper


@pytest.fixture()
def square_data_area():

    def _wrapper(data: str):
        if data == "integer":
            return 5, 25
        if data == "float":
            return 3.5, 12.25

    yield _wrapper


@pytest.fixture()
def circle_data_area():

    def _wrapper(data: str):
        if data == "integer":
            return 10, 314.16
        if data == "float":
            return 12.3, 475.29

    yield _wrapper


@pytest.fixture()
def circle_data_perimeter():
    def _wrapper(data: str):
        if data == "integer":
            return 13, 81.68
        if data == "float":
            return 14.8, 92.89

    yield _wrapper

    def _wrapper(data: str):
        if data == "integer":
            return 10, 314.16
        if data == "float":
            return 12.3, 475.29

    yield _wrapper


@pytest.fixture()
def rectangle_bad_data():

    def _wrapper(data: str):
        if data == "side_a is 0":
            return 0, 1
        if data == "side_b is 0":
            return 2, 0
        if data == "side_a less than 0":
            return -1, 3
        if data == "side_b less than 0":
            return 4, -2

    yield _wrapper


@pytest.fixture()
def square_bad_data():

    def _wrapper(data: str):
        if data == "side is 0":
            return 0
        if data == "side less than 0":
            return -1

    yield _wrapper



@pytest.fixture()
def circle_bad_data():

    def _wrapper(data: str):
        if data == "radius is 0":
            return 0
        if data == "radius less than 0":
            return -1

    yield _wrapper

@pytest.fixture()
def triangle_bad_data():

    def _wrapper(data: str):
        if data == "one side is 0":
            return 0, 5, 6
        if data == "wrong size of sides":
            return 3, 4, 10

    yield _wrapper
