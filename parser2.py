from requests import get
from bs4 import BeautifulSoup


def soup(url):
    r = get(url)
    return BeautifulSoup(r.text, 'lxml')


s = soup('https://rutracker.org/forum/viewforum.php?f=187')
x = s.findAll('div', {'class': 'torTopic'})
for y in x:
    if y is not None:
        y = y.span.text
        print(y, end='')
        print()
