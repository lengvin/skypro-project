import csv
import pandas as pd


def read_csv_file(file_path):
    """
    Преобразование CSV файла в Python-объект
    """
    try:
        result = []
        with open(file_path, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                result.append(row)
    except (FileNotFoundError, ValueError, TypeError):
        return []
    else:
        return result


def read_excel_file(file_path):
    """
    Преобразование XLSX файла в Python-объект
    """
    df = pd.read_excel(file_path)
    result = []

    for index, row in df.iterrows():
        dict_ = {}

        for key, value in row.items():
            dict_[key] = value
        try:
            dict_['id'] = int(dict_['id'])
        except ValueError:
            pass
        finally:
            result.append(dict_)

    return result
