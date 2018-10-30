from requests import get
from bs4 import BeautifulSoup


def soup(url):
    r = get(url)
    return BeautifulSoup(r.text, 'lxml')


s = soup('https://rutracker.org/forum/viewforum.php?f=941')
x = s.find('div', {'class': 'bottom_info pad_2'}).findAll('b')
print(x[1].text)
