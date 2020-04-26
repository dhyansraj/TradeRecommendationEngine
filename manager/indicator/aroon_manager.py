from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "aroon",
    "YNECR52IM6Y24UD4",
    "Technical Analysis: AROON",
    "function=AROON&interval=daily&time_period=200",
    data15="Aroon Up",
    data16="Aroon Down",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db(manager.get_all_symbols_from_disk())
