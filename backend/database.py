from motor.motor_asyncio import AsyncIOMotorClient

# Local MongoDB connection
MONGO_URL = "mongodb://localhost:27017"

# Database name
DB_NAME = "loginflow_db"

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
