from fastapi import FastAPI
from model.user_connection import UserConnection
from schema.user_schema import UserSchema

app = FastAPI()
conn = UserConnection()

@app.get("/")
async def root():
    return conn.read_all()

@app.post("/api/insert")
async def insert(user_data: UserSchema):
    data = user_data.dict()
    data.pop("id")
    conn.write(data)