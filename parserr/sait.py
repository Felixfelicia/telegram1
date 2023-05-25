import requests
from bs4 import BeautifulSoup

URL = "https://kaktus.media/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36 Edg/113.0.1774.50"
}


def get_html(url):
    response = requests.get(url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="Dashboard-Board--content", limit=4)
    parsed_data = []
    for item in items:
        title_element = item.find('a', class_='Dashboard-Content-Card--name')
        if title_element is not None:
            title = title_element.text.strip()
            url = title_element.get('href')
            parsed_data.append({
                "title": title,
                "url": url,
            })
    return parsed_data


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        parsed_data = get_data(html.text)
        return parsed_data
    raise Exception("Ошибка в парсере!")
