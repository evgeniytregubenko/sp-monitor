from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Приложение запущено!"

@app.route("/test-connection")
def test_connection():
    try:
        url = "https://www.sportsdirect.com/"
        response = requests.get(url, timeout=10)
        return f"Status: {response.status_code}\n\n{response.text[:500]}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
