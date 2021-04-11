import json

from typing import Optional

from fastapi import FastAPI

import uvicorn

def read_json_file(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data
         

app = FastAPI()


@app.get("/")
def read_root():
    return {"HOST": f'IP'}


@app.get("/imdb")
def read_imdb():
    return read_json_file('./data/imdb.json')


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")