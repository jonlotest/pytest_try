import pytest
from src.baseclasses.response import Response
from src.schemas.user import User
from src.schemas.computer import Computer
from examples import computer


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    # print(make_number)


@pytest.mark.development
@pytest.mark.production
@pytest.mark.skip('Skip this test')
def test_another():
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('a', 2, None),
    ('a', 'b', None)
])
def test_calculator(first_value, second_value, result, calc):
    assert calc(first_value, second_value) == result


@pytest.mark.development
@pytest.mark.production
def test_another_wrong():
    assert 1 == 1


def test_pydantic_object():
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.physical.color.as_hex())
