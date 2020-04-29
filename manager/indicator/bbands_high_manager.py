from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "bbands_high",
    "IAQH3DS4YAYABN7N",
    "Technical Analysis: BBANDS",
    "function=BBANDS&interval=daily&time_period=200&series_type=high&nbdevup=3&nbdevdn=3&interval=daily&time_period=200",
    data23="Real Upper Band",
    data24="Real Middle Band",
    data25="Real Lower Band",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():

    manager.store_all_symbols_on_db_live()
