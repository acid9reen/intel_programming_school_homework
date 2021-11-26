from datetime import datetime as dt

from get_time_package.get_time_module import get_time


def print_time_pretty(unixtime: int) -> None:
    formatted_time = dt.fromtimestamp(unixtime).strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_time)


def main() -> int:
    unixtime = get_time()
    print_time_pretty(unixtime)

    return 0


if __name__ == "__main__":
    SystemExit(main())
