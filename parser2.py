from requests import get
from bs4 import BeautifulSoup


def soup(url):
    r = get(url)
    return BeautifulSoup(r.text, 'lxml')


s = soup('https://rutracker.org/forum/viewforum.php?f=187')
x = s.findAll('div', {'class': 'torTopic'})
x = [y.span for y in x]
print(x)
