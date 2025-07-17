import pytest

from src import widget


def test_mask_account_card(bank_cards):
    for card_data in bank_cards:
        card, result = card_data
        assert widget.mask_account_card(card) == result


@pytest.mark.parametrize('invalid_data', [
    'Maestro7000792289606361',
    'Счет45930725495749350875',
    'VisaPlatinum7000792289606361',
    'Maestro',
    7000792289606361
])
def test_invalid_account_card(invalid_data):
    with pytest.raises(ValueError):
        widget.mask_account_card(invalid_data)


def test_get_date(date_examples):
    for date_data in date_examples:
        data, result = date_data
        assert widget.get_date(data) == result


@pytest.mark.parametrize('invalid_data', [
    '2025-06-2402:26:18.671407',
    'T02:26:18.671407',
    '2025-6-4T02:26:18.671407'
])
def test_invalid_date(invalid_data):
    with pytest.raises(ValueError):
        widget.get_date(invalid_data)
