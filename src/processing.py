from datetime import datetime
from typing import Any
import re


def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция, сортирующая список словарей по ключу state с условием
    по-умолчанию EXECUTED"""
    filter_list = []
    for dict_n in list_of_dicts:
        if state == dict_n.get("state"):
            filter_list.append(dict_n)
        elif 'state' not in dict_n:
            return list_of_dicts
    return filter_list


def sort_by_date(data_list: list, data_key: str, descending: bool = True) -> list:
    """Сортировка по ключу date, с обработкой пропущенных дат, с условием
    по-умолчанию сортировать по убыванию"""
    def parse_date(date_str) -> Any:
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        except (ValueError, TypeError):
            return datetime.min

    return sorted(
        data_list,
        key=lambda x: parse_date(x.get(data_key)),
        reverse=descending
    )
