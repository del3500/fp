from fastapi import FastAPI
from fastapi import Query
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


# Ordering matters. See 2 functions below
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


# Enum
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name is ModelName.resnet:
        return {"model_name": model_name, "message": "leCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# Query paramater, type conversion, usage of union/optional/defaults
# Required query parameter
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str, short: bool = True):
    item = {"item_id": item_id, "q": q}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


items = [
    {"id": 1, "name": "Wireless Mouse", "price": 25.99},
    {"id": 2, "name": "Keyboard", "price": 45.50},
    {"id": 3, "name": "Monitor", "price": 199.99},
    {"id": 4, "name": "USB-C Cable", "price": 9.99},
    {"id": 5, "name": "Laptop Stand", "price": 34.95},
    {"id": 6, "name": "Bluetooth Speaker", "price": 59.00},
    {"id": 7, "name": "Webcam", "price": 89.49},
    {"id": 8, "name": "External Hard Drive", "price": 120.00},
    {"id": 9, "name": "Desk Lamp", "price": 18.75},
    {"id": 10, "name": "Notebook Cooler", "price": 22.40},
]


#Query from FastAPI
@app.get("/equipments")
async def get_equipments(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0, le=50)
):
    return items[skip : skip + limit]
