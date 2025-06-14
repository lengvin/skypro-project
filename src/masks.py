def get_mask_card_number(card_number: int) -> str:
    """
    создание маски по номеру карты
    """
    str_card_number = str(card_number)
    list_number = []
    for i in range(4):
        list_number.append(str_card_number[i * 4: (i * 4) + 4])

    list_number[2] = "****"
    list_number[1] = list_number[1][0:2] + "**"
    result = " ".join(list_number)

    return result


def get_mask_account(check_number: int) -> str:
    """
    создание маски по номеру счёта
    """
    str_check_number = str(check_number)
    last_digits = str_check_number[-4::]
    result = "**" + last_digits

    return result
