from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

# @app.get("/")

# def home():
#     return {"Data":"Test"}

# @app.get("/about")
# def about():
#     return {"Data":"About"}

#Path parameters 
inventory = {
    1: {"name": "Apple", "price": 100},
    2: {"name": "Yoghurt", "price": 50},
    3: {"name": "Apple Juice", "price": 30},
    4: {"name": "Macadamia Nuts", "price": 50},
    5: {"name": "Coffee", "price": 60}
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description = "The ID of the item you'd like to view", gt = 0, le = 5)):
    return inventory[item_id]

@app.get("/get-by-name")
def get_name(*, name: Optional [str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Error":"Data not Found" } 
