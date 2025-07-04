from datetime import datetime


def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    filter_list = []
    for dict in list_of_dicts:
        if state == dict.get("state"):
            filter_list.append(dict)
    return filter_list



