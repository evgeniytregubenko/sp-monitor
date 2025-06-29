from flask import Flask, render_template_string, redirect, url_for
import parser
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    # Читаем записи из базы
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT name, url, price, available, last_checked FROM products ORDER BY id DESC")
    products = c.fetchall()
    conn.close()

    html = """
    <h2>✅ Приложение запущено!</h2>
    <a href="/run-parser">
        <button style="padding:10px 20px; font-size:16px;">Запустить парсер</button>
    </a>
    <h3>Товары:</h3>
    <table border="1" cellpadding="5">
        <tr><th>Название</th><th>URL</th><th>Цена</th><th>В наличии</th><th>Последняя проверка</th></tr>
    """
    for p in products:
        html += f"<tr><td>{p[0]}</td><td><a href='{p[1]}'>Ссылка</a></td><td>{p[2]}</td><td>{p[3]}</td><td>{p[4]}</td></tr>"
    html += "</table>"
    return render_template_string(html)

@app.route("/run-parser")
def run_parser():
    parser.init_db()
    parser.parse_sportsdirect()
    return redirect(url_for('home'))
