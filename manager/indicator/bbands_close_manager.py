from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "bbands_close",
    "B9PYGN3NUATWZIUR",
    "Technical Analysis: BBANDS",
    "function=BBANDS&interval=daily&time_period=200&series_type=close&nbdevup=3&nbdevdn=3&interval=daily&time_period=200",
    data17="Real Upper Band",
    data18="Real Middle Band",
    data19="Real Lower Band",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():

    manager.store_all_symbols_on_db_live()
