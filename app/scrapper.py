# app/scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_fifa_world_cup_data(limit: int = 10):
    driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals")
    time.sleep(2)

    data = []

    for i in range(1, limit + 1):
        base = f"//table[contains(@class,'sortable')]/tbody/tr[{i}]"
        try:
            year = driver.find_element(By.XPATH, base + "/th").text.strip()
            winner = driver.find_element(By.XPATH, base + "/td[1]").text.strip()
            score = driver.find_element(By.XPATH, base + "/td[2]").text.strip()
            runner_up = driver.find_element(By.XPATH, base + "/td[3]").text.strip()
            data.append([year, winner, score, runner_up])
        except Exception as e:
            print(f"[ERROR] Row {i} failed: {e}")

    driver.quit()
    return data

