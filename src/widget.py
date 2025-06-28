from masks import get_mask_account, get_mask_card_number


def mask_account_card(data_acc_or_card: str) -> str:
    "Функция, маскирующая номер счета или номер карты"
    masked_data = " "
    if data_acc_or_card.startswith("Счет") and len(data_acc_or_card) == 25:
        masked_data = get_mask_account(data_acc_or_card[5:])
    elif data_acc_or_card[:-17].isalpha() and data_acc_or_card[-16:].isdigit() and len(data_acc_or_card[-16:]) == 16:
        masked_data = get_mask_card_number(data_acc_or_card[-16:])
    return masked_data


def get_date(str_with_date_and_time: str) -> str:
    "Функция, возвращающая дату в формате ДД.ММ.ГГГГ"
    day_mon_year = " "
    if len(str_with_date_and_time) == 26 and "T" in str_with_date_and_time:
        day_mon_year = f"{str_with_date_and_time[8:10]}.{str_with_date_and_time[5:7]}.{str_with_date_and_time[0:4]}"
    else:
        "Некорректный ввод"
    return day_mon_year
