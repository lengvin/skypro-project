import json


def read_json_file(file_path):
    """
    Преобразование JSON файла в Python-объект
    """
    try:
        with open(file_path, encoding='utf-8') as file:
            json_file = json.load(file)
    except (FileNotFoundError, TypeError, json.JSONDecodeError, ValueError):
        return []
    else:
        return json_file
