from flask import Flask, render_template_string
from parser import parse_sportsdirect

app = Flask(__name__)

@app.route("/")
def home():
    items = parse_sportsdirect()
    html = "<h2>Тест парсера SportsDirect</h2><ul>"
    for item in items:
        html += f"<li><a href='{item['url']}'>{item['name']}</a></li>"
    html += "</ul>"
    return html
