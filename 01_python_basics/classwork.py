"""
Write a decorator that, when applied to a function, will
wrap it in such a way that every call to the decorated
function is logged with a timestamp and the arguments
(keyword and positional) of the called function are also
included in the log entry.
"""

from datetime import datetime as dt
from functools import wraps
from typing import Any, Callable


def logger(*, verbose: bool = True) -> Callable:
    def _logger(func: Callable) -> Callable:
        @wraps(func)
        def __logger(*args, **kwargs) -> Any:
            timestamp = dt.now().timestamp()

            print("-" * 35)
            if verbose:
                print(
                    f"Function name: {func.__name__}",
                    f"Docstring: {func.__doc__}",
                    sep="\n",
                )

            print(
                f"Positional arguments: {args}",
                f"Keyword arguments: {kwargs}",
                sep="\n",
            )

            print(f"Timestamp: {timestamp}")
            print("-" * 35)

            return func(*args, **kwargs)

        return __logger

    return _logger


@logger(verbose=True)
def pprint(*args, **kwargs):
    print(*args, kwargs)


def main():
    pprint("df", 43, [34, 54, 25], k=144, m="fdga")


if __name__ == "__main__":
    main()
