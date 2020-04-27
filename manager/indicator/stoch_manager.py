from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "stoch",
    "5UPWIORMLZTOLO2O",
    "Technical Analysis: STOCH",
    "function=STOCH&interval=daily",
    data10="SlowK",
    data11="SlowD",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db_live()
