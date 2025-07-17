import pytest

from src import processing


def test_filter_by_state(data_to_filter_by_state):
    for data_lists in data_to_filter_by_state:
        test_list, result, state = data_lists
        assert processing.filter_by_state(test_list, state=state) == result


def test_invalid_data_filter_by_state(invalid_data_to_filter_by_state):
    with pytest.raises(KeyError):
        processing.filter_by_state(invalid_data_to_filter_by_state)


def test_sort_by_date(data_to_filter_by_date):
    for data_lists in data_to_filter_by_date:
        test_list, result, _reversed = data_lists
        assert processing.sort_by_date(test_list, _reverse=_reversed) == result
