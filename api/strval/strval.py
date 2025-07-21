import random
from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import StringConstraints
from pydantic import AfterValidator

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        for i in q:
            results.update({"q": q})
    return results


# Declaring more metadata for OpenAPI and docs

query = Annotated[str, StringConstraints(min_length=3, max_length=5)]


@app.get("/v2/items/")
async def read_items_v2(
    q: Annotated[query | None, Query(title="Query string", deprecated=True)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Test"}]}
    if q:
        results.update({"q": q})
    return results


# Customer Validator

data = {
    "isbn-123456789": "Samle Book",
    "imdb-987654321": "C Progamming Language",
    "isbn-123456num": "ASM Bare Metal Lang"
}

def check_valid_id(id: str) -> str:
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError("Invalid ID Format, it must start with 'isbn-' or 'imdb-'")
    return id

@app.get("/v3/items")
async def read_items_v3(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id": id, "name": item} 
    

