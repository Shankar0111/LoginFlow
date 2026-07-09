from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router  # we'll create this next

app = FastAPI()

# Configure CORS so the frontend (localhost:3000) can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes from routes.py
app.include_router(router)


@app.get("/")
def home():
    return {"message": "LoginFlow backend running successfully!"}
