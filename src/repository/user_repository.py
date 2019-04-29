import json
from bson.json_util import dumps
from bson import ObjectId

from database_config import get_db_connection_obj

client = get_db_connection_obj()
db = client.get_default_database()

user_collection = db["user"]

def find_all():
    try:
        return (json.loads(dumps(user_collection.find().limit(100))))
    except:
        print("Error happened")

def create(user):
    try:
        user_collection.insert(user)
        return (json.loads(dumps(user)))
    except:
        print("Error happened")
