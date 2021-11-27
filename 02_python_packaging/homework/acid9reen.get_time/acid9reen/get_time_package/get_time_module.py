import requests

try:
    from acid9reen.pretty_print_package.pretty_print_module import \
        unix_to_pretty as utp
except ImportError:
    utp = None


def get_time() -> int:
    url = "http://worldtimeapi.org/api/timezone/Europe/Moscow"
    resp = requests.get(url)
    unixtime = resp.json().get("unixtime", 0)

    return unixtime


def main() -> int:
    unixtime = get_time()
    time_to_print = utp(unixtime) if utp else unixtime
    print(time_to_print)

    return 0


if __name__ == "__main__":
    SystemExit(main())
