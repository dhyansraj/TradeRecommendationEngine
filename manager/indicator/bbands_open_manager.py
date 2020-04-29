from manager.indicator.indicator_manager import IndicatorManager


manager = IndicatorManager(
    "bbands_open",
    "HDY88RPWVMREB9Q7",
    "Technical Analysis: BBANDS",
    "function=BBANDS&interval=daily&time_period=200&series_type=open&nbdevup=3&nbdevdn=3&interval=daily&time_period=200",
    data20="Real Upper Band",
    data21="Real Middle Band",
    data22="Real Lower Band",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():

    manager.store_all_symbols_on_db_live()
