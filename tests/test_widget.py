from src import widget


def test_mask_account_card(card_data, account_data):
    assert widget.mask_account_card('Visa Platinum 7000792289606361') == card_data
    assert widget.mask_account_card('Счет 73654108430135874305') == account_data


def test_get_date(date_data):
    assert widget.get_date('2024-03-11T02:26:18.671407') == date_data
