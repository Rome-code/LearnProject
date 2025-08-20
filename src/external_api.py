import requests
from dotenv import load_dotenv
import os



def transaction_amount(transaction:dict) -> float:
    """ Возвращает сумму транзакции в рублях"""

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    #Путь к файлу .env
    load_dotenv(os.path.join(base_dir,".env"))

    api_key = os.getenv('API_KEY')

    try:
        amount = transaction["operationAmount"]["amount"]

        if transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
            "Условие, задающее выполнение кода, если валюта EUR или USD"

            currency_from = transaction["operationAmount"]["currency"]["code"]

            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_from}&amount={amount}"

            payload = {}

            headers = {
                "apikey": f"{api_key}"
            }

            response = requests.request("GET", url, headers=headers, data=payload)

            status_code = response.status_code
            result = response.json()
            amount = result["result"]
        return float(amount)

    except KeyError:
        amount = 0.0
        return amount
