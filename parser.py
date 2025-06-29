from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sqlite3

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

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.sportsdirect.com/brands")
    time.sleep(5)  # ждем загрузки

    elems = driver.find_elements("css selector", "a.Anchor-cms-link")
    products = []

    for e in elems:
        name = e.text.strip()
        url = e.get_attribute("href")
        if name and url:
            products.append({"name": name, "url": url, "price": "?", "available": 1})

    driver.quit()

    # Сохраняем в базу
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    for p in products:
        c.execute("INSERT INTO products (name, url, price, available) VALUES (?, ?, ?, ?)",
                  (p["name"], p["url"], p["price"], p["available"]))

    conn.commit()
    conn.close()

    print(f"✅ Сохранено {len(products)} записей в базу")

if __name__ == "__main__":
    init_db()
    parse_sportsdirect()
