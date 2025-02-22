# Anime Investigation Website

This project investigates the popularity of anime by fetching ranking data from the [Jikan API](https://jikan.moe/). It stores the data in MongoDB and provides a backend for further analysis or visualization.

## Tecknique

### Backend

- Python (FastAPI)
- MongoDB
- Pandas (for ETL processing)

### Frontend:

- React
- Recharts for D3.js (for visualizing anime trends)

### Version Control:

- Github Actions (for automating data updates)
- Git (version control)

## Features

- Fetch top anime rankings from Jikan API
- Store the data in MongoDB
- Provide an API endpoint to access stored anime data
- Interactive dashboard for visualizing trends

## How to run the project

### Setup backend

1. Install dependencies

   `pip install fastapi pymongo pandas requests uvicorn
`

2. Run the ETL script to fetch and store anime rankings
   `python backend/etl.py
`

3. Start the FastAPI server:
   `uvicorn backend.app:app --reload
`

### Setup Frontend

1. Navigate to the frontend directory:
   `cd frontend`

2. Install dependencies and start React app:
   `npm install`
   `npm start`

## Future improvements

- Add filtering/search functionality for anime rankings.
- Automate data updates using GitHub Actions + MongoDB.
- Improve visualization with D3.js & Power BI integration.
