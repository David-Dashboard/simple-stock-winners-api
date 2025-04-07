from typing import Union

from fastapi import FastAPI
import app.data as data

DATABASE_PATH = "tests/test_database.csv"
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
@app.get("/get_stock_winners")
def get_stock_winners():
    return data.get_stock_winners(data.read_database (DATABASE_PATH))