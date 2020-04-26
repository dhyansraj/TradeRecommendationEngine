from manager.indicator.indicator_manager import IndicatorManager
import time

close_manager = IndicatorManager(
    "bbands_close",
    "B9PYGN3NUATWZIUR",
    "Technical Analysis: BBANDS",
    "function=BBANDS&interval=daily&time_period=200&series_type=close&nbdevup=3&nbdevdn=3&interval=daily&time_period=200",
    data17="Real Upper Band",
    data18="Real Middle Band",
    data19="Real Lower Band",
)

open_manager = IndicatorManager(
    "bbands_open",
    "HDY88RPWVMREB9Q7",
    "Technical Analysis: BBANDS",
    "function=BBANDS&interval=daily&time_period=200&series_type=open&nbdevup=3&nbdevdn=3&interval=daily&time_period=200",
    data20="Real Upper Band",
    data21="Real Middle Band",
    data22="Real Lower Band",
)

high_manager = IndicatorManager(
    "bbands_high",
    "IAQH3DS4YAYABN7N",
    "Technical Analysis: BBANDS",
    "function=BBANDS&interval=daily&time_period=200&series_type=high&nbdevup=3&nbdevdn=3&interval=daily&time_period=200",
    data23="Real Upper Band",
    data24="Real Middle Band",
    data25="Real Lower Band",
)

low_manager = IndicatorManager(
    "bbands_low",
    "IU8X1O6HSQWLS2XX",
    "Technical Analysis: BBANDS",
    "function=BBANDS&interval=daily&time_period=200&series_type=low&nbdevup=3&nbdevdn=3&interval=daily&time_period=200",
    data26="Real Upper Band",
    data27="Real Middle Band",
    data28="Real Lower Band",
)


def store_all_symbols_on_disk():

    close_manager.store_all_symbols_on_disk()
    time.sleep(60)
    open_manager.store_all_symbols_on_disk()
    time.sleep(60)
    high_manager.store_all_symbols_on_disk()
    time.sleep(60)
    low_manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():

    close_manager.store_all_symbols_on_db(close_manager.get_all_symbols_from_disk())

    open_manager.store_all_symbols_on_db(open_manager.get_all_symbols_from_disk())

    high_manager.store_all_symbols_on_db(high_manager.get_all_symbols_from_disk())

    low_manager.store_all_symbols_on_db(low_manager.get_all_symbols_from_disk())
