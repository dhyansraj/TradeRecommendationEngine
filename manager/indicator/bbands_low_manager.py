from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "bbands_low",
    "IU8X1O6HSQWLS2XX",
    "Technical Analysis: BBANDS",
    "function=BBANDS&interval=daily&time_period=200&series_type=low&nbdevup=3&nbdevdn=3&interval=daily&time_period=200",
    data26="Real Upper Band",
    data27="Real Middle Band",
    data28="Real Lower Band",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():

    manager.store_all_symbols_on_db_live()
