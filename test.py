import pymongo

myclient = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# mydict = {"_id": "test:123", "name": "John", "address": "Highway 37"}

# x = mycol.insert_one(mydict)


myquery = {"_id": "test:123"}
newvalues = {"$set": {"zip": "08816"}}

mycol.update_one(myquery, newvalues)
