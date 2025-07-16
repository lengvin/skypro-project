from src import masks
import pytest


@pytest.mark.parametrize('card_number, result', [
    (7000792289606361, '7000 79** **** 6361'),
    (3928457690236251, '3928 45** **** 6251'),
    ('7000792289606361', '7000 79** **** 6361'),
    (453457, '4534 57** **** '),
    (5432759478037935028938573245, '5432 75** **** 7935'),
    ('', ' ** **** ')
])
def test_card_number(card_number, result):
    assert masks.get_mask_card_number(card_number) == result


@pytest.mark.parametrize('account_number, result', [
    (73654108430135874305, '**4305'),
    (12332489832489834924, '**4924'),
    ('73654108430135874305', '**4305'),
    (47563247562385258724568325, '**8325'),
    (23434342, '**4342'),
    (12, '**12')
])
def test_account_number(account_number, result):
    assert masks.get_mask_account(account_number) == result
