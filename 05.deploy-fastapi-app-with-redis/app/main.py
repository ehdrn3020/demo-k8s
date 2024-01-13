from fastapi import FastAPI
from redis_config import redis_config
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/redis_test")
async def redis_test():
    rd = redis_config()
    rd.set("juice", "orange")
    return {
        "data":rd.get("juice")  # get
    }