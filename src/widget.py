from src import masks


def mask_account_card(card_data: str) -> str:
    """
    обработка информации о картах и о счетах
    формат аргумента должен быть: 'карта/Счет + номер карты'
    """
    if isinstance(card_data, str):
        card_data_elements = card_data.split()
        if card_data_elements[0] == "Счет":
            card_data_elements[-1] = masks.get_mask_account(int(card_data_elements[-1]))
        else:
            card_data_elements[-1] = masks.get_mask_card_number(int(card_data_elements[-1]))
        result = " ".join(card_data_elements)

        return result
    else:
        raise ValueError("формат аргумента должен быть: 'карта/Счет + номер карты'")


def get_date(full_date: str) -> str:
    """
    получение даты в формате ДД.ММ.ГГГГ
    формат аргумента должен быть: 'ГГГГ-ММ-ДДT(другие данные)'
    """
    if isinstance(full_date, str) and 'T' in full_date:
        date_parts = full_date.split("T")

        if bool(date_parts[0]):
            date = date_parts[0].split("-")
            date.reverse()

            if len(date[0]) == 2 and len(date[1]) == 2 and len(date[2]) == 4:
                result = ".".join(date)

                return result
            else:
                raise ValueError('Аргумент должен начиться с даты в формате ГГГГ-ММ-ДДT')
        else:
            raise ValueError('Аргумент должен начиться с даты в формате ГГГГ-ММ-ДДT')
    else:
        raise ValueError('Аргумент должен начиться с даты в формате ГГГГ-ММ-ДДT')
