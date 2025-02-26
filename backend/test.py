# from pymongo import MongoClient
# import os

# MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://wanqichen0924:anime@animedb.t7coi.mongodb.net/?retryWrites=true&w=majority&appName=AnimeDB")

# client = MongoClient(MONGO_URI)
# db = client["anime_db"]
# print("Connected to MongoDB Atlas!", db.list_collection_names())

from pymongo import MongoClient
import certifi

mongo_uri = "mongodb+srv://wanqichen0924:anime@animedb.t7coi.mongodb.net/?retryWrites=true&w=majority&appName=AnimeDB"

try:
    client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
    db = client["anime_db"]
    print("MongoDB Connection Successful!")
except Exception as e:
    print("MongoDB Connection Failed:", e)
