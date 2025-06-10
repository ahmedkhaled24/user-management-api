from fastapi import APIRouter, HTTPException
from bson import ObjectId
from models import UserModel, UpdateUserModel
from database import user_collection

user_router = APIRouter()

@user_router.post("/user")
async def create_user(user: UserModel):
    result = await user_collection.insert_one(user.dict())
    return {"id": str(result.inserted_id)}


@user_router.get("/users")
async def get_users():
    users = []
    async for user in user_collection.find():
        user["id"] = str(user["_id"])
        del user["_id"]
        users.append(user)
    return users


@user_router.get("/user/{id}")
async def get_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["id"] = str(user["_id"])
    del user["_id"]
    return user

    
@user_router.get("/userByName/{name}")
async def get_user_by_name(name: str):
    users = []
    async for user in user_collection.find():
        if(user["name"] == name):
            user["id"] = str(user["_id"])
            del user["_id"]
            users.append(user)
    return users                      

@user_router.put("/user/{id}")
async def update_user(id: str, user: UpdateUserModel):
    result = await user_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {k: v for k, v in user.dict().items() if v is not None}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}



@user_router.delete("/user/{id}")
async def delete_user(id: str):
    result = await user_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
