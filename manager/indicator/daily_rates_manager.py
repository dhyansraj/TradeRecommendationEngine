from manager.indicator.indicator_manager import IndicatorManager

manager = IndicatorManager(
    "daily_rates",
    "5B2SMYIVORAAHUVQ",
    "Time Series (Daily)",
    "function=TIME_SERIES_DAILY",
    data0="1. open",
    data1="2. high",
    data2="3. low",
    data3="4. close",
    data4="5. volume",
)


def store_all_symbols_on_disk():

    manager.store_all_symbols_on_disk()


def store_all_symbols_on_db():
    manager.store_all_symbols_on_db(True)
