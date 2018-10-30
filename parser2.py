from requests import get
from bs4 import BeautifulSoup


def soup(url):
    r = get(url)
    return BeautifulSoup(r.text, 'lxml')


counter = 0
s = soup('https://rutracker.org/forum/viewforum.php?f=187')
x = s.findAll('div', {'class': 'torTopic'})
for y in x:
    yy = y
    yy = yy.span
    print(y, end='~~~~')
    print(yy)
    # if yy is not None and yy.text == '&radic':
    #     z = y.find('a', {'class': 'torTopic bold tt-text'}).get('href')
    #     print(z, end=';;;')
    #     print()
    #     counter += 1
    # print(counter)

