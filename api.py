from fastapi import FastAPI, Request

app = FastAPI()

# In-memory storage for demo purposes
items = []

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items")
async def get_items():
    return items

@app.post("/items")
async def create_item(request: Request):
    item = await request.json()
    items.append(item)
    return {"message": "Item created successfully"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if 0 <= item_id < len(items):
        return items[item_id]
    return {"message": "Item not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)