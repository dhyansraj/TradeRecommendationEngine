from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "sma",
    "XCD1OICB033WI7W8",
    "Technical Analysis: SMA",
    "function=SMA&interval=daily&time_period=200&series_type=open",
    data5="SMA",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db()
