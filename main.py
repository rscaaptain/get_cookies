from fastapi import FastAPI
import undetected_chromedriver as uc
import time

app = FastAPI()

@app.get("/get-cookies")
def get_cookies(url: str):
    options = uc.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')

    driver = uc.Chrome(options=options)
    
    driver.get(url)
    time.sleep(10)
    
    cookies = driver.get_cookies()
    driver.quit()
    
    return {"cookies": cookies}