from tests.conftest import transactions


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой."""

    """Переменная, отвечающая за ввод выбранного варианта с файлом,
     из которого будет взята информация о транзакциях"""

    choise_inf_file_input = input("""Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n
                        Выберите необходимый пункт меню:\n
                        1. Получить информацию о транзакциях из JSON-файла\n
                        2. Получить информацию о транзакциях из CSV-файла\n
                        3. Получить информацию о транзакциях из XLSX-файла\n""")

    while True:
        if choise_inf_file_input is "1":
            print('Для обработки выбран JSON-файл.')
            break

        elif choise_inf_file_input is "2":
            print('Для обработки выбран CSV-файл.')
            break

        elif choise_inf_file_input is "3":
            print('Для обработки выбран XLSX-файл.')
            break

        else:
            print('Некорректный ввод, попробуйте снова')



    status_for_filter_input = input('''Введите статус, по которому необходимо выполнить фильтрацию. \n
                                        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')

    while True:
        if status_for_filter_input is "EXECUTED":
            print('Операции отфильтрованы по статусу "EXECUTED"')
            break

        elif status_for_filter_input is "CANCELED":
            print('Операции отфильтрованы по статусу "CANCELED"')
            break

        elif status_for_filter_input is "PENDING":
            print('Операции отфильтрованы по статусу "PENDING"')
            break

        else:
            print(f'Статус операции {status_for_filter_input} недоступен.')


    sort_to_date_input = input("Отсортировать операции по дате? Да/Нет")

    while True:
        if sort_to_date_input is 'Да':
            pass
            break

        elif sort_to_date_input is 'Нет':
            break

        elif sort_to_date_input not in ['Да', 'Нет']:
            print()

    rub_not_only_rub_transactions = input("Выводить только рублевые транзакции? Да/Нет")

    if rub_not_only_rub_transactions is 'Да':
        pass

    filter_spec_word_in_description = input('''Отфильтровать список транзакций 
                                            по определенному слову в описании? Да/Нет''')

    if filter_spec_word_in_description is 'Да':
        pass

    transactions_in_sample = []   # список с данными о транзакций,
                                  # которые прошли через фильтр

    print(f'Всего операций в выборке: {len(transactions_in_sample)}')

    if len(transactions_in_sample) > 0:
        print(transactions_in_sample)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")