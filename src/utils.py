import json
import logging
import os


def transactions_data(path_to_json_file: str) -> list:
    """Преобразование JSON-файла в список словарей"""

    try:
        with open(path_to_json_file, "r", encoding="utf-8") as f:
            transaction_data = json.load(f)
        if type(transaction_data) is not list or len(transaction_data) == 0:
            return []
        return transaction_data

    except json.JSONDecodeError:
        return []

    except FileNotFoundError:
        return []


utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
path_to_utils = os.path.abspath(os.path.join(os.pardir, "logs", "utils.log"))

utils_file_handler = logging.FileHandler(path_to_utils, mode="w")
utils_file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
utils_file_handler.setFormatter(utils_file_formatter)
utils_logger.addHandler(utils_file_handler)
utils_logger.setLevel(logging.DEBUG)

utils_logger.debug("Debug message")
utils_logger.info("Info message")
utils_logger.warning("Warning message")
utils_logger.error("Error message")
utils_logger.critical("Critical message")
