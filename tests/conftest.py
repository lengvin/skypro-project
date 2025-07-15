import pytest


@pytest.fixture
def card_number():
    return '7000 79** **** 6361'


@pytest.fixture
def account_number():
    return '**4305'


@pytest.fixture
def card_data():
    return 'Visa Platinum 7000 79** **** 6361'


@pytest.fixture
def account_data():
    return 'Счет **4305'


@pytest.fixture
def date_data():
    return '11.03.2024'
