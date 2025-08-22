from src import opening, utils, widget, processing, generators


def yes_or_no():
    while True:
        user_input = input()
        if user_input.lower() == 'да':
            return True
        elif user_input.lower() == 'нет':
            return False
        else:
            print('Некоректный ответ, пожалуйста, повторите попытку')


def take_data_from_user():
    user_params = {}
    file_extensions = {'1': 'JSON', '2': 'CSV', '3': 'XLSX'}
    params = ['file_extension',
              'file_path',
              'state_type',
              'is_sort_by_date',
              'is_rub_transactions',
              'sort_word',
              'sort_reverse']
    questions = ['''
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
             ''',
                 'Укажите путь до файла с транзакциями',
                 'Введите статус, по которому необходимо выполнить фильтрацию. \nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING',
                 'Отсортировать операции по дате? Да/Нет',
                 'Выводить только рублевые транзакции? Да/Нет',
                 'Отфильтровать список транзакций по определенному слову в описании? Да/Нет']

    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. \n')

    for i in range(len(questions)):
        while True:
            print(questions[i])
            if i == 0:
                user_input = input()

                if user_input in ['1', '2', '3']:
                    user_params[params[i]] = file_extensions[user_input]
                    break
                else:
                    print('Некоректный ответ, пожалуйста, повторите попытку')
            elif i == 1:
                user_input = input()
                user_params[params[i]] = user_input
                break
            elif i == 2:
                user_input = input()

                if user_input.upper() in ['EXECUTED', 'CANCELED', 'PENDING']:
                    user_params[params[i]] = user_input.upper()
                    break
                else:
                    print('Некоректный ответ, пожалуйста, повторите попытку')
            elif i == 3:
                user_input = yes_or_no()
                user_params[params[i]] = user_input

                if user_input:
                    print('Отсортировать по возрастанию?')
                    user_input = yes_or_no()
                    user_params[params[-1]] = user_input
                    break
                else:
                    user_params[params[-1]] = user_input
                    break
            elif i == 5:
                user_input = yes_or_no()

                if user_input:
                    print('Введите слово для фильтрации')
                    user_word = input()
                    user_params[params[i]] = user_word
                    break
                else:
                    user_params[params[i]] = None
                    break
            else:
                user_input = yes_or_no()

                if user_input or not user_input:
                    user_params[params[i]] = user_input
                    break
                else:
                    print('Некоректный ответ, пожалуйста, повторите попытку')

    return user_params


def main():
    user_sort_params = take_data_from_user()
    raw_data = []
    result = []

    try:
        if user_sort_params['file_extension'] == 'JSON':
            raw_data = utils.read_json_file(user_sort_params['file_path'])
        elif user_sort_params['file_extension'] == 'CSV':
            raw_data = opening.read_csv_file(user_sort_params['file_path'])
        elif user_sort_params['file_extension'] == 'XLSX':
            raw_data = opening.read_excel_file(user_sort_params['file_path'])
    except FileNotFoundError:
        print('Файла не существует либо введён некоректный путь до файла')
    else:
        sorting_list = processing.filter_by_state(raw_data, state=user_sort_params['state_type'])

        if user_sort_params['is_sort_by_date']:
            sorting_list = processing.sort_by_date(sorting_list, _reverse=not user_sort_params['sort_reverse'])

        if user_sort_params['sort_word']:
            sorting_list = processing.process_bank_search(sorting_list, user_sort_params['sort_word'])

        if user_sort_params['is_rub_transactions']:
            rub_transactions = generators.filter_by_currency(sorting_list, 'RUB')
            for i in range(len(sorting_list)):
                try:
                    result.append(next(rub_transactions))
                except StopIteration:
                    break
            sorting_list = result

        if not sorting_list:
            print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        else:
            for transaction in sorting_list:
                date = widget.get_date(transaction["date"])
                description = transaction["description"]
                from_ = transaction['from']
                to = transaction['to']

                if transaction.get('operationAmount'):
                    amount = transaction['operationAmount']['amount']
                    currency = transaction['operationAmount']['currency']['name']
                else:
                    amount = transaction['amount']
                    currency = transaction['currency_name']

                if transaction['from']:
                    print(f'{date} {description} \n'
                          f'{from_} -> {to} \n'
                          f'Сумма: {amount} {currency} \n')
                else:
                    print(f'{date} {description} \n'
                          f'{to} \n'
                          f'Сумма: {amount} {currency} \n')


if __name__ == '__main__':
    main()
