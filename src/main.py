from src.utils import transactions_data
from src.financial_data_readers import csv_reader
from src.financial_data_readers import excel_reader
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from tests.conftest import path_to_json_file, path_to_csv_file, path_to_xlsx_file, transactions
import datetime, re

json_file_path = path_to_json_file
csv_file_path = path_to_csv_file
xlsx_file_path = path_to_xlsx_file


def main():
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой."""


    def file_selection():
        """Функция, отвечающая за ввод выбранного варианта с файлом,
           из которого будет взята информация о транзакциях"""

        selection_inf_file_input = input("""Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
                            Выберите необходимый пункт меню:\n
                            1. Получить информацию о транзакциях из JSON-файла\n
                            2. Получить информацию о транзакциях из CSV-файла\n
                            3. Получить информацию о транзакциях из XLSX-файла\n""")

        while True:
            if selection_inf_file_input == "1":
                print('Для обработки выбран JSON-файл.\n')
                transactions_from_sel_file = transactions_data(json_file_path)
                return transactions_from_sel_file

            elif selection_inf_file_input == "2":
                print('Для обработки выбран CSV-файл.\n')
                transactions_from_sel_file = csv_reader(csv_file_path)
                return transactions_from_sel_file

            elif selection_inf_file_input == "3":
                print('Для обработки выбран XLSX-файл.\n')
                transactions_from_sel_file = excel_reader(xlsx_file_path)
                return transactions_from_sel_file

            else:
                print('Некорректный ввод, попробуйте снова\n')
                break

    def status_filter(transactions_from_sel_file):
        """Фильтрует список словарей с транзакциями по статусу транзакций"""

        status_for_filter_input = input('''Введите статус, по которому необходимо выполнить фильтрацию. \n
                                        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n''')

        while True:
            if status_for_filter_input.upper() == "EXECUTED":
                print('Операции отфильтрованы по статусу "EXECUTED"\n')
                state_filtered_list = filter_by_state(transactions_from_sel_file, "EXECUTED")
                return state_filtered_list

            elif status_for_filter_input.upper() == "CANCELED":
                print('Операции отфильтрованы по статусу "CANCELED"\n')
                state_filtered_list = filter_by_state(transactions_from_sel_file, "CANCELED")
                return state_filtered_list

            elif status_for_filter_input.upper() == "PENDING":
                print('Операции отфильтрованы по статусу "PENDING"\n')
                state_filtered_list = filter_by_state(transactions_from_sel_file, "PENDING")
                return state_filtered_list

            else:
                print(f'Статус операции {status_for_filter_input} недоступен. Попробуйте снова:')


    def date_filter(state_filtered_list):
        """Фильтрует список словарей с транзакциями по дате транзакций"""

        sort_to_date_input = input("Отсортировать операции по дате? Да/Нет\n")

        while True:
            if sort_to_date_input == 'Да':
                descending_selection = input("""Отсортировать по возрастанию или по убыванию?\n
                                                1. По возрастанию
                                                2. По убыванию""")

                if descending_selection == "1":
                    descending = False
                else:
                    descending = True

                date_sorted_list = sort_by_date(state_filtered_list, "date", descending)
                return date_sorted_list

            elif sort_to_date_input == 'Нет':
                date_sorted_list = state_filtered_list
                return date_sorted_list

            else:
                print(f"Вариант {sort_to_date_input} недоступен")


    def rub_filter(date_sorted_list):
        """Если ответ Да, выводит только рублевые транзакции"""

        rub_or_not_rub_transactions = input("Выводить только рублевые транзакции? Да/Нет\n")

        while True:
            if rub_or_not_rub_transactions == 'Да':
                rub_filtered_list = filter_by_currency(date_sorted_list, 'RUB')
                return rub_filtered_list

            elif rub_or_not_rub_transactions == 'Нет':
                rub_filtered_list = date_sorted_list
                return rub_filtered_list


    def spec_word_filter(rub_filtered_list: list) -> list:
        """Фильтр транзакций по определенному слову в описании"""
        spec_filter_word_in_description = input('''Отфильтровать список транзакций 
                                                   по определенному слову в описании? Да/Нет\n''')

        while True:
            if spec_filter_word_in_description == 'Да':

                spec_word_filtered_list = []

                search_string = input("Введите слово: ")

                for dict_n in rub_filtered_list:
                    
                    if re.search(search_string, dict_n["description", re.IGNORECASE]):
                        spec_word_filtered_list.append(dict_n)

                    elif 'description' not in dict_n:
                        return rub_filtered_list

                return spec_word_filtered_list

            elif spec_filter_word_in_description == 'Нет':
                spec_word_filtered_list = rub_filtered_list
                return spec_word_filtered_list


    step_1 = file_selection()
    step_2 = status_filter(step_1)
    step_3 = date_filter(step_2)
    step_4 = rub_filter(step_3)
    step_5 = spec_word_filter(step_4)


    filtered_transactions = spec_word_filter(step_5)

    print(f'Всего операций в выборке: {len(filtered_transactions)}')

    if len(filtered_transactions) > 0:
        return filtered_transactions
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


main()