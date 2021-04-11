import os 

import json

import uvicorn

from typing import Optional

from fastapi import FastAPI



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
    dir_path = os.path.dirname(os.path.realpath(__file__))
    imdb_json = f'{dir_path}\\data\\imdb.json'
    data = read_json_file(imdb_json)
    return data


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")