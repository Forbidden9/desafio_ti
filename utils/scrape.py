import requests
from bs4 import BeautifulSoup


def generate_url(year: int) -> str:
    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm"
    return url


def get_page(url: str) -> BeautifulSoup:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_value_x_date(year: int, month: int, day: int) -> float:
    url = generate_url(year)
    page = get_page(url)

    table = page.find('table', class_='table', id='table_export')

    lists = []

    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')
        lists.append(columns[month].text)
    return lists[day]
