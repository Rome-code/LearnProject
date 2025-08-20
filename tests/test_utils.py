from src.utils import transactions_data
from tests.conftest import list_of_transaction, not_path_to_json_file, path_to_json_empty_file, path_to_json_file


def test_transactions_data_base() -> None:
    "Тест базового срабатывания"

    assert transactions_data(path_to_json_file) == list_of_transaction


def test_transactions_data_error_1_2() -> None:
    "Тест на срабатывание с ошибкой FileNotFoundError и пустым файлом json"

    assert transactions_data(path_to_json_empty_file) == []
    assert transactions_data(not_path_to_json_file) == []
