import csv

import pandas as pd

from typing import Any


def csv_reader(csv_file_path: str) -> Any:
    """Функция, считывающая данные финансовых операций из CSV с файла и
       возвращающая список словарей с транзакциями"""
    try:
        csv_file_transactions = []
        with open(csv_file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                csv_file_transactions.append(row)

        return csv_file_transactions

    except FileNotFoundError:
        print(f"Ошибка: Файл '{csv_file_path}' не найден.")

    except Exception as e:
        print(f"Произошла ошибка при чтении Excel файла: {e}")

path_to_csv_file = r"H:\Pyton-разработчик учеба\transactions.csv"
print(csv_reader(path_to_csv_file))


def excel_reader(excel_file_path: str) -> Any:
    """Функция, считывающая данные финансовых операций из CSV с файла и
       возвращающая список словарей с транзакциями"""

    excel_file_transactions = []

    try:
        excel_data = pd.read_excel(excel_file_path)
        excel_data_as_dicts = excel_data.to_dict("records")

        for row in excel_data_as_dicts:
            excel_file_transactions.append(row)
        return excel_file_transactions

    except FileNotFoundError:
        print(f"Ошибка: Файл '{excel_file_path}' не найден.")

    except Exception as e:
        print(f"Произошла ошибка при чтении Excel файла: {e}")

# excel_file_path = r"H:\Pyton-разработчик учеба\transactions_excel.xlsx"
# print(excel_reader(excel_file_path))
