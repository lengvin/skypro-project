import pytest


@pytest.fixture
def card_numbers() -> list:
    return [
        (7000792289606361, "7000 79** **** 6361"),
        (3928457690236251, "3928 45** **** 6251"),
        (5495759023457075, "5495 75** **** 7075"),
    ]


@pytest.fixture
def account_numbers() -> list:
    return [(73654108430135874305, "**4305"),
            (12332489832489834924, "**4924"),
            (53454358794538978775, "**8775")]


@pytest.fixture
def bank_cards() -> list:
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 45930725495749350875", "Счет **0875"),
    ]


@pytest.fixture
def date_examples() -> list:
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-11-19T02:26:18.671407", "19.11.2023"),
        ("2025-06-24T02:26:18.671407", "24.06.2025"),
    ]


@pytest.fixture
def data_to_filter_by_state() -> list:
    test_list_1 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    test_list_2 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]
    test_list_3 = [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result_executed_state_1 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    result_executed_state_2 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result_executed_state_3 = []
    result_canceled_state_1 = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    result_canceled_state_2 = []
    result_canceled_state_3 = [
        {"id": 41428829, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    return [
        (test_list_1, result_executed_state_1, "EXECUTED"),
        (test_list_2, result_executed_state_2, "EXECUTED"),
        (test_list_3, result_executed_state_3, "EXECUTED"),
        (test_list_1, result_canceled_state_1, "CANCELED"),
        (test_list_2, result_canceled_state_2, "CANCELED"),
        (test_list_3, result_canceled_state_3, "CANCELED"),
        ([], [], "EXECUTED"),
        ([], [], "CANCELED"),
    ]


@pytest.fixture
def invalid_data_to_filter_by_state() -> list:
    list_without_state = [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]

    return list_without_state


@pytest.fixture
def data_to_filter_by_date() -> list:
    test_list_1 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    test_list_2 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2025-08-12T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2023-03-13T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2023-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2025-10-14T08:21:33.419441"},
    ]
    test_list_3 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2020-06-23T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2020-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2020-09-11T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2021-10-14T08:21:33.419441"},
    ]
    result_1 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    result_2 = [
        {"id": 615064591, "state": "CANCELED", "date": "2025-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2025-08-12T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2023-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2023-03-13T02:08:58.425572"},
    ]
    result_3 = [
        {"id": 615064591, "state": "CANCELED", "date": "2021-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2020-09-11T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2020-06-30T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "2020-06-23T18:35:29.512364"},
    ]
    reversed_result_1 = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    reversed_result_2 = [
        {"id": 939719570, "state": "EXECUTED", "date": "2023-03-13T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2023-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2025-08-12T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2025-10-14T08:21:33.419441"},
    ]
    reversed_result_3 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2020-06-23T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2020-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2020-09-11T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2021-10-14T08:21:33.419441"},
    ]
    nonstandard_list_1 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    nonstandard_result_1 = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    reversed_nonstandard_result_1 = [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
    ]
    return [
        (test_list_1, result_1, True),
        (test_list_2, result_2, True),
        (test_list_3, result_3, True),
        (test_list_1, reversed_result_1, False),
        (test_list_2, reversed_result_2, False),
        (test_list_3, reversed_result_3, False),
        ([], [], True),
        ([], [], False),
        (nonstandard_list_1, nonstandard_result_1, True),
        (nonstandard_list_1, reversed_nonstandard_result_1, False),
    ]


@pytest.fixture
def transactions_example():
    transactions = (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )
    return transactions


@pytest.fixture
def usd_filtered_transactions():
    expected_result = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]

    return expected_result


@pytest.fixture
def rub_filtered_transactions():
    expected_result = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]

    return expected_result


@pytest.fixture
def descriptions_result():
    return [
        'Перевод организации',
        'Перевод со счета на счет',
        'Перевод со счета на счет',
        'Перевод с карты на карту',
        'Перевод организации'
    ]
