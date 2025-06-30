from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sqlite3
import time

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT,
            price TEXT,
            available INTEGER,
            last_checked DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def parse_sportsdirect():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-data-dir=/tmp/chrome-data")

    driver = webdriver.Chrome(options=options)

    # Открываем конкретный товар (пример)
    url = "https://www.sportsdirect.com/adidas-runfalcon-3-trainers-mens-121002#colcode=12100203"
    driver.get(url)
    wait = WebDriverWait(driver, 15)
    time.sleep(5)  # ждём загрузки

    name = driver.find_element(By.CSS_SELECTOR, "h1").text.strip()
    price_elem = wait.until(EC.presence_of_element_located((By.ID, "lblSellingPrice")))
    price = price_elem.text.strip()
    available = 1

    driver.quit()

    # Сохраняем в базу
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (name, url, price, available) VALUES (?, ?, ?, ?)",
              (name, url, price, available))
    conn.commit()
    conn.close()

    print(f"✅ Сохранён товар: {name}, цена: {price}")

