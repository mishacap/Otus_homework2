import pytest


@pytest.fixture()
def rectangle_data():
    side_a, side_b, area = 3, 5, 15

    yield side_a, side_b, area

    print("\n Down")