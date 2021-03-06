import json
from bson.json_util import dumps
from bson import ObjectId
import dateutil
import datetime
import copy

from database_config import get_db_connection_obj

client = get_db_connection_obj()
db = client.get_default_database()

user_collection = db["user"]

def find_all():
    try:
        return (json.loads(dumps(user_collection.find().limit(100))))
    except:
        print("Error happened")

def find_by_id(user_id):
    try:
        return json.loads(dumps(user_collection.find_one({"id": int(user_id)})))
    except:
        print("Error happened")

def create(user):
    try:
        last_id = 0
        documents = json.loads(dumps(user_collection.find().sort("id", -1).limit(1)))
        if (len(documents) > 0):
            last_id = documents[0]["id"]
        user["id"] = last_id + 1
        user["createdAt"] = datetime.datetime.now()
        user["updatedAt"] = datetime.datetime.now()
        user_collection.insert(user)
        return (json.loads(dumps(user)))
    except:
        print("Error happened")

def update(user_id, user):
    try:
        db_user = json.loads(dumps(user_collection.find_one({"id": int(user_id)})))
        updated_user = {
            "id": db_user["id"],
            "name": user["name"],
            "email": user["email"],
            "password": user["password"],
            "createdAt": datetime.datetime.fromtimestamp(int(db_user["createdAt"]["$date"]) / 1000),
            "updatedAt": datetime.datetime.now()
        }
        user_collection.update({"id": int(user_id)}, updated_user, upsert=True)
        return (json.loads(dumps(updated_user)))
    except:
        print("Error happened")
