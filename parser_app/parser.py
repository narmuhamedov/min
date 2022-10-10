import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "http://medcenter-kgma.kg/"
URL = "http://medcenter-kgma.kg/doctors.html"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='items-row cols-2 row-0 row-fluid clearfix')
    mediki = []

    for item in items:
        mediki.append(
            {
                 'name': item.find('div', class_='page-header').get_text(),
                'image': item.find('div', class_='cat-left').find('img').get('src')
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