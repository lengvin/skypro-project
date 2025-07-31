import json


def read_json_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            json_file = json.load(file)
    except FileNotFoundError:
        return []
    except TypeError:
        return []
    except ValueError:
        return []
    else:
        return json_file
