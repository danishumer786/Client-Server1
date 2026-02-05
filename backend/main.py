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
    return {"message": "FastAPI Backend is running!"}


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


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import subprocess
# import os

# app = FastAPI()

# # Add CORS middleware to allow requests from React frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # React development server
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def read_root():
#     return {"message": "FastAPI Backend is running!"}


# @app.post("/open-image")
# def open_image():
#     """
#     This endpoint opens the server.png image when called
#     """
#     try:
#         # Path to the image file
#         image_path = r"\\photonix04\Interdepartmental Coordination\Danish Mohammed\testing\server.png"

#         print(f"DEBUG: Checking path: {image_path}")
#         print(f"DEBUG: Path exists: {os.path.exists(image_path)}")
#         print(f"DEBUG: Is file: {os.path.isfile(image_path)}")

#         # Check if file exists
#         if os.path.exists(image_path):
#             print(f"DEBUG: Opening file...")
#             # Open the image using default system application
#             subprocess.Popen(f'explorer /select,"{image_path}"')
#             return {
#                 "success": True,
#                 "message": "Image opened successfully!",
#                 "path": image_path,
#             }
#         else:
#             # List files in directory
#             dir_path = os.path.dirname(image_path)
#             print(f"DEBUG: Directory path: {dir_path}")
#             if os.path.exists(dir_path):
#                 print(f"DEBUG: Files in directory: {os.listdir(dir_path)}")
#             return {
#                 "success": False,
#                 "message": f"Image not found at path: {image_path}",
#                 "debug_info": f"Directory exists: {os.path.exists(dir_path)}",
#             }
#     except Exception as e:
#         print(f"DEBUG: Error - {str(e)}")
#         return {"success": False, "message": f"Error opening image: {str(e)}"}


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)
