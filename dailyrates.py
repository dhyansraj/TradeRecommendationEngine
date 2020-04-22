import requests
import json
import csv
import time
from tredao import HistoricalRatesTable

daily_rates_path = "daily_rates/"
key = "Time Series (Daily)"


def fetchTodayRates(sym):
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


def getTodayRates(sym):
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


def getStoredSymbols():
    from os import listdir
    from os.path import isfile, join

    files = [f for f in listdir(daily_rates_path) if isfile(join(daily_rates_path, f))]
    return files


def toHrt(symbol, row):
    hrt = HistoricalRatesTable()

    hrt.symbol = symbol
    hrt.data0 = row["1. open"]
    hrt.data1 = row["2. high"]
    hrt.data2 = row["3. low"]
    hrt.data3 = row["4. close"]
    hrt.data4 = row["5. volume"]

    return hrt


def getHrtForAllSymbols():
    hrts = []
    for f in getStoredSymbols():
        symbol = f.split(".")[0]
        with open(daily_rates_path + f) as jfile:
            data = json.load(jfile)
            if key in data:
                for k in data[key]:
                    hrts.append(toHrt(symbol, data[key][k]))

    return hrts


def fetchAllSymbols(getStoredSymbols, fetchTodayRates):
    with open("nasdaqlisted.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter="|")
        existing_files = getStoredSymbols()

        i = 0
        for row in reader:
            sym = row["Symbol"]

            if sym + ".json" not in existing_files:
                print("Fetching ", sym)
                fetchTodayRates(sym)
                i += 1

                if i % 5 == 0:
                    time.sleep(60)
            else:
                print("Symbol ", sym, " already exists. Skiping.")


# fetchAllSymbols(getStoredSymbols, fetchTodayRates)

# getAllSymbols()[0].symbol
