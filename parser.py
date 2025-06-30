from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    # Пример: парсим бренд Adidas (можно изменить на другую страницу)
    driver.get("https://www.sportsdirect.com/adidas/all-adidas")
    time.sleep(5)  # ждём загрузки JS

    products = []

    # Ищем карточки товаров
    items = driver.find_elements(By.CSS_SELECTOR, ".productgrid .item")

    for item in items:
        try:
            name = item.find_element(By.CSS_SELECTOR, ".itemTitle").text.strip()
            url = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            price = item.find_element(By.CSS_SELECTOR, ".pri").text.strip()
            available = 1  # пока считаем все доступными
            products.append({"name": name, "url": url, "price": price, "available": available})
        except Exception as e:
            print("⚠️ Ошибка при парсинге товара:", e)

    driver.quit()

    # Сохраняем в базу
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    for p in products:
        c.execute("INSERT INTO products (name, url, price, available) VALUES (?, ?, ?, ?)",
                  (p["name"], p["url"], p["price"], p["available"]))

    conn.commit()
    conn.close()

    print(f"✅ Сохранено {len(products)} товаров в базу")
