from fastapi import FastAPI
import undetected_chromedriver as uc
import time
import pymysql

app = FastAPI()

@app.get("/")
def update_cookies():
    url = "https://shop.garena.my/"
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

    connection = pymysql.connect(
        host='gateway01.eu-central-1.prod.aws.tidbcloud.com',
        port=4000,
        user='3A6TaGgYi7CaDM1.root',
        password='tiy9rHALwhwfMLB5',
        database='free_fire',
        ssl={"reject_hostname": False}
    )

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO cookies (name, value) VALUES (%s, %s) ON DUPLICATE KEY UPDATE value = VALUES(value)"
            for cookie in cookies:
                cursor.execute(sql, (cookie['name'], cookie['value']))
        connection.commit()
    finally:
        connection.close()
    
    return {"status": "success", "message": "Cookies successfully updated in database"}