from src import masks
import pytest


def test_get_mask_card_number(card_numbers):
    for data in card_numbers:
        card_number, result = data
        assert masks.get_mask_card_number(card_number) == result


@pytest.mark.parametrize('invalid_data', [
    453457,
    5432759478037935028938573245,
    0,
    '',
])
def test_invalid_card_number(invalid_data):
    with pytest.raises(ValueError):
        masks.get_mask_card_number(invalid_data)


def test_get_mask_account(account_numbers):
    for data in account_numbers:
        account_number, result = data
        assert masks.get_mask_account(account_number) == result


@pytest.mark.parametrize('invalid_data', [
    47563247562385258724568325,
    23434342,
    0,
    ''
])
def test_invalid_account_number(invalid_data):
    with pytest.raises(ValueError):
        masks.get_mask_account(invalid_data)
