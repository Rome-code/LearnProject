from collections import Counter
import re


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Функция для поиска транзакций с определенным словом в описании"""

    filtered_list = []

    for tx in data:
        description = tx.get("description", "")

        if re.search(re.escape(search), description, re.IGNORECASE):
            filtered_list.append(tx)

    return filtered_list


def process_bank_operations(transactions: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество
    операций в каждой категории.
    """
    category_counts = Counter(
        operation.get('description') for operation in transactions if operation.get('description') in categories
    )
    return dict(category_counts)
