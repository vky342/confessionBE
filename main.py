from fastapi import FastAPI, Request, HTTPException
from pymongo import MongoClient
import uvicorn
from config import mycollection, db

app = FastAPI()


@app.post("/receive_data")
async def receive_data(request: Request):
    try:
        data = await request.json()
        if "time" not in data or "content" not in data or "comments" not in data:
            raise HTTPException(status_code=400, detail="Missing required fields: time, content, and comments")

        # Add default empty list for comments if not provided
        if not data["comments"]:
            data["comments"] = []

        result = mycollection.insert_one(data)
        return {"message": "Data inserted successfully", "inserted_id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/retrieve_data")
async def retrieve_data():
    try:
        data = list(mycollection.find({}, {"_id": 0}))  # Exclude _id field from results
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Hello World 3"}