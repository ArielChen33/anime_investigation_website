from pymongo import MongoClient # type: ignore
import ssl
import requests
import pandas as pd
import os

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")
# db = client["anime_db"]
# collection = db["anime_rankings"]

mongo_url = "mongodb+srv://wanqichen0924:anime@animedb.t7coi.mongodb.net/?retryWrites=true&w=majority&appName=AnimeDB"
client = MongoClient(mongo_url, tls=True, tlsCertificateKeyFile=None, ssl=True)
db = client["AnimeDB"]  # Use the correct database name
collection = db["anime_rankings"]



JIKAN_API_URL = "https://api.jikan.moe/v4/top/anime"

def fetch_anime_rankings():
    response = requests.get(JIKAN_API_URL)
    if response.status_code == 200: 
        data = response.json()
        anime_list = data["data"]
        df = pd.DataFrame([{
            "title": anime["title_japanese"],  
            "rank": anime["rank"], 
            "score": anime["score"], 
            "popularity": anime["popularity"],
            "members": anime["members"], 
            "aired_from": anime["aired"]["from"] if anime["aired"] else None, 
        } for anime in anime_list])
        return df
    return None


def save_to_mongo(df):    
    # mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    # mongo_uri = os.getenv("MONGO_URI", "mongodb+srv://wanqichen0924:anime@animedb.t7coi.mongodb.net/?retryWrites=true&w=majority&appName=AnimeDB")
    # client = MongoClient(mongo_uri)
    # db = client["anime_db"] 
    # collection = db["anime_rankings"]
    
    collection.delete_many({})  # Clear old data
    collection.insert_many(df.to_dict(orient="records"))
    print("Data updated in MongoDB!")

if __name__ == "__main__":
    df = fetch_anime_rankings()
    # print(df.head()) # Preview the data
    if df is not None:
        save_to_mongo(df)

    df.to_csv("anime_ranking.csv", index=False)

