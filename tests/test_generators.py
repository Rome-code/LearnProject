import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from tests.conftest import (
    card_number_generator_exp_result_1_5,
    card_number_generator_exp_result_2_2050,
    description_res,
    exp_with_result_rub,
    exp_with_result_usd,
    result_rub,
    result_usd,
    transactions,
    transactions_with_rub_1,
    transactions_with_rub_2,
    transactions_with_usd_1,
    transactions_with_usd_2,
    transactions_with_usd_3,
)


def test_filter_by_currency_with_usd() -> None:
    gived_transaction = filter_by_currency(transactions, "USD")
    assert next(gived_transaction) == transactions_with_usd_1
    assert next(gived_transaction) == transactions_with_usd_2
    assert next(gived_transaction) == transactions_with_usd_3


def test_filter_by_currency_with_rub() -> None:
    gived_transaction = filter_by_currency(transactions, "RUB")
    assert next(gived_transaction) == transactions_with_rub_1
    assert next(gived_transaction) == transactions_with_rub_2


@pytest.mark.parametrize(
    "value, expected",
    [
        (transactions, description_res),
        (result_usd, exp_with_result_usd),
        (result_rub, exp_with_result_rub),
        ([], [[]]),
    ],
)
def test_transaction_descriptions(value: list, expected: list) -> None:
    result = list(transaction_descriptions(value))
    assert result == expected


"""Параметризация для card_number_generator"""


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 5, card_number_generator_exp_result_1_5),
        (2000000000000000, 2000000000000010, card_number_generator_exp_result_2_2050),
        (0, 5, []),
        (0, 0, []),
        (8, 5, []),
        (5, 5, []),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected
