# Банковский виджет

## Описание:

банковский виджет - это новая фича для личного кабинета клиента, который показывает несколько последних успешных банковских операций клиента.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/lengvin/skypro-project.git
```

## Тестирование

Все модули покрыты тестами на 99%


## Модуль generators.py

### Итератор filter_by_currency

Данный итератор генерирует транзакции с указанной валютой из списка транзакций, пример использования:
```
from generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
for i in range(2):
    print(next(usd_transactions))
```

### Итератор transaction_descriptions

Данный итератор генерирует описания транзакций из списка транзакций, пример использования:
```
from generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)
for i in range(5):
    print(next(descriptions))
```

### Генератор card_number_generator

Данный генератор генерирует номера банковских карт в указанном диапазоне, пример использования:
```
from generators import card_number_generator

for card_number in card_number_generator(1, 5):
    print(card_number)
```