import pytest

from src import generators


def test_filter_by_currency(transactions_example, usd_filtered_transactions, rub_filtered_transactions):
    usd_filter = generators.filter_by_currency(transactions_example, 'USD')
    rub_filter = generators.filter_by_currency(transactions_example, 'RUB')
    eur_filter = generators.filter_by_currency(transactions_example, 'EUR')
    empty_filter = generators.filter_by_currency([], 'USD')
    for i in range(2):
        assert next(usd_filter) == usd_filtered_transactions[i]
        assert next(rub_filter) == rub_filtered_transactions[i]

    assert next(eur_filter) == 'В данном списке нет указанных транзакций'
    assert next(empty_filter) == 'В данном списке нет указанных транзакций'


def test_transaction_descriptions(transactions_example, descriptions_result):
    descriptions = generators.transaction_descriptions(transactions_example)
    empty_descriptions = generators.transaction_descriptions([])
    for i in range(5):
        assert next(descriptions) == descriptions_result[i]

    assert next(descriptions) == 'В списке больше нет транзакций'
    assert next(empty_descriptions) == 'В списке больше нет транзакций'


@pytest.mark.parametrize('start_num, end_num, result', [
    (1, 5, [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
        '0000 0000 0000 0005'
    ]),
    (0, 2, [
        '0000 0000 0000 0000',
        '0000 0000 0000 0001',
        '0000 0000 0000 0002'
    ]),
    (1, 1, [
        '0000 0000 0000 0001'
    ]),
    (9999999999999997, 9999999999999999, [
        '9999 9999 9999 9997',
        '9999 9999 9999 9998',
        '9999 9999 9999 9999'
    ]),
    (9999999999999999, 10000000000000000, [
        'Некорректные крайние значения'
    ])
])
def test_card_number_generator(start_num, end_num, result):
    card_gen = generators.card_number_generator(start_num, end_num)
    assert list(card_gen) == result
