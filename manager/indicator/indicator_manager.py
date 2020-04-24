import requests
import json
import csv
import time
from trade_dao import HistoricalRatesTable
import trade_dao as dao
import util
import os


class IndicatorManager:
    site = "https://www.alphavantage.co/query?"

    def __init__(self, name, apiKey, key, function, **data):
        self.store_at = name + "/"
        self.key = key
        self.apiKey = "&apikey=" + apiKey
        self.function = function
        self.data = data

        try:
            os.makedirs(self.store_at)
        except OSError:
            pass

    def store(self, sym):

        symbol = "&symbol=" + sym

        url = IndicatorManager.site + self.function + symbol + self.apiKey

        print(url)

        response = requests.get(url)

        daily = json.loads(response.content.decode("utf-8"))

        if self.key in daily:
            with open(self.store_at + sym + ".json", "w") as outfile:
                json.dump(daily, outfile)
        else:
            print(daily)

    def get_stored_symbols(self):
        from os import listdir
        from os.path import isfile, join

        files = [f for f in listdir(self.store_at) if isfile(join(self.store_at, f))]
        return files

    def convert_to_hrt(self, symbol, date, row):
        hrt = HistoricalRatesTable()

        hrt.symbol = symbol
        hrt.date = util.fromisoformat(date)

        for k in self.data:
            setattr(hrt, k, row[self.data[k]])

        return hrt

    def get_all_symbols_as_hrt(self):
        hrts = []
        for f in self.get_stored_symbols():
            symbol = f.split(".")[0]
            with open(self.store_at + f) as jfile:
                data = json.load(jfile)
                if self.key in data:
                    for k in data[self.key]:
                        hrts.append(self.convert_to_hrt(symbol, k, data[self.key][k]))

        return hrts

    def store_all_symbols_on_disk(self):
        with open("nasdaqlisted.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter="|")
            existing_files = self.get_stored_symbols()
            print("Storing in ", self.store_at)
            i = 0
            for row in reader:
                sym = row["Symbol"]

                if sym + ".json" not in existing_files:
                    print("Fetching ", sym)
                    self.store(sym)
                    i += 1

                    if i % 5 == 0:
                        time.sleep(60)
                else:
                    print("Symbol ", sym, " already exists. Skiping.")

    def store_all_symbols_on_db(self, daily_rates=False):
        hrts = self.get_all_symbols_as_hrt()
        ehrts = {str(i.symbol) + ":" + str(i.date): i for i in dao.get_all_records()}
        for hrt in hrts:
            ehrt = ehrts.get(hrt.symbol + ":" + str(hrt.date))
            if daily_rates and ehrt:
                continue
            elif daily_rates:
                dao.create_record(hrt)
            elif ehrt:
                for k in self.data:
                    setattr(ehrt, k, getattr(hrt, k))
                    dao.update_record(ehrt)


# store_all_symbols()

# getAllSymbols()[0].symbol
# function = "function=EMA&interval=daily&time_period=200&series_type=open"

# rsi_manager = IndicatorManager(
#     "rsi",
#     "Technical Analysis: RSI",
#     "function=RSI&interval=daily&time_period=200&series_type=open",
#     data1="RSI",
# )

# rsi_manager.store_all_symbols()

# print(rsi_manager.get_all_symbols_as_hrt()[0].date)

print(dao.get_records("AAA"))
