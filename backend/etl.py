from pymongo import MongoClient # type: ignore
from dotenv import load_dotenv # type: ignore
import ssl
import requests
import pandas as pd
import os

# # Connect to MongoDB in local
# client = MongoClient("mongodb://localhost:27017/")
# db = client["anime_db"]
# collection = db["anime_rankings"]

load_dotenv() # Load enviornment variable from .env file
mongo_url = os.getenv("MONGO_URI")
if not mongo_url:
    raise ValueError("MONGO_URI environment variable is not set.")
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
    
    """Saves anime rankings DataFrame to MongoDB after clearing old data."""
    if df is not None and not df.empty: 
        collection.delete_many({})  # Clear old data
        collection.insert_many(df.to_dict(orient="records"))
        print("Data updated in MongoDB!")
    else: 
        print("No data to save to MongoDB.")

if __name__ == "__main__":
    df = fetch_anime_rankings()
    
    if df is not None:
        # print(df.head()) # Preview data befor saving
        save_to_mongo(df)

        df.to_csv("anime_ranking.csv", index=False)
    
    else:
        print("No data retrieved, skipping MogoDB save.")

