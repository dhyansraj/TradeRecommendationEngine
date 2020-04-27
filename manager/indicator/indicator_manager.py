import requests
import json
import csv
import time
import trade_dao as dao
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

    def download_data(self, sym):
        symbol = "&symbol=" + sym

        url = IndicatorManager.site + self.function + symbol + self.apiKey

        print(url)

        response = requests.get(url)

        return (
            "{}".content.decode("utf-8")
            if response in (None, "")
            else json.loads(response.content.decode("utf-8"))
        )

    def store(self, sym):

        downloaded_data = self.download_data(sym)

        if self.key in downloaded_data:
            with open(self.store_at + sym + ".json", "w") as outfile:
                json.dump(downloaded_data, outfile)
        else:
            print(downloaded_data)

    def get_stored_symbols(self):
        from os import listdir
        from os.path import isfile, join

        files = [f for f in listdir(self.store_at) if isfile(join(self.store_at, f))]
        return files

    def clean_data(self, symbol, date, row):
        data = {}

        data["_id"] = symbol + ":" + date
        data["symbol"] = symbol
        data["date"] = date

        for k in self.data:
            data[k] = float(row[self.data[k]])

        return data

    def get_symbol_data(self, data, symbol):
        symbol_data = []
        if self.key in data:
            for k in data[self.key]:
                symbol_data.append(self.clean_data(symbol, k, data[self.key][k]))

        return symbol_data

    def get_all_symbols_from_disk(self):
        all_symbols = []
        for f in self.get_stored_symbols():
            symbol = f.split(".")[0]
            with open(self.store_at + f) as jfile:
                data = json.load(jfile)

                all_symbols.extend(self.get_symbol_data(data, symbol))
        return all_symbols

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

    def store_all_symbols_on_db_live(self, daily_rates=False):
        with open("nasdaqlisted.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter="|")
            i = 0
            for row in reader:
                sym = row["Symbol"]

                self.store_all_symbols_on_db(
                    self.get_symbol_data(self.download_data(sym), sym), daily_rates
                )
                i += 1

                if i % 5 == 0:
                    time.sleep(60)

    def store_all_symbols_on_db(self, all_symbols, daily_rates=False):

        if daily_rates:
            dao.create_record(all_symbols)
        else:
            existing_records = set([i["_id"] for i in dao.get_all_records()])
            all_symbols = list(
                filter(lambda x: x["_id"] in existing_records, all_symbols)
            )
            for record in all_symbols:
                dao.update_record(record)


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

# print(dao.get_records("AAA"))


# manager = IndicatorManager(
#     "daily_rates",
#     "5B2SMYIVORAAHUVQ",
#     "Time Series (Daily)",
#     "function=TIME_SERIES_DAILY",
#     data0="1. open",
#     data1="2. high",
#     data2="3. low",
#     data3="4. close",
#     data4="5. volume",
# )

# manager.store_all_symbols_on_db(manager.get_all_symbols_from_disk(), True)
# manager.get_all_symbols_from_disk()[0]


# manager = IndicatorManager(
#     "adx",
#     "MOARBV4V30DX6V4O",
#     "Technical Analysis: ADX",
#     "function=ADX&interval=daily&time_period=200",
#     data13="ADX",
# )
# # e = {"_id": "LNT:2020-04-23", "symbol": "LNT", "date": "2020-04-23", "data13": 6.0011}

# manager.get_all_symbols_from_disk()[0]

# list(filter(lambda x: x["_id"] in er, manager.get_all_symbols_from_disk()))[0]

# manager = IndicatorManager(
#     "aroon",
#     "YNECR52IM6Y24UD4",
#     "Technical Analysis: AROON",
#     "function=AROON&interval=daily&time_period=200",
#     data15="Aroon Up",
#     data16="Aroon Down",
# )

# manager.store_all_symbols_on_db(manager.get_all_symbols_from_disk())
