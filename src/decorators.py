from time import time
from functools import wraps


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            func_mame = func.__name__
            time_1 = time()
            time_2 = time()
            if filename:
                try:
                    result = func(*args, **kwargs)
                    with open(filename, 'a', encoding='windows-1251') as file:
                        file.write(f'\n Начало выполнения: {time_1} \n')
                        file.write(f'{func_mame} ok. результат выполнения: \n {result} \n')
                        file.write(f'Конец выполнения: {time_2} \n')
                except Exception as e:
                    with open(filename, 'a') as file:
                        file.write(f'\n Начало выполнения: {time_1} \n')
                        file.write(f'{func_mame} error: {e}. Inputs: {*args, *kwargs} \n')
                        file.write(f'Конец выполнения: {time_2} \n')
            else:
                try:
                    result = func(*args, **kwargs)
                    print(f'Начало выполнения: {time_1}')
                    print(f'{func_mame} ok. результат выполнения: \n {result}')
                    print(f'Конец выполнения: {time_2}')
                except Exception as e:
                    print(f'Начало выполнения: {time_1}')
                    print(f'{func_mame} error: {e}. Inputs: {*args, *kwargs}')
                    print(f'Конец выполнения: {time_2}')

        return inner

    return wrapper
