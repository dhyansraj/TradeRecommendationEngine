from datetime import datetime


def fromisoformat(date):
    fmt = "%Y-%m-%d"
    return datetime.strptime(date, fmt).date()


print(fromisoformat("2020-04-21"))
