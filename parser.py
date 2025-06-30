from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    options.add_argument("--user-data-dir=/tmp/chrome-data")

    driver = webdriver.Chrome(options=options)

    url = "https://www.sportsdirect.com/lonsdale-shorts-and-vest-set-kids-290167"
    driver.get(url)

    wait = WebDriverWait(driver, 30)

    driver.save_screenshot("/tmp/screen.png")  # 💥 Добавляем

    # Ждем заголовок
    name_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
    name = name_elem.text.strip()

    # Ждем цену по ID
    price_elem = wait.until(EC.presence_of_element_located((By.ID, "lblSellingPrice")))
    price = price_elem.text.strip()

    available = 1  # считаем, что товар доступен

    driver.quit()

    # Сохраняем в базу
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (name, url, price, available) VALUES (?, ?, ?, ?)",
              (name, url, price, available))
    conn.commit()
    conn.close()

    print(f"✅ Сохранён товар: {name}, цена: {price}")

if __name__ == "__main__":
    init_db()
    parse_sportsdirect()
