from src import widget
from collections import Counter
import re


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
    key_to_sort = lambda x: int("".join(reversed(widget.get_date(x["date"]).split("."))))
    sorted_list = sorted(list_of_data, key=key_to_sort, reverse=_reverse)

    return sorted_list


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    фильтрация данных по строке в описании
    """
    result = []
    for transaction in data:
        if re.search(search, transaction.get('description'), flags=re.IGNORECASE):
            result.append(transaction)

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    подсчет количества транзакций по категориям
    """
    descriptions = []
    unfounded = []
    for transaction in data:
        if transaction.get('description') in categories:
            descriptions.append(transaction.get('description'))

    return Counter(descriptions)
