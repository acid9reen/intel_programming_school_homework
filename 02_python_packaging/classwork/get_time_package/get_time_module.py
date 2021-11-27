import requests


def get_time() -> int:
    url = "http://worldtimeapi.org/api/timezone/Europe/Moscow"
    resp = requests.get(url)
    unixtime = resp.json().get("unixtime", 0)

    return unixtime


def print_time(unixtime: int) -> None:
    print(unixtime)


def main() -> int:
    unixtime = get_time()
    print(unixtime)

    return 0


if __name__ == "__main__":
    SystemExit(main())
