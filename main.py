from typing import Any

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/shipment")
def get_shipment():
    return {
        "id":1,
        "origin":"New York"
    }

@app.get("/shipment/{id}")
def get_shipment_by_id(id: int ):
    return {
        "id":id,
        "origin": "New Yor",
        "code":["NY","US","001"]
    }

# Return type validation
@app.get("/order/{id}")
def get_order_by_id(id: int | str | Any)  -> dict[str,int | list[int]]:
    return {
        "orderid":id,
        "amount":100,
        "quantity":2,
        "price":[50,50]

    }

# Query Parameters
@app.get("/items/{item_id}")
def read_item(item_id: int) ->dict[str,Any]:
    return {
        "item_id":item_id,
        "name":"item name"
    }

# write query paramter example

@app.get("/search/")
def search_item(q: str | None = None):
    return {
        "q":q,
        "item": "item name"
    }

@app.get("/users")
def get_users(id: int, location: str,contact: int, country: str | None = None):
    return {
        "id":id,
        "location":location,
        "country":country,
    }



@app.post("/booking")
def booking(data:dict) -> dict[str,Any]:
    return data;











