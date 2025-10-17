import logging
import os


def setup_logging_masks() -> None:
    masks_logger.setLevel(logging.DEBUG)
    path_to_masks = os.path.abspath(os.path.join(os.pardir, "logs", "masks.log"))

    masks_file_handler = logging.FileHandler(path_to_masks, mode="w")
    masks_file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    masks_file_handler.setFormatter(masks_file_formatter)
    masks_logger.addHandler(masks_file_handler)

    masks_logger.debug("Debug message")
    masks_logger.info("Info message")
    masks_logger.warning("Warning message")
    masks_logger.error("Error message")
    masks_logger.critical("Critical message")

# Вызов функции настройки логирования
setup_logging_masks()

# Настройка логгера
masks_logger = logging.getLogger("masks")

def get_mask_card_number(card_num: str) -> str:
    """Функция для маскировки номера карты"""
    masks_logger.debug(f"Начало работы функции с параметром: {card_num}")

    if len(card_num) == 16 and card_num.isdigit():
        masked_card = f"{card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"
        masks_logger.info(f"Маскированный номер карты: {masked_card}")
        return masked_card
    elif len(card_num) != 16:
        warning_message = "Недостаток или избыток символов, проверьте количество введенных символов"
        masks_logger.warning(warning_message)
        return warning_message
    elif not card_num.isdigit():
        error_message = "Введены символы, некорректные для номера карты"
        masks_logger.error(error_message)
        return error_message
    else:
        return "Некорректный ввод"


def get_mask_account(acc_num: str) -> str:
    """Функция для маскировки номера аккаунта"""
    if len(acc_num) == 20 and acc_num.isdigit():
        masked_acc = f"**{acc_num[16:]}"
        masks_logger.info(f"Маскированный номер счета: {masked_acc}")
        return masked_acc
    elif len(acc_num) != 20:
        warning_message = "Недостаток или избыток символов, проверьте их количество"
        masks_logger.warning(warning_message)
        return warning_message
    elif not acc_num.isdigit():
        error_message = "Введены символы, некорректные для номера счета"
        masks_logger.error(error_message)
        return error_message
    else:
        return "Некорректный ввод"
