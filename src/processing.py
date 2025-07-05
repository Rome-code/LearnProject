from datetime import datetime


def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция, сортирующая список словарей по ключу state с условием
    по-умолчанию EXECUTED"""
    filter_list = []
    for dict_n in list_of_dicts:
        if state == dict_n.get("state"):
            filter_list.append(dict_n)
    return filter_list


def sort_by_date(data_list: list, data_key: str, descending: bool = True) -> list:
    """Функция, сортирующая список словарей по ключу date с условием
    по-умолчанию сортировать по убыванию"""
    return sorted(data_list, key=lambda x: datetime.strptime(x[data_key], "%Y-%m-%dT%H:%M:%S.%f"), reverse=descending)
