from src import utils
import json


def test_read_json_file():
    json_file_path = 'data/operations.json'
    func_result = utils.read_json_file(json_file_path)

    with open(json_file_path, encoding='utf-8') as file:
        dict_result = json.load(file)

    assert func_result == dict_result
