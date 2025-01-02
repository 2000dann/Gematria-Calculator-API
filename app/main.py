## Imports
import logging
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from enum import Enum
from app.gematria import (
    calculate_hebrew_gematria,
    calculate_english_gematria,
    atbash_cipher
)
from fastapi.staticfiles import StaticFiles
from app.texts import texts
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from pydantic import BaseModel
import asyncio 

## Logging Configuration
logging.basicConfig(level=logging.INFO)

## Background Threading
executor = ThreadPoolExecutor(max_workers = 4)

class GematriaSystem (str, Enum):
    hebrew = "hebrew"
    english = "english"

## Main application object to manage routes, middleware and app config

app = FastAPI()

# Mount static filess
app.mount("/static", StaticFiles(directory="app/static"), name="static")


## Ensures Requests from frontend are allowed
## Prevents browser security policies from blocking cross-origin requests.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.on_event("shutdown")
def shutdown_event():
    executor.shutdown(wait=True)

    
# Welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the Gematria Calculator API!"}


## Background task for Gematria calculations
def background_calculate_gematria(text: str, system: str):
    if system == "hebrew":
        return calculate_hebrew_gematria(text)
    elif system == "english":
        return calculate_english_gematria(text)
    else:
        raise ValueError("Unsupported gematria system")


# Standard and Atbash gematria endpoint
@app.get("/calculate")
def calculate(word: str, method: str = "standard"):
    if method == "standard":
        value = calculate_hebrew_gematria(word)
    elif method == "atbash":
        value = atbash_cipher(word)
    else:
        return {"error": "Invalid method. Choose 'standard' or 'atbash'."}
    return {"word": word, "method": method, "value": value}


# Hebrew and English gematria endpoint
@app.get("/gematria")
async def calculate_gematria(text: str, system: str = "hebrew"):
    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(executor, background_calculate_gematria, text, system)
        return {"text": text, "system": system, "gematria": result}
    except ValueError as e:
        return {"error": str(e)}


# Find matches for a given gematria value in predefined texts
@app.get("/gematria/match")
def find_matches(value: int, system: str = "hebrew"):
    matches = []
    for passage in texts:
        if system == "hebrew":
            gematria_value = calculate_hebrew_gematria(passage["text"])
        elif system == "english":
            gematria_value = calculate_english_gematria(passage["text"])
        else:
            return {"error": "Unsupported gematria system"}
        
        if gematria_value == value:
            matches.append({"text": passage["text"], "source": passage["source"]})
    return {"value": value, "system": system, "matches": matches}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), system: str = "hebrew"):
    content = await file.read() # Read file content
    text = content.decode("utf-8") # Decode it to a string
    loop = asyncio.get_event_loop()
    try:
        gematria_value = await loop.run_in_executor(executor, process_uploaded_file, text, system)
        return {"filename": file.filename, "system": system, "gematria": gematria_value}
    except ValueError as e:
        return {"error": str(e)}

  
        