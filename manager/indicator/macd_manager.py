from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "macd",
    "O6Z6BDQ821VGC8T3",
    "Technical Analysis: MACD",
    "function=MACD&interval=daily&series_type=open",
    data7="MACD",
    data8="MACD_Hist",
    data9="MACD_Signal",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db(manager.get_all_symbols_from_disk())
