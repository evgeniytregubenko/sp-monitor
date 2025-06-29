import requests
from bs4 import BeautifulSoup

def parse_sportsdirect():
    url = "https://www.sportsdirect.com/brands"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(resp.text, "html.parser")
    items = []

    # Временный пример — берём все ссылки с текстом
    for a in soup.find_all("a", href=True):
        name = a.get_text(strip=True)
        link = a["href"]
        if name and "/brands/" in link:
            items.append({"name": name, "url": "https://www.sportsdirect.com" + link})

    return items
