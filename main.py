from typing import Union

from fastapi import FastAPI
import data

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/get_stock_winners")
def get_stock_winners():
    return data.get_stock_winners()