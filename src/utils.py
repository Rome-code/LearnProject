import json


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
