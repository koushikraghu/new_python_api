import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
new_db = myclient['rk_db']
mycol = new_db['rk_collection']