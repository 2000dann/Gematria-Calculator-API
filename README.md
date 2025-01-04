# Gematria Calculator API

## Overview

The Gematria Calculator API is a FastAPI-based application that provides tools for calculating gematria values for Hebrew and English texts. 
The application supports standard gematria calculations, Atbash cipher transformations, and gematria value matching in predefined texts. 
It also includes an upload feature to process files for gematria calculations.

**What is Gematria?**

Gematria is an alphanumeric code where letters correspond to numbers. It is primarily used in Hebrew, though adaptations exist for other languages like English. In Hebrew, gematria has historical and mystical significance, often used in scriptural analysis and Kabbalistic studies. In English, it serves a more exploratory or cryptographic purpose.

**Differences Between Hebrew and English Gematria**

Hebrew gematria assigns numerical values based on the traditional order of the Hebrew alphabet (Aleph = 1, Bet = 2, etc.). Larger numbers are represented by combining letter values (e.g., Yod = 10).

English gematria adapts similar principles, with variations like assigning values sequentially (A = 1, B = 2, etc.) or using systems inspired by Hebrew gematria.

**What is the Atbash Cipher?**

The Atbash cipher is a substitution cipher where each letter in the alphabet is replaced with its reverse counterpart. For example, in Hebrew, Aleph (first letter) becomes Tav (last letter), and Bet becomes Shin. In English, A becomes Z, B becomes Y, and so on. Originally developed for cryptographic purposes, the Atbash cipher is also studied for its esoteric and symbolic applications in ancient texts.


## Features

**Standard Gematria Calculations**: Calculate gematria values for Hebrew and English texts.

**Atbash Cipher Transformation**: Perform Atbash cipher transformations on Hebrew texts.

**File Upload**: Find passages from predefined texts with matching gematria values.

**CORS Support**: Allow integration with frontend applications.

## GOALS

**1.** Enable accurate gematria calculations for Hebrew and English texts.

**2.** Provide an accessible API for developers interested in gematria-related tools.

**3.** Allow users to explore matches for gematria values in ancient and esoteric texts.

**4.** Facilitate experimentation with Atbash cipher and other cryptographic methods

## Prerequisites

**Python 3.8 or higher**

**pip**

**git**

**Node.js and npm setup**

## Installation

## Step 1: Clone the Repository

**git clone https://github.com/2000dann/Gematria-Calculator-API.git**

**cd gematria-calculator**

## Step 2: Install dependencies for the Backend

**pip install -r requirements.txt**

## Step 3: Navigate to the frontend directory and install frontend dependencies

**cd frontend**

**npm install**

# Step 4: Run the backend server

**cd ..**

**uvicorn main:app --reload**

# Step 5: Run the frontend server

**cd frontend**

**npm install**

## Accessing the application:

**Backend API:** http://127.0.0.1:8000

**Frontend:** http://localhost:3000


**---------------------------------**

**---------------------------------**


## Usage

The Gematria Calculator API allows users to calculate and explore gematria values using various methods. It is accessible via endpoints detailed below.

To use the API:

**1.** Ensure the backend server is running (uvicorn main:app --reload).

**2.** Use a browser or an API testing tool (e.g., Postman) to access the endpoints.

For example, to calculate gematria for the word "hello" using the standard method:

**3.** Open your browser and navigate to http://127.0.0.1:8000/calculate?word=hello&method=standard.

The server will respond with the calculated gematria value.

**4.** For endpoints requiring POST requests, like file upload:

Use an API testing tool to send requests with the required parameters.

**5.** For the frontend application:

Access http://localhost:3000 in your browser to interact with the graphical user interface that integrates API functionalities.

## Endpoints

**Welcome Message**

**--Endpoint:** /

**--Method:** GET

**--Description:** Returns a welcome message.

**Standard and Atbash Gematria Calculation**

**--Endpoint:** /calculate

**--Method**: GET

**--Parameters:**

----word: The word to calculate gematria for.

----method: standard (default) or atbash.

**--Description:** Calculates gematria using the specified method.

**Hebrew and English Gematria Calculation**

**--Endpoint:** /gematria

**--Method:** GET

**--Parameters:**

----text: The text to calculate gematria for.

----system: hebrew (default) or english.

**--Description:** Calculates gematria for a given text in the specified system.

**Find Matches for Gematria Value**

**--Endpoint:** /gematria/match

**--Method:** GET

**--Parameters:**

----value: The gematria value to search for.

----system: hebrew (default) or english.

**--Description:** Finds text passages matching the given gematria value.

**Upload File for Gematria Calculation**

**--Endpoint:** /upload/

**--Method:** POST

**--Parameters:**

----file: File to upload.

----system: hebrew (default) or english.

**--Description:** Processes the uploaded file and calculates gematria for its contents.


## Project Structure

**gematria-calculator/** 

**|-- app/**

**|  |  |-- gematria.py**       # Functions for gematria calculations

**|  |  |-- texts.py**          # Predefined texts for matching

**|  |   |-- main.py**           # Main FastAPI application

**|  |   |-- static/**           # Static files directory

**|-- requirements.txt**      # Python dependencies

**|-- frontend/**             # React-based frontend application

**|-- README.md**             # Project documentation

## Tech Stack

**Backend:** FastAPI (Python)

**Deployment:** Uvicorn server

**Utilities:** Concurrent threading for background tasks

**Middleare:** CORS for frontend-backend interaction

## Future Improvements:

-- Add support for additional cryptographic methods.

--Develop a frontend for interactive use

--Optimize performance for larger datasets

## Contribution Guidelines:

**1.** Fork the repository

**2.** Create new branch

**git checkout -b branch_name**

**3.** Commit changes and push to forked repository

**4.** Submit pull request with description of changes

## License

This project is licensed under the MIT License.


