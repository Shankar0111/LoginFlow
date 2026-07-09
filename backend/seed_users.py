import asyncio
import bcrypt
from database import db

TEST_USERS = [
    {"username": "admin", "email": "admin@example.com", "password": "admin123"},
    {"username": "user1", "email": "user1@example.com", "password": "pass1"},
    {"username": "user2", "email": "user2@example.com", "password": "pass2"},
    {"username": "user3", "email": "user3@example.com", "password": "pass3"},
    {"username": "tester", "email": "tester@example.com", "password": "test123"},
    {"username": "guest", "email": "guest@example.com", "password": "guest123"},
    {"username": "shankar", "email": "developer@example.com", "password": "RATbat@1"}
]

async def seed_users():
    for user in TEST_USERS:
        existing = await db["users"].find_one({"username": user["username"]})
        if existing:
            print(f"Skipping existing user: {user['username']}")
            continue

        hashed_pw = bcrypt.hashpw(user["password"].encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        await db["users"].insert_one({
            "username": user["username"],
            "email": user["email"],
            "password": hashed_pw,
        })
        print(f"Seeded user: {user['username']}")

    print("Test users seeding complete.")

if __name__ == "__main__":
    asyncio.run(seed_users())
