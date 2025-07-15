from src import masks
from src import widget


def test_card_number(card_number):
    assert masks.get_mask_card_number(7000792289606361) == card_number


def test_account_number(account_number):
    assert masks.get_mask_account(73654108430135874305) == account_number
