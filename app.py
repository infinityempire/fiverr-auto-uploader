import os, time, json
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("FIVERR_EMAIL")
PASSWORD = os.getenv("FIVERR_PASSWORD")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1200,800")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

print("🔑 Logging in to Fiverr...")
driver.get("https://www.fiverr.com/login")
try:
    driver.find_element(By.NAME, "email").send_keys(EMAIL)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
except Exception as e:
    print("⚠️ Login fields not found or missing env:", e)

time.sleep(8)
print("✅ Logged (or attempted). Proceeding to load gigs...")

gigs = json.loads(Path("gigs.json").read_text())
for gig in gigs:
    print("🚀 Creating gig:", gig["title"])
    driver.get("https://www.fiverr.com/gigs/create")
    time.sleep(5)
    try:
        title_el = driver.find_element(By.CSS_SELECTOR, "input[placeholder*='I will']")
        title_el.clear(); title_el.send_keys(gig["title"])
        desc_el = driver.find_element(By.TAG_NAME, "textarea")
        desc_el.clear(); desc_el.send_keys(gig["description"])
    except Exception as e:
        print("⚠️ Could not auto-fill full gig:", e)
    print("✅ Attempted gig:", gig["title"])
    time.sleep(2)

print("🎯 All gigs processed (attempted). Check Fiverr dashboard.")
driver.quit()
