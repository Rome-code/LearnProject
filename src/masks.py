import logging
import os


def get_mask_card_number(card_num: str) -> str:
    """Функция для маскировки номера карты"""
    if len(card_num) == 16 and card_num.isdigit():
        return f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"
    elif len(card_num) != 16:
        return "Недостаток или избыток символов, проверьте количество введенных символов"
    elif not card_num.isdigit():
        return "Введены символы, некорректные для номера карты"

    else:
        return "Некорректный ввод"


def get_mask_account(acc_num: str) -> str:
    """Функция для маскировки номера аккаунта"""
    if len(acc_num) == 20 and acc_num.isdigit():
        return f"**{acc_num[16:]}"
    elif len(acc_num) != 20:
        return "Недостаток или избыток символов, проверьте их количество"
    elif not acc_num.isdigit():
        return "Введены символы, некорректные для номера счета"

    else:
        return "Некорректный ввод"


root_logger = logging.getLogger()

masks_logger = logging.getLogger("__main__")
masks_logger.setLevel(logging.DEBUG)
path_to_masks = os.path.abspath(os.path.join(os.pardir, "logs", "masks.log"))

masks_file_handler = logging.FileHandler(path_to_masks, mode="w")
masks_file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
masks_file_handler.setFormatter(masks_file_formatter)
masks_logger.addHandler(masks_file_handler)
masks_logger.setLevel(logging.DEBUG)

masks_logger.debug("Debug message")
masks_logger.info("Info message")
masks_logger.warning("Warning message")
masks_logger.error("Error message")
masks_logger.critical("Critical message")
