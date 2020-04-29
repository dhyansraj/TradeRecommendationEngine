import pymongo

mdb_client = pymongo.MongoClient("mongodb://admin:admin@10.128.0.2:27017/")
db = mdb_client["tre_database"]
hd = db["historical_data"]


def create_record(data):
    try:
        hd.insert_many(data)
    except Exception:
        pass


def update_record(record):

    query = {}

    query["_id"] = record.pop("_id")

    values = {"$set": record}

    hd.update_one(query, values)


def get_all_records():

    return list(hd.find())


def get_records(symbol, limit=0, date=None):
    query = {"symbol": {"$eq": symbol}}

    if date:
        query["date"] = {"$lt": date}
    return list(hd.find(query).sort("date", -1).limit(limit))


def get_symbols_list():
    return list(hd.find({}, {"symbol": 1}).distinct("symbol"))


# len(get_records("AAPL", date="2020-01-17"))

# get_symbols_list()
