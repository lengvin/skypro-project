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

## Модуль decorators.py

### Декораток log

Данный декоратор позволяет логировать начало, результат и конец работы функции, пример использования:
```
@log(filename='mylog.txt')
def my_function(a, b):
    retutn a + b

my_function(1, 2)
```

## Модуль opening.py

### Функция read_csv_file

Данная функция открывает и преобразовывает CSV файл в список словарей транзакций из файла, пример использования:
```
print(read_csv_file('example.csv'))
```

### Функция read_excel_file

Данная функция открывает и преобразовывает XLSX файл в список словарей транзакций из файла, пример использования:
```
print(read_excel_file('example.csv'))
```
