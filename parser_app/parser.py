import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://zdorovie-lab.kg/"
URL = "https://zdorovie-lab.kg/%d1%81%d0%bf%d0%b5%d1%86%d0%b8%d0%b0%d0%bb%d0%b8%d1%81%d1%82%d1%8b/"

HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='row specialists_list')
    mediki = []

    for item in items:
        mediki.append(
            {
                'name': item.find('div', class_='specialists_item_title').get_text(),
                'image': item.find('div', class_='specialists_item_img').find('img').get('src')
            }
        )
        return mediki

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        mediks = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            mediks.extend(get_data(html.text))
            return mediks
    else:
        raise ValueError('Error in parser function')