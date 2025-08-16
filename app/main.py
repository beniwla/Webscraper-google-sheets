# app/main.py
import traceback
from fastapi import FastAPI, HTTPException
from app.scrapper import scrape_fifa_world_cup_data
from app.sheets import upload_to_sheet

app = FastAPI(title="FIFA World Cup Scraper API")

@app.get("/")
def root():
    return {"message": "FIFA World Cup API Running"}

@app.get("/scrape")
def scrape_data():
    data = scrape_fifa_world_cup_data()
    return {"message": "Data scraped successfully", "rows": data}

@app.post("/upload")
def upload_data():
    data = scrape_fifa_world_cup_data()
    try:
        result = upload_to_sheet(data)
        return result
    except Exception as e:
        traceback.print_exc()  # logs full error in console
        raise HTTPException(status_code=500, detail=str(e))