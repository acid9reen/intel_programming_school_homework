from acid9reen.get_time_package.get_time_module import get_time
from acid9reen.pretty_print_package.pretty_print_module import unix_to_pretty


def main() -> int:
    unixtime = get_time()
    print(unix_to_pretty(unixtime))

    return 0


if __name__ == "__main__":
    SystemExit(main())
