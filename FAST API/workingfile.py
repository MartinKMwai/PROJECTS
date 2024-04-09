from fastapi import FastAPI

app = FastAPI()

# @app.get("/")

# def home():
#     return {"Data":"Test"}

# @app.get("/about")
# def about():
#     return {"Data":"About"}

#Path parameters 
inventory = {
    1: {"name": "apple", "price": 100},
    2: {"name": "yorghurt", "price": 50},
    3: {"name": "apple juice", "price": 30},
    4: {"name": " luncheon meat", "price": 50},
    5: {"name": "mince beef", "price": 60}
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]