import pytest

from src.widget import get_date, mask_account_card
from tests.conftest import date_and_time, date_and_time_uncorrectly, date_and_time_uncorrectly_2

"Парметризация для mask_account_card"


@pytest.mark.parametrize(
    "data_acc_or_card, expected_result",
    (
        ["MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"],
        ["Maestro 1596837868705199", "Maestro 1596 83** **** 5199"],
        ["Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"],
        ["Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"],
        ["Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"],
        ["Счет 35383033474447895560", "Счет **5560"],
        ["7158300734726758", "Некорректный ввод"],
        ["Счет", "Некорректный ввод"],
        ["35383033474447895560", "Некорректный ввод"],
        ["", "Некорректный ввод"],
    ),
)
def test_mask_account_card(data_acc_or_card: str, expected_result: str) -> None:
    assert mask_account_card(data_acc_or_card) == expected_result


"Параметризация для функции get_date"


@pytest.mark.parametrize(
    "str_with_date_and_time, sorted_result",
    (
        ["", "Неверное количество введеных символов"],
        [date_and_time, "14.10.2018"],
        [date_and_time_uncorrectly, "Неверное количество введеных символов"],
        [1312, "Неверный тип данных даты и времени"],
        [date_and_time_uncorrectly_2, "Недопустимые символы в блоках цифр даты и времени"],
    )
)
def test_get_date(str_with_date_and_time: str, sorted_result: str) -> None:
    assert get_date(str_with_date_and_time) == sorted_result
