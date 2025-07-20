from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import StringConstraints

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        for i in q:
            results.update({"q": q})
    return results


# Declaring more metadata for OpenAPI and docs 
# TODO: update query param of v2

query = Annotated[str, StringConstraint(min_length=3, max_length=5)]

@app.get("/v2/items/")
async def read_items_v2(
    q: Annotated[list[str] | None, Query(title="Query string", min_length=3)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Test"}]}
    if q:
        results.update({"q": q})
    return results
