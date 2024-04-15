from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

# @app.get("/")

# def home():
#     return {"Data":"Test"}

# @app.get("/about")
# def about():
#     return {"Data":"About"}

#Path parameters 
inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description = "The ID of the item you'd like to view", gt = 0, le = 5)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_name(*, name: str = Query(None, title = "Name", description = "Name of Item", max_length = 8, min_length = 2)):
    for item_id in inventory:
        if inventory[item_id].name== name:
            return inventory[item_id]
    return {"Error":"Data not Found"}

#post request
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {" Redundant": f"Item with id {item_id} already exists"}
    inventory[item_id] = Item
    return inventory[item_id]



