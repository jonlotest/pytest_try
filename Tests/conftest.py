import pytest
from random import randrange


@pytest.fixture
def get_number():
    return randrange(1, 100, 5)


def _calc(a, b):
    return a + b


@pytest.fixture
def calc():
    return _calc


@pytest.fixture
def make_number():
    print("I'm getting number")
    number = randrange(1, 100, 5)
    yield number
    print(f"ready {number}")
