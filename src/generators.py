def filter_by_currency(list_of_transactions, currency):
    """
    Итератор, сортирующий транзакции по валюте
    """
    for transaction in list_of_transactions:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(list_of_transactions):
    """
    Генератор, возвращающий описание транзакций
    """
    for transaction in list_of_transactions:
        yield transaction["description"]


def card_number_generator(start_num, end_num):
    """
    Генератор номеров банковских карт с указанным диапазоном
    """
    for i in range(start_num, end_num + 1):
        str_card_numbers = '0' * (16 - len(str(i))) + str(i)
        yield ' '.join(map(lambda x: str_card_numbers[x * 4: (x + 1) * 4], range(4)))
