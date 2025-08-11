import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import (list_of_dict_all_states_canceled, list_of_dict_ident_dates_fixture,
                            list_of_dict_ident_dates_sort, list_of_dict_sort_res_false, list_of_dict_sort_res_true,
                            list_of_dict_sorted_1, list_of_dict_sorted_2, list_of_dict_without_state,
                            list_of_dicts_fixture)

"""Тесты для функции filter_by_state"""


def test_filter_by_state_default(list_of_dicts_fixture: list) -> None:
    """Тест на срабатывание функции со списком словарей list_of_dicts по дефолтным условиям"""
    assert filter_by_state(list_of_dicts_fixture) == list_of_dict_sorted_1


def test_filter_by_state_canceled(list_of_dicts_fixture: list) -> None:
    """Тест на срабатывание функции со списком словарей, где state = 'CANCELED'"""
    assert filter_by_state(list_of_dicts_fixture, state="CANCELED") == list_of_dict_sorted_2


"""Параметризация функции filter_by_state."""


@pytest.mark.parametrize(
    "value, expected",
    (
        [
            ([], []),
            (list_of_dict_without_state, list_of_dict_without_state),
            (list_of_dict_all_states_canceled, []),
        ]
    ),
)
def test_filter_by_state(value: list, expected: list) -> None:
    assert filter_by_state(value) == expected


"Тесты для функции sort_by_date"


def test_sort_by_date_des_true(list_of_dicts_fixture: list) -> None:
    """Тестирование сортировки списка словарей по дате в порядке убывания."""
    assert sort_by_date(list_of_dicts_fixture, "date") == list_of_dict_sort_res_true


def test_sort_by_date_des_false(list_of_dicts_fixture: list, descending: bool = False) -> None:
    """Тестирование сортировки списка словарей по дате в порядке возрастания."""
    assert sort_by_date(list_of_dicts_fixture, "date", False) == list_of_dict_sort_res_false


def test_sort_by_date_ident_dates(list_of_dict_ident_dates_fixture: list) -> None:
    """Проверка корректности сортировки при одинаковых датах"""
    assert sort_by_date(list_of_dict_ident_dates_fixture, "date") == list_of_dict_ident_dates_sort
