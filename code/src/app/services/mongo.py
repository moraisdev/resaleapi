import pymongo


def mongo_connection():
    mongo = pymongo.MongoClient("db", 27017)
    db_mongo = mongo.resale
    mongo.server_info()
    print(mongo.hostInfo)
    return db_mongo
