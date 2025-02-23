from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://wanqichen0924:anime@animedb.t7coi.mongodb.net/?retryWrites=true&w=majority&appName=AnimeDB")

client = MongoClient(MONGO_URI)
db = client["anime_db"]
print("Connected to MongoDB Atlas!", db.list_collection_names())
