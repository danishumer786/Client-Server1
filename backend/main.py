from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Get frontend URLs - support both development and production
localhost_url = "http://localhost:3000"
production_url = "https://salmon-island-0c4d7891e.1.azurestaticapps.net"

# Allow both development and production frontend URLs
allowed_origins = [localhost_url, production_url]
print(f"🌐 Allowing CORS from: {allowed_origins}")

# Add CORS middleware to allow requests from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Both localhost and production URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "FastAPI Backend is running by Danish!"}


@app.get("/info")
def get_info():
    return {
        "app_name": "Client-Server Backend",
        "version": "1.0.0",
        "developer": "Danish",
        "framework": "FastAPI",
        "status": "Active"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": "2026-02-05", "uptime": "running"}


@app.get("/quote")
def random_quote():
    quotes = [
        {"quote": "Code never lies, comments sometimes do.", "author": "Ron Jeffries"},
        {"quote": "First, solve the problem. Then, write the code.", "author": "John Johnson"},
        {"quote": "Experience is the name everyone gives to their mistakes.", "author": "Oscar Wilde"},
        {"quote": "In order to be irreplaceable, one must always be different.", "author": "Coco Chanel"},
        {"quote": "Java is to JavaScript what car is to Carpet.", "author": "Chris Heilmann"}
    ]
    return random.choice(quotes)


@app.get("/numbers/{num}")
def get_number_info(num: int):
    return {
        "number": num,
        "square": num * num,
        "cube": num * num * num,
        "is_even": num % 2 == 0,
        "is_positive": num > 0
    }


@app.get("/greet/{name}")
def greet_user(name: str):
    return {
        "greeting": f"Hello {name}!",
        "message": f"Welcome to Danish's FastAPI Backend, {name}!",
        "length": len(name)
    }


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
