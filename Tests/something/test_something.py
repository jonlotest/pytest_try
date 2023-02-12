import pytest
from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses


# @pytest.mark.skip
@pytest.mark.parametrize('status', [
    *Statuses.list()
])
def test_somthing_01(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


# @pytest.mark.skip
@pytest.mark.parametrize('balance_value', [
    '100',
    '0',
    '-10',
    'qwerty'
])
def test_somthing_02(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


# @pytest.mark.skip
@pytest.mark.parametrize('delete_key', [
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_somthing_03(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


# @pytest.mark.skip
@pytest.mark.parametrize('localizations, loc', [
    ('fr', 'fr_FR')
])
def test_somthing_04(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)
