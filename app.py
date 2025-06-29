from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Приложение запущено! Парсер пока отключен из-за таймаута."
