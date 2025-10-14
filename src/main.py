from src.utils import transactions_data
from src.financial_data_readers import csv_reader, excel_reader
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from datetime import datetime
from src.widget import mask_account_card
import os, re


def main():
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой."""
    json_file_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "operations.json"
    )

    csv_file_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "transactions.csv"
    )

    xlsx_file_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "transactions_excel.xlsx"
    )
    # json_file_path = r'C:\Users\Rome\work\tmp\LearnProject\data\operations.json'
    # csv_file_path = r'C:\Users\Rome\work\tmp\LearnProject\data\transactions.csv'
    # xlsx_file_path = r"C:\Users\Rome\work\tmp\LearnProject\data\transactions_excel.xlsx"

    def file_selection():
        """Функция, отвечающая за ввод выбранного варианта с файлом,
           из которого будет взята информация о транзакциях"""

        while True:
            selection_inf_file_input = input("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
            Выберите необходимый пункт меню:\n
            1. Получить информацию о транзакциях из JSON-файла\n
            2. Получить информацию о транзакциях из CSV-файла\n
            3. Получить информацию о транзакциях из XLSX-файла\n""")


            if selection_inf_file_input == "1":
                print('Для обработки выбран JSON-файл.\n')
                return transactions_data(json_file_path)

            elif selection_inf_file_input == "2":
                print('Для обработки выбран CSV-файл.\n')
                return csv_reader(csv_file_path)

            elif selection_inf_file_input == "3":
                print('Для обработки выбран XLSX-файл.\n')
                return excel_reader(xlsx_file_path)

            else:
                print('Некорректный ввод, попробуйте снова\n')


    def status_filter(transactions_from_sel_file):
        """Фильтрует список словарей с транзакциями по статусу транзакций"""


        while True:
            status_for_filter_input = input(
'''\nВведите статус, по которому необходимо выполнить фильтрацию. \n
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n'''
)

            status_upper = status_for_filter_input.upper()

            if status_upper in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f'Операции отфильтрованы по статусу "{status_upper}"\n')
                state_filtered_list = filter_by_state(transactions_from_sel_file, status_upper)
                return state_filtered_list

            else:
                print('Некорректный статус, попробуйте снова.')


    def date_filter(state_filtered_list):
        """Фильтрует список словарей с транзакциями по дате транзакций"""

        while True:

            sort_to_date_input = input("\nОтсортировать операции по дате? Да/Нет\n")

            if sort_to_date_input.upper() in ['ДА', 'LF']:

                while True:
                    descending_selection = input("""Отсортировать по возрастанию или по убыванию?\n
                    1. По возрастанию
                    2. По убыванию\n"""
                    )

                    if descending_selection == "1":
                        descending = False
                        break

                    elif descending_selection == "2":
                        descending = True
                        break
                    else:
                        print('Некорректный статус, попробуйте снова.')

                date_sorted_list = sort_by_date(state_filtered_list, 'date', descending)
                return date_sorted_list

            elif sort_to_date_input.upper() in ['НЕТ', 'YTN']:
                date_sorted_list = state_filtered_list
                return date_sorted_list

            else:
                print(f"Вариант {sort_to_date_input} недоступен")


    def rub_filter(date_sorted_list):
        """Если ответ Да, выводит только рублевые транзакции"""

        while True:
            rub_or_not_rub_transactions = input("Выводить только рублевые транзакции? Да/Нет\n")

            if rub_or_not_rub_transactions.upper() in ['ДА', 'LF']:
                rub_filtered_list = filter_by_currency(date_sorted_list, 'RUB')
                return rub_filtered_list

            elif rub_or_not_rub_transactions.upper() in ['НЕТ', 'YTN']:
                rub_filtered_list = date_sorted_list
                return rub_filtered_list

            else:
                print("Некорректный ввод, попробуйте снова")


    def spec_word_filter(transactions_list):
        """Фильтр транзакций по наличию слова в описании"""
        while True:
            filter_choice = input("Отфильтровать по слову в описании? Да/Нет: ")

            if filter_choice.upper() in ['ДА', 'LF']:
                search_str = input("Введите слово для поиска: ")
                filtered_list = []

                for tx in transactions_list:
                    description = tx.get("description", "")

                    if re.search(re.escape(search_str), description, re.IGNORECASE):
                        filtered_list.append(tx)
                return filtered_list

            elif filter_choice.upper() in ['НЕТ', 'YTN']:
                return transactions_list

            else:
                print("Некорректный ввод, попробуйте снова.")

    filtered_transactions = file_selection()
    filtered_transactions = status_filter(filtered_transactions)
    filtered_transactions = date_filter(filtered_transactions)
    filtered_transactions = rub_filter(filtered_transactions)
    filtered_transactions = spec_word_filter(filtered_transactions)

    print(f'Всего операций в выборке: {len(filtered_transactions)}')
    print()

    if len(filtered_transactions) > 0:

        # Обработка и вывод
        for t in filtered_transactions:
            # Изменение формата даты на дд.мм.гггг
            datetime_obj = datetime.fromisoformat(t['date'])
            date_str = datetime_obj.strftime('%d.%m.%Y')

            description = t.get('description', '')
            amount = t['operationAmount']['amount']
            currency_code = t['operationAmount']['currency']['code']
            currency_name = t['operationAmount']['currency']['name']

            # Определяем тип операции по description
            if 'Перевод' in description:
                operation_type = description

            elif 'Открытие вклада' in description:
                operation_type = 'Открытие вклада'

            else:
                operation_type = description

            # Пункты для отображения в зависимости от Description
            from_account = t.get('from', '')
            to_account = t.get('to', '')

            # Маскируем номера карт/счётов с функцией mask_account_card
            from_masked = mask_account_card(from_account)
            to_masked = mask_account_card(to_account)

            if 'Перевод' in description:
                print(f"{date_str} {operation_type}")
                print(f"{from_masked} -> {to_masked}")
                print(f"Сумма: {amount} {currency_name}")
                print()

            elif 'Открытие' in description or 'вклад' in description:
                print(f"{date_str} {operation_type}")
                print(f"{to_masked}")
                print(f"Сумма: {amount} {currency_name}")
                print()

            else:
                print(f"{date_str} {operation_type}")
                print(f"Сумма: {amount} {currency_name}")
                print()
    else:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"

if __name__ == "__main__":
    main()
