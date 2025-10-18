import json
import logging
import os

# Настройка логгера
utils_logger = logging.getLogger("utils")


def setup_logging_utils() -> None:
    utils_logger.setLevel(logging.DEBUG)

    # Определения пути
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    log_dir = os.path.join(project_root, "logs")

    # Создаем директорию для логов
    os.makedirs(log_dir, exist_ok=True)
    path_to_utils = os.path.join(log_dir, "utils.log")

    utils_file_handler = logging.FileHandler(path_to_utils, mode="w", encoding="utf-8")
    utils_file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    utils_file_handler.setFormatter(utils_file_formatter)
    utils_logger.addHandler(utils_file_handler)

    utils_logger.debug("Debug message")
    utils_logger.info("Info message")
    utils_logger.warning("Warning message")
    utils_logger.error("Error message")
    utils_logger.critical("Critical message")


# Вызов функции настройки логирования
setup_logging_utils()

def transactions_data(path_to_json_file: str) -> list:
    """Преобразование JSON-файла в список словарей"""

    utils_logger.debug(f"Начало работы функции с параметром: {path_to_json_file}")
    try:
        with open(path_to_json_file, "r", encoding="utf-8") as f:
            utils_logger.info(f"Чтение данных из файла{path_to_json_file}")
            transaction_data = json.load(f)
        if type(transaction_data) is not list or len(transaction_data) == 0:
            utils_logger.warning("Данные не являются списком или список пуст")
            return []

        utils_logger.info("Данные успешно преобразованы в список")
        return transaction_data

    except json.JSONDecodeError as e:
        utils_logger.error(f"Ошибка декодирования JSON: {e}")
        return []

    except FileNotFoundError as e:
        utils_logger.error(f"Файл не найден: {e}")
        return []
