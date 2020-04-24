from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "obv",
    "A8OOINAZ1UM76LZZ",
    "Technical Analysis: OBV",
    "function=OBV&interval=daily",
    data29="OBV",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db()
