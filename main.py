from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema import UserSchema

app = FastAPI()
conn = UserConnection()

@app.get("/")
async def root():
    items = []
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["phone"] = data[2]
        items.append(dictionary)

    return items


@app.post("/api/insert")
async def insert(user_data: UserSchema):
    data = user_data.dict()
    data.pop("id")
    conn.write(data)

@app.get("/api/user/{id}")
async def get_one(id: str):
    dictionary = {}
    data = conn.read(id)
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]

    return dictionary


@app.put("/api/update/{id}")
async def update(user_data: UserSchema, id):
    data = user_data.dict()
    data["id"] = id
    conn.update(data)


@app.delete("/api/delete/{id}")
async def delete(id: str):
    conn.delete(id)