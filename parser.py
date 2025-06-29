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
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Временные тестовые записи
    products = [
        {"name": "Test Product 1", "url": "https://example.com/1", "price": "£100", "available": 1},
        {"name": "Test Product 2", "url": "https://example.com/2", "price": "£150", "available": 1},
    ]

    for p in products:
        c.execute("INSERT INTO products (name, url, price, available) VALUES (?, ?, ?, ?)",
                  (p["name"], p["url"], p["price"], p["available"]))

    conn.commit()
    conn.close()

    print(f"✅ Сохранено {len(products)} тестовых записей")
