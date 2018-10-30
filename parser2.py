from requests import get
from bs4 import BeautifulSoup


def soup(url):
    r = get(url)
    return BeautifulSoup(r.text, 'lxml')


s = soup('https://rutracker.org/forum/viewforum.php?f=941')
_ = s.find('div', {'class': 'bottom_info pad_2'})
#    subcategory_list = _.findAll('h4', {'class': 'forumlink'})
print(_)
