from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Get frontend URL from environment variable
frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
print(f"🌐 Allowing CORS from: {frontend_url}")

# Add CORS middleware to allow requests from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],  # Dynamic frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "FastAPI Backend is running by Danish!"}


@app.post("/open-image")
def open_image():
    """
    This endpoint returns a random message
    """
    messages = [
        "🎉 Button click successful!",
        "✅ Request received from Frontend!",
        "🚀 Backend is working perfectly!",
        "💡 REST API call successful!",
        "🔥 Frontend-Backend communication works!",
        "⭐ You're learning FastAPI well!",
        "🎯 Endpoint executed successfully!",
    ]

    random_message = random.choice(messages)

    return {
        "success": True,
        "message": random_message,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
