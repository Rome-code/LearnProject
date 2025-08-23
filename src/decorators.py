from functools import wraps
from typing import Any, Callable


def log(filename: str | Any = None) -> Callable:
    """Декоратор, логирующий работу функции и ее результат в консоль"""

    def logging_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} is ok\n")
                else:
                    print(f"{func.__name__} is ok\n")
                return result
            except Exception as error_:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {error_}, input: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error_}, input: {args}, {kwargs}\n")
            except ZeroDivisionError as error_2:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {error_2}, input: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error_2}, input: {args}, {kwargs}\n")
                return result

        return wrapper

    return logging_decorator
