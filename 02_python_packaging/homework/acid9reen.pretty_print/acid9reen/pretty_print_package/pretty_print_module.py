from datetime import datetime as dt


def unix_to_pretty(unixtime: int) -> str:
    formatted_time = dt.fromtimestamp(unixtime).strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time
