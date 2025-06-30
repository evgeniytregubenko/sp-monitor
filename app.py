from flask import Flask, render_template_string
import parser
import sqlite3

app = Flask(__name__)

# Создаём таблицу при старте
parser.init_db()

@app.route("/")
def home():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT name, url, price, available, last_checked FROM products ORDER BY id DESC")
    products = c.fetchall()
    conn.close()

    html = """
    <h2>✅ Приложение запущено!</h2>
    <p>Таблица обновляется автоматически через cron (каждые 4 часа).</p>
    <h3>Товары:</h3>
    <table border="1" cellpadding="5">
        <tr><th>Название</th><th>URL</th><th>Цена</th><th>В наличии</th><th>Последняя проверка</th></tr>
    """
    for p in products:
        html += f"<tr><td>{p[0]}</td><td><a href='{p[1]}'>Ссылка</a></td><td>{p[2]}</td><td>{p[3]}</td><td>{p[4]}</td></tr>"
    html += "</table>"
    return render_template_string(html)

@app.route("/run-parser-cron")
def run_parser_cron():
    parser.parse_sportsdirect()
    return "✅ Парсер запущен по cron!"
