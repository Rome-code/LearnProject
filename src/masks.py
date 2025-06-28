def get_mask_card_number(card_num: str) -> str:
    """Функция для маскировки номера карты"""
    if len(card_num) == 16 and card_num.isdigit():
        return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"
    elif not card_num.isdigit():
        return "Введены символы, некорректные для номера карты"
    else:
        return "Недостаток или избыток символов, проверьте количество введенных символов"


def get_mask_account(acc_num: str) -> str:
    """Функция для маскировки номера аккаунта"""
    if len(acc_num) == 20 and acc_num.isdigit():
        return f"**{acc_num[16:]}"
    elif not acc_num.isdigit():
        return "Введены символы, некорректные для номера счета"
    else:
        return "Недостаток или избыток символов, проверьте количество введенных символов"
