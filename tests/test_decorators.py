from typing import Any

from src.decorators import log


def test_log_with_filename_1() -> None:
    """Тестирует результат успешного выполнения функции"""

    @log(filename="log.txt")
    def my_function(x: Any, y: Any) -> Any:
        return x * y

    result = my_function(2, 4)
    assert result == 8


def test_log_with_filename_2_divizion_zero() -> None:
    """Тестирует запись в файл после успешного выполнения"""

    @log(filename="log.txt")
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    result = my_function(2, 0)
    assert result is None


def test_log_without_filename_2_divizion_zero() -> None:
    """Тестирует вывод в консоль после ошибки"""

    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x / y

    result = my_function(2, 0)
    assert result is None


def test_log_console_positive(capsys: Any) -> None:
    """Тестирует вывод в консоль после успешного выполнения"""

    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x * y

    my_function(2, 4)
    captured = capsys.readouterr()
    assert captured.out == "my_function is ok\n\n"


def test_log_console_negative(capsys: Any) -> None:
    """Тестирует вывод после ошибки в консоль"""

    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x * y

    my_function("2", "4")
    captured = capsys.readouterr()
    assert (
        captured.out
        == """my_function error: can't multiply sequence by non-int of type 'str', input: ('2', '4'), {}\n\n"""
    )


def test_log_file_positive(capsys: Any) -> None:
    """Тестирует запись в файл после успешного выполнения"""

    @log(filename="log.txt")
    def my_function(x: Any, y: Any) -> Any:
        return x * y

    my_function(2, 4)
    with open("log.txt", "r") as file:
        logs = file.read()

    assert "my_function is ok\n" in logs


def test_log_exception_file_log(capsys: Any) -> None:
    """Тестирует запись в файл после ошибки"""

    @log(filename="log.txt")
    def func(x: Any, y: Any) -> Any:
        return x + y

    func(1, "2")
    with open("log.txt", "r") as file:
        logs = file.read()

    assert "func error: unsupported operand type(s) for +: 'int' and 'str', input: (1, '2'), {}\n" in logs
