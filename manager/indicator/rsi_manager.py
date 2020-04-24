from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "rsi",
    "G3U882UM0AXEH1WX",
    "Technical Analysis: RSI",
    "function=RSI&interval=daily&time_period=200&series_type=open",
    data12="RSI",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db()
