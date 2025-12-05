# Project Setup Guide
------------------------------------------------------------------------------------

## Scraping Backend Setup

To run the RSS scraping scraping, you must create and activate the Python virtual environment, install scraping dependencies, and start the scraper manually.

### 1. Create the virtual environment (only once)
python -m venv scraping/venv

### 2. Activate the virtual environment
# Windows (bash)
source scraping/venv/Scripts/activate

# macOS / Linux
source scraping/venv/bin/activate

### 3. Install scraping dependencies
pip install flask
pip install flask_cors
pip install requests
pip install feedparser
pip install APScheduler


### 4. Start the scraping module
python -m scraping.api

# IMPORTANT
# Keep this terminal open.
# The scraper must remain active for the website to display updated data.
# For the website to work correctly, you must keep two terminals running:
# 1. Terminal 1 -> scraping scraper (python -m scraping.api)
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





# #2f0538