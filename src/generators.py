from typing import Generator


def filter_by_currency(transactions_list: list, currency: str) -> Generator:
    if len(transactions_list) > 0:
        for transaction in transactions_list:
            if currency == transaction.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency:
                yield transaction
    else:
        yield []


def transaction_descriptions(transaction_list: list) -> Generator:
    if len(transaction_list) > 0:
        for transaction in transaction_list:
            yield transaction.get("description")
    else:
        yield []


def card_number_generator(start: int, stop: int) -> Generator:
    if stop > start >= 1:
        start += 1
        for number in range(start - 1, stop + 1):
            card_number = str(number)
            while len(card_number) < 16:
                card_number = "0" + card_number
            formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
            yield formatted_card_number
