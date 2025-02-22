from fastapi import FastAPI # type: ignore
from pymongo import MongoClient # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["anime_db"]
collection = db["anime_rankings"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def home():
    return {"message": "Anime popularity Dashboard API"}

@app.get("/anime-rankings")
def get_anime_rankings():
    anime_list = list(collection.find({}, {"_id": 0})) # Exclude MongoDB ID
    return {"data": anime_list}