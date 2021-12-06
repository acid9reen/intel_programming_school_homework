from enum import Enum, auto
from functools import wraps
from timeit import default_timer as timer


class ExperimentStage(Enum):
    REQUEST_RESPONSE = auto()
    CPU_BOUND = auto()


def fib(num: int = 500_000) -> int:
    prev_prev, prev = 0, 1

    if num == 0:
        return prev_prev
    if num == 1:
        return prev

    for __ in range(1, num):
        prev_prev, prev = prev, prev_prev + prev

    return prev


def timeit(func):
    @wraps(func)
    def _timeit(*args, **kwargs):
        start = timer()
        __ = func(*args, **kwargs)
        end = timer()

        return f"{(end - start):.4f}"

    return _timeit


def main() -> int:
    num = int(input("num = "))
    print(fib(num))

    return 0


if __name__ == "__main__":
    SystemExit(main())
