from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "adx",
    "MOARBV4V30DX6V4O",
    "Technical Analysis: ADX",
    "function=ADX&interval=daily&time_period=200",
    data13="ADX",
)


def store_all_symbols_on_disk():
    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db_live()
