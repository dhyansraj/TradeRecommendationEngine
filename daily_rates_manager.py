import requests
import json
import csv
import time
from trade_dao import HistoricalRatesTable
import util

daily_rates_path = "daily_rates/"
key = "Time Series (Daily)"


def store_todays_rates(sym):
    site = "https://www.alphavantage.co/query?"
    function = "function=TIME_SERIES_DAILY"
    symbol = "&symbol=" + sym
    apikey = "&apikey=5B2SMYIVORAAHUVQ"

    url = site + function + symbol + apikey

    response = requests.get(url)

    daily = json.loads(response.content.decode("utf-8"))

    if key in daily:

        with open(daily_rates_path + sym + ".json", "w") as outfile:
            json.dump(daily, outfile)


def get_todays_rates(sym):
    site = "https://www.alphavantage.co/query?"
    function = "function=TIME_SERIES_DAILY"
    symbol = "&symbol=" + sym
    apikey = "&apikey=5B2SMYIVORAAHUVQ"

    url = site + function + symbol + apikey

    response = requests.get(url)

    daily = json.loads(response.content.decode("utf-8"))

    try:
        price_map = daily[daily]["2020-04-20"]

        price_o = price_map["1. open"]
        price_h = price_map["2. high"]
        price_l = price_map["3. low"]
        price_c = price_map["4. close"]

    except:
        print(daily)

    print(
        sym,
        " - ",
        "Open: ",
        price_o,
        ", Close: ",
        price_c,
        ", High: ",
        price_h,
        ", Low: ",
        price_l,
    )


def get_stored_symbols():
    from os import listdir
    from os.path import isfile, join

    files = [f for f in listdir(daily_rates_path) if isfile(join(daily_rates_path, f))]
    return files


def convert_to_hrt(symbol, date, row):
    hrt = HistoricalRatesTable()

    hrt.symbol = symbol
    hrt.date = util.fromisoformat(date)
    hrt.data0 = row["1. open"]
    hrt.data1 = row["2. high"]
    hrt.data2 = row["3. low"]
    hrt.data3 = row["4. close"]
    hrt.data4 = row["5. volume"]

    return hrt


def get_all_symbols_as_hrt():
    hrts = []
    for f in get_stored_symbols():
        symbol = f.split(".")[0]
        with open(daily_rates_path + f) as jfile:
            data = json.load(jfile)
            if key in data:
                for k in data[key]:
                    hrts.append(convert_to_hrt(symbol, k, data[key][k]))

    return hrts


def store_all_symbols():
    with open("nasdaqlisted.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter="|")
        existing_files = get_stored_symbols()

        i = 0
        for row in reader:
            sym = row["Symbol"]

            if sym + ".json" not in existing_files:
                print("Fetching ", sym)
                store_todays_rates(sym)
                i += 1

                if i % 5 == 0:
                    time.sleep(60)
            else:
                print("Symbol ", sym, " already exists. Skiping.")


# store_all_symbols(get_stored_symbols, store_todays_rates)

# getAllSymbols()[0].symbol
