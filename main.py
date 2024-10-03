from fastapi import FastAPI, Request, HTTPException
from pymongo import MongoClient
import uvicorn
from config import mycollection, db
import uuid

app = FastAPI()


@app.post("/receive_data")
async def receive_data(request: Request):
    try:
        data = await request.json()
        if "time" not in data or "content" not in data:
            raise HTTPException(status_code=400, detail="Missing required fields: time, content, and comments")

        
        data["comments"] = []

        # Generate a unique ID (replace with your preferred method)
        data["id"] = str(uuid.uuid4())  # Using the uuid library
        print(data)
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


@app.post("/add_comment/{confession_id}")
async def add_comment(confession_id: str, request: Request):
    try:
        comment_data = await request.json()

        # Find the confession document
        confession = mycollection.find_one({"id": confession_id})
        if not confession:
            raise HTTPException(status_code=404, detail="Confession not found")


        # Add the comment to the existing comments list
        confession["comments"].append(comment_data["data"])
        print(comment_data)
        # Update the confession document
        result = mycollection.update_one({"_id": confession["_id"]}, {"$set": confession})
        if result.modified_count == 0:
            raise HTTPException(status_code=500, detail="Failed to update confession")

        return {"message": "Comment added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Hello World 3"}