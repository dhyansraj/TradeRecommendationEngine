from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "ema",
    "W8TB3XIG1GKIGQEJ",
    "Technical Analysis: EMA",
    "function=EMA&interval=daily&time_period=200&series_type=open",
    data6="EMA",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db()
