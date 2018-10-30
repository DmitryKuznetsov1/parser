from requests import get
from bs4 import BeautifulSoup


def soup(url):
    r = get(url)
    return BeautifulSoup(r.text, 'lxml')


counter = 0
s = soup('https://rutracker.org/forum/viewforum.php?f=187')
x = s.findAll('div', {'class': 'torTopic'})
for y in x:
    z = y.find('a', {'class': 'torTopic bold tt-text'}).get('href')
    print(z, end=';;;')
    print()
    counter += 1
print(counter)
# for y in x:
#     print(y, end='---')
#     print()
# x = [y.span for y in x]
# for y in x:
#     if y is not None:
#         y = y.text
#         print(y, end=' ')
