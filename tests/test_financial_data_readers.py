from unittest.mock import mock_open, patch

import pandas as pd

from typing import Any


from src.financial_data_readers import csv_reader, excel_reader
from tests.conftest import mocked_file_content, result_to_excel_file


@patch("builtins.open", mock_open(read_data=mocked_file_content))
def test_csv_reader_with_mock_and_patch() -> None:
    """Тест на срабатывание csv_reader с mock и patch"""
    assert csv_reader("mocked_csv_file.csv") == result_to_excel_file


def test_csv_reader_file_not() -> None:
    """Тест при отсутствии файла по указанному пути"""
    assert csv_reader("nothing.xlsx") is None


mocked_excel_data = pd.DataFrame(
    {
        "id": ["1"],
        "state": ["EXECUTED"],
        "date": ["2023-09-05T11:30:32Z"],
        "amount": ["16210"],
        "currency_name": ["Sol"],
        "currency_code": ["PEN"],
        "from": ["Счет 58803664561298323391"],
        "to": ["Счет 39745660563456619397"],
        "description": ["Перевод организации"],
    }
)


@patch("pandas.read_excel", return_value=mocked_excel_data)
def test_excel_reader(mock_read_excel: Any) -> None:
    """Тест на срабатывание excel_reader с mock и patch"""

    expected_result = mocked_excel_data.to_dict("records")

    result = excel_reader("fake_path.xlsx")

    assert result == expected_result

    mock_read_excel.assert_called_once_with("fake_path.xlsx")
