import pymongo

connection_obj = pymongo.MongoClient("mongodb://chetan:chetan36@ds052968.mlab.com:52968/practiceapp")
print("Database connection successful")

def get_db_connection_obj():
    return connection_obj
