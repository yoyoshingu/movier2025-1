import pandas as pd
from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from recommender import item_based_recommendation
from resolver import random_items, random_genres_items, random_genres_items_best

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello MovieR"}

@app.get("/all")
async def all_movies():
    result = random_items()
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    result = random_genres_items(genre)
    return {"result": result}

@app.get("/genresbest/{genre}")
async def genre_movies_best(genre: str):
    result = random_genres_items_best(genre)
    return {"result": result}

@app.get("/item_based/{item_id}")
async def item_based(item_id: str):
    result = item_based_recommendation(item_id)
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)