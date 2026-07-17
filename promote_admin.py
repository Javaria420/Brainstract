from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb://localhost:27017/brainstract")
db = client["brainstract"]
result = db["users"].update_one(
    {"_id": ObjectId("6a128dd0ebf795ddf4055bd6")},
    {"$set": {"role": "admin"}}
)
print(f"Modified: {result.modified_count}")

# Also fetch the user to confirm
user = db["users"].find_one({"_id": ObjectId("6a128dd0ebf795ddf4055bd6")}, {"password": 0})
print(f"User role: {user.get('role')}")
client.close()
