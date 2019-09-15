# Задание 25:
# Используя модуль urllib,
# соберите все ссылки на заданной веб-странице (http://google.com)
# и запишите их в файл
import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html, parser)
        with open('log.txt', 'w') as f:
            for tag in sp.find_all('a'):
                url = tag.get('href')
                if url is None:
                    continue
            if 'html' in url:
                print(('\n' + url))
                f.write('\n' + url)


s = 'https://google.com/'
Scraper(s).scrape()
