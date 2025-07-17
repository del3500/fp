from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    percent_tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.percent_tax is not None:
        taxed = item.price + (item.price * item.percent_tax / 100)
        item_dict.update({"price_with_tax": taxed})
    return item_dict
