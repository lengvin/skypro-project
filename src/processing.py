from widget import get_date


def filter_by_state(list_of_data: list, state: str = "EXECUTED") -> list:
    """
    фильтрация данных по значению ключа state
    """
    filtered_list = []
    for data in list_of_data:
        if data["state"] == state:
            filtered_list.append(data)

    return filtered_list


def sort_by_date(list_of_data: list, _reverse: bool = True) -> list:
    """
    фильтрация данных по дате
    """
    key_to_sort = lambda x: int("".join(reversed(get_date(x["date"]).split("."))))
    sorted_list = sorted(list_of_data, key=key_to_sort, reverse=_reverse)

    return sorted_list
