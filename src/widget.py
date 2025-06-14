import masks


def mask_account_card(card_data: str) -> str:
    """
    обработка информации о картах и о счетах
    """
    card_data_elements = card_data.split()
    if card_data_elements[0] == 'Счет':
        card_data_elements[-1] = masks.get_mask_account(int(card_data_elements[-1]))
    else:
        card_data_elements[-1] = masks.get_mask_card_number(int(card_data_elements[-1]))
    result = ' '.join(card_data_elements)

    return result
