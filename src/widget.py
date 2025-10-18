from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data_acc_or_card: str) -> str:
    #Функция, маскирующая номер счета или номер карты

    if data_acc_or_card.startswith("Счет") and len(data_acc_or_card) == 25:
        masked_data = f"{data_acc_or_card[:4]} {get_mask_account(data_acc_or_card[5:])}"
    elif not data_acc_or_card[:-16].isdigit() and data_acc_or_card[-16:].isdigit() and len(data_acc_or_card[:-16]) > 0:
        masked_data = f"{data_acc_or_card[:-16]}{get_mask_card_number(data_acc_or_card[-16:])}"
    else:
        return "Некорректный ввод"
    return masked_data


def get_date(str_with_date_and_time: str) -> str:
    "Функция, возвращающая дату в формате ДД.ММ.ГГГГ"
    if not isinstance(str_with_date_and_time, str):
        return "Неверный тип данных даты и времени"
    elif len(str_with_date_and_time) != 26:
        return "Неверное количество введеных символов"
    elif not (str_with_date_and_time[:4].isdigit() and str_with_date_and_time[5:7].isdigit()
             and str_with_date_and_time[8:10].isdigit() and str_with_date_and_time[11:13].isdigit()
             and str_with_date_and_time[14:16].isdigit() and str_with_date_and_time[17:19].isdigit()
             and str_with_date_and_time[21:].isdigit()):
        return "Недопустимые символы в блоках цифр даты и времени"
    elif (
        str_with_date_and_time[10] == "T"
        and str_with_date_and_time[4] == "-"
        and str_with_date_and_time[7] == "-"
        and str_with_date_and_time[-7] == "."
    ):
        day_mon_year = f"{str_with_date_and_time[8:10]}.{str_with_date_and_time[5:7]}.{str_with_date_and_time[0:4]}"
        return day_mon_year
    else:
        return "Некорректный ввод"
