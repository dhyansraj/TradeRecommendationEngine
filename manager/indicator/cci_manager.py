from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "cci",
    "GYJGYCBQANG01UWC",
    "Technical Analysis: CCI",
    "function=CCI&interval=daily&time_period=200",
    data14="CCI",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db(manager.get_all_symbols_from_disk())
