import requests
from bs4 import BeautifulSoup

def parse_sportsdirect():
    url = "https://www.sportsdirect.com/brands"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    items = []

    # Пример: собрать ссылки на бренды (позже заменим на товары)
    for a in soup.select("a.anchor-brand"):  # нужно будет проверить точный селектор
        name = a.get_text(strip=True)
        link = a["href"]
        items.append({"name": name, "url": link})

    return items

if __name__ == "__main__":
    data = parse_sportsdirect()
    print(data)
