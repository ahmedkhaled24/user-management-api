﻿from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017/")
database = client["user_api"]
user_collection = database.get_collection("users")
