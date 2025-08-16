# app/sheets.py
import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
SHEET_ID = "1koeKcUPZ4JhUPuj7f1Gn21a2foexXHR5CO6GDuGZw1M"

def get_google_sheet():
    creds = Credentials.from_service_account_file("C:\\Users\\shees\\Desktop\\Tennr\\credentials.json", scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(SHEET_ID).sheet1
    return sheet

def upload_to_sheet(data: list):
    sheet = get_google_sheet()
    sheet.clear()
    sheet.update("A1", [["Year", "Winner", "Score", "Runner-up"]] + data)
    return {"status": "success", "rows_uploaded": len(data)}
