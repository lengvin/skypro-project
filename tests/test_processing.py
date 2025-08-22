import pytest

from src import processing


def test_filter_by_state(data_to_filter_by_state: list) -> None:
    for data_lists in data_to_filter_by_state:
        test_list, result, state = data_lists
        assert processing.filter_by_state(test_list, state=state) == result


def test_sort_by_date(data_to_filter_by_date: list) -> None:
    for data_lists in data_to_filter_by_date:
        test_list, result, _reversed = data_lists
        assert processing.sort_by_date(test_list, _reverse=_reversed) == result


@pytest.mark.parametrize('search_string', [
    'перевод',
    'открытие',
    'вклад'
])
def test_process_bank_search(search_string, transactions_example):
    result = processing.process_bank_search(transactions_example, search_string)
    for transaction in result:
        assert search_string in transaction['description'].lower()


def test_process_bank_operations(transactions_example, categories, categories_result):
    assert processing.process_bank_operations(transactions_example, categories) == categories_result
