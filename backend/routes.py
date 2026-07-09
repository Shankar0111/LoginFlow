from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import db
import bcrypt

router = APIRouter()

# Pydantic models
class User(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str

# Signup route
@router.post("/signup")
async def signup(user: User):
    existing_user = await db["users"].find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    user_dict = user.dict()
    user_dict["password"] = hashed_pw.decode("utf-8")

    await db["users"].insert_one(user_dict)
    return {"message": "User registered successfully"}

# Login route
@router.post("/login")
async def login(login: Login):
    user = await db["users"].find_one({"username": login.username})
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not bcrypt.checkpw(login.password.encode("utf-8"), user["password"].encode("utf-8")):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"message": "Login successful"}
