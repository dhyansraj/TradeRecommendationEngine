from util import fromisoformat
import pymongo

mdb_client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
db = mdb_client["tre_database"]
hd = db["historical_data"]


def create_record(data):
    try:
        hd.insert_many(data)
    except pymongo.errors.BulkWriteError:
        pass


def update_record(record):

    query = {}

    query["_id"] = record.pop("_id")

    values = {"$set": record}

    hd.update_one(query, values)


def get_all_records():

    return list(hd.find())


def get_records(symbol):
    query = {"symbol": {"$eq": symbol}}
    return list(hd.find(query).sort("date", -1))


def get_symbols_list():
    return list(hd.find({}, {"symbol": 1}).distinct("symbol"))


# def get_records(symbol):
#     Session = sessionmaker()
#     Session.configure(bind=engine)
#     session = Session()

#     try:
#         row = (
#             session.query(HistoricalRatesTable)
#             .filter(HistoricalRatesTable.symbol == symbol)
#             .order_by(HistoricalRatesTable.date.desc())
#         )

#         return row.all()
#     except SQLAlchemyError as e:
#         print(e)
#     finally:
#         session.close()


# def get_symbols_list():
#     Session = sessionmaker()
#     Session.configure(bind=engine)
#     session = Session()

#     try:
#         row = (
#             session.query(HistoricalRatesTable.symbol)
#             .distinct(HistoricalRatesTable.symbol)
#             .group_by(HistoricalRatesTable.symbol)
#         )

#         return row.all()
#     except SQLAlchemyError as e:
#         print(e)
#     finally:
#         session.close()


# def get_unique_record(symbol, date):
#     Session = sessionmaker()
#     Session.configure(bind=engine)
#     session = Session()

#     try:
#         row = (
#             session.query(HistoricalRatesTable)
#             .filter(HistoricalRatesTable.symbol == symbol)
#             .filter(HistoricalRatesTable.date == date)
#             .first()
#         )

#         return row
#     except SQLAlchemyError as e:
#         print(e)
#     finally:
#         session.close()


# create_table()

# {(str(i.symbol) + ":" + str(i.date), i) for i in get_all_records()]

# {str(i.symbol) + ":" + str(i.date):i for i in get_all_records()}

# get_records("AAPL")[99]

# print(len(get_symbols_list()))
