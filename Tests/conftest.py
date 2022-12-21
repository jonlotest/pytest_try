import pytest
from random import randrange
from src.generators.player import Player


@pytest.fixture
def get_player_generator():
    return Player()


@pytest.fixture
def get_number():
    return randrange(1, 100, 5)


def _calc(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture
def calc():
    return _calc


@pytest.fixture
def make_number():
    # print("I'm getting number")
    number = randrange(1, 100, 5)
    yield number
    # print(f"ready {number}")
