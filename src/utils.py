import json
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)
module_logger = logging.getLogger(__name__)


def read_json_file(file_path):
    """
    Преобразование JSON файла в Python-объект
    """
    try:
        with open(file_path, encoding="utf-8") as file:
            module_logger.info("Открытие JSON-файла")
            json_file = json.load(file)
    except (FileNotFoundError, TypeError, json.JSONDecodeError, ValueError) as e:
        module_logger.error(f"Ошибка: {e}")
        return []
    else:
        module_logger.info("Успешное преобразование JSON-файла в Python-объект")
        return json_file
