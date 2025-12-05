## Setup
------------------------------------------------------------------------------------
# Scraping Backend Setup : To run the RSS scraping backend, you must activate the Python virtual environment and start the module manually.
# 1. Activate the virtual environment

# win :
source backend/venv/Scripts/activate 
# mac/linux : 
source backend/venv/bin/activate


# 2. Start the scraping module
python -m backend.api

# Keep this terminal open and running.  
# The scraper must stay active for the website to display updated data.
# For the website to work correctly, you must have two terminals running at the same time
------------------------------------------------------------------------------------
Make sure to install dependencies:

```bash
# npm
npm install

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

## Production

Build the application for production:

```bash
# npm
npm run build

```
