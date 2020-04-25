from datetime import datetime


def fromisoformat(date):
    date = date[:10]
    fmt = "%Y-%m-%d"
    return datetime.strptime(date, fmt).date()
