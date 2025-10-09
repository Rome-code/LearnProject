import pytest
from unittest.mock import patch, MagicMock
from src.main import main

@pytest.mark.parametrize("inputs, expected_calls", [
    (["1", "EXECUTED", "ДА", "2", "НЕТ", "YTN", "НЕТ", "НЕТ"], ["transactions_data", "filter_by_state", "sort_by_date", "filter_by_currency"])
])
def test_main(monkeypatch, capsys, inputs, expected_calls) -> None:

    # Моки для зависимостей
    mock_transactions = [{"date": "2023-04-01T12:00:00", "description": "Перевод", "operationAmount": {"amount": "1000", "currency": {"code": "RUB", "name": "руб"}}}]
    mock_filtered = mock_transactions
    mock_sorted = mock_transactions

    # Мок input() для подачи заданных последовательностей
    input_iter = iter(inputs)

    def mock_input(prompt):
        return next(input_iter)

    monkeypatch.setattr("builtins.input", mock_input)

    # Моки функций загрузки данных
    with patch("src.utils.transactions_data", return_value=mock_transactions) as mock_transactions_data, \
         patch("src.financial_data_readers.csv_reader", return_value=mock_transactions) as mock_csv_reader, \
         patch("src.financial_data_readers.excel_reader", return_value=mock_transactions), \
         patch("src.processing.filter_by_state", return_value=mock_filtered) as mock_filter_by_state, \
         patch("src.processing.sort_by_date", return_value=mock_sorted) as mock_sort_by_date, \
         patch("src.generators.filter_by_currency", return_value=mock_transactions), \
         patch("src.widget.mask_account_card", side_effect=lambda acc: "***"):

        # Вызываем main
        main()



    # Проверяем вызовы функций
    for func_name in expected_calls:
        assert mock_transactions_data.called
        assert mock_filter_by_state.called
        assert mock_csv_reader.called


    # Проверяем вывод
    captured = capsys.readouterr()
    print(captured.out)
