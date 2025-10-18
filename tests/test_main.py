from unittest.mock import patch

import pytest

from main import main

from typing import Any

@pytest.mark.parametrize(
    "inputs, expected_calls",
    [
        (
            ["1", "EXECUTED", "ДА", "2", "ДА", "YTN"],
            ["transactions_data", "filter_by_state", "sort_by_date", "filter_by_currency"],
        )
    ],
)
def test_main(monkeypatch, capsys, inputs, expected_calls) -> None:

    # Моки для зависимостей
    mock_transactions = [
        {
            "date": "2023-04-01T12:00:00",
            "description": "Перевод",
            "operationAmount": {"amount": "1000", "currency": {"code": "RUB", "name": "руб"}},
        }
    ]
    mock_filtered = mock_transactions
    mock_sorted = mock_transactions

    # Мок input() для подачи заданных последовательностей
    input_iter = iter(inputs)

    def mock_input(prompt) -> Any:
        return next(input_iter)

    monkeypatch.setattr("builtins.input", mock_input)

    # Моки функций загрузки данных
    with patch("main.transactions_data", return_value=mock_transactions) as mock_transactions_data, patch(
        "main.csv_reader", return_value=mock_transactions
    ) as mock_csv_reader, patch("main.excel_reader", return_value=mock_transactions) as mock_excel_reader, patch(
        "main.filter_by_state", return_value=mock_filtered
    ) as mock_filter_by_state, patch(
        "main.sort_by_date", return_value=mock_sorted
    ) as mock_sort_by_date, patch(
        "main.filter_by_currency", return_value=mock_transactions
    ) as mock_filter_by_currency, patch(
        "main.mask_account_card", side_effect=lambda acc: "***"
    ):

        # Вызываем main
        main()

    # Проверяем вызовы функций
    mock_funcs = {
        "transactions_data": mock_transactions_data,
        "filter_by_state": mock_filter_by_state,
        "sort_by_date": mock_sort_by_date,
        "filter_by_currency": mock_filter_by_currency,
        "csv_reader": mock_csv_reader,
        "excel_reader": mock_excel_reader
    }

    for func_name in expected_calls:
        assert mock_funcs[func_name].called

    # Проверяем вывод
    captured = capsys.readouterr()
    print(captured.out)
