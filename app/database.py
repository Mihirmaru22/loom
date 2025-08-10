from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "finance_db"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]