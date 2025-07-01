import requests

url = "https://www.sportsdirect.com/lonsdale-shorts-and-vest-set-kids-290167"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
}

response = requests.get(url, headers=headers)

print(f"Status code: {response.status_code}")
print(response.text[:1000])  # Выводим первые 1000 символов страницы
