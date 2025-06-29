from flask import Flask, render_template_string, redirect, url_for
import parser

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <h2>✅ Приложение запущено!</h2>
    <a href="/run-parser">
        <button style="padding:10px 20px; font-size:16px;">Запустить парсер</button>
    </a>
    """
    return render_template_string(html)

@app.route("/run-parser")
def run_parser():
    parser.init_db()
    parser.parse_sportsdirect()
    return redirect(url_for('home'))
