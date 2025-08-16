# FIFA World Cup Final Scraper

This project scrapes the first 10 rows of the FIFA World Cup Final table from Wikipedia and appends them to a Google Sheet via API.

## Endpoints

- `/scrape`: Scrape and return the data
- `/upload`: Scrape and upload to Google Sheets

## Setup

- Install ChromeDriver and place it in your PATH.
- Create a Google service account and download `credentials.json`.
- Add your email to the spreadsheet sharing list.
- Run: `uvicorn app.main:app --reload`
