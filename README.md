# Project Setup Guide
------------------------------------------------------------------------------------

## Scraping Backend Setup

To run the RSS scraping backend, you must create and activate the Python virtual environment, install backend dependencies, and start the scraper manually.

### 1. Create the virtual environment (only once)
python -m venv backend/venv

### 2. Activate the virtual environment
# Windows
backend\venv\Scripts\activate

# macOS / Linux
source backend/venv/bin/activate

### 3. Install backend dependencies
pip install flask
pip install flask_cors
pip install requests
pip install feedparser

### 4. Start the scraping module
python -m backend.api

# IMPORTANT
# Keep this terminal open.
# The scraper must remain active for the website to display updated data.
# For the website to work correctly, you must keep two terminals running:
# 1. Terminal 1 -> backend scraper (python -m backend.api)
# 2. Terminal 2 -> frontend dev server (npm run dev)

------------------------------------------------------------------------------------

## Frontend Setup

### Install dependencies
npm install

### Development Server
# Starts the dev server on http://localhost:3000
npm run dev

### Production Build
npm run build

------------------------------------------------------------------------------------
