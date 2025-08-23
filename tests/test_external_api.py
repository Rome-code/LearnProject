from unittest.mock import Mock
from unittest.mock import patch
import requests
from src.external_api import transaction_amount
from tests.conftest import usd_transaction, rub_transaction
from dotenv import load_dotenv
import os




@patch('requests.request')
def test_transaction_amount_usd(mock_request ):
    "тестирует конвертацию USD в RUB"

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Путь к файлу .env
    load_dotenv(os.path.join(base_dir, ".env"))

    api_key = os.getenv('API_KEY')
    currency_from = "USD"
    amount = 1

    mock_request.return_value.json.return_value = \
        {
            "success": True,
            "query": {
                "from": "USD",
                "to": "RUB",
                "amount": 1
            },
            "info": {
                "timestamp": 1755681064,
                "rate": 80.299329
            },
            "date": "2025-08-20",
            "result": 80.299329
        }
    assert transaction_amount(usd_transaction) == 80.299329
    mock_request.assert_called_once_with(
        "GET",
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}",
        headers={"apikey": api_key},
        data={}
    )


def test_transaction_amount_base():
    "Тест на срабатывание без использования конвертации и запроса к API"
    assert transaction_amount(rub_transaction) == 1.0
