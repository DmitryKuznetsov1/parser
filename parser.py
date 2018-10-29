# coding: utf-8
from requests import get, Session
from bs4 import BeautifulSoup
from time import sleep
import requests


def get_href(x):
    return x.get('href')


def get_href_2(x):
    return x.a.get('href')

# s = requests.Session()
# data = {"login_username" : "Dmitry_Kuznetsov", "login_password":"dmitrykuznetsov1998"}
# url_auth = "http://kinopoisk.ru"
# r = s.post(url_auth, data=data)
# s.cookies


main_url = 'https://rutracker.org'
r = get(main_url)


soup = BeautifulSoup(r.text, 'lxml')
_ = soup.find('div', {'class': 'tr_main_cats'})
# category_list = _.findAll('a')
# category_list = list(map(get_href, category_list))
# Фильмы, Наше кино, Артхаус и авторское кино, DVD, HD, Док. фильмы, мультсериалы соответсвенно
category_list = ["viewforum.php?f=7", "viewforum.php?f=22", "viewforum.php?f=124", "viewforum.php?f=93",
                 "viewforum.php?f=2198", "viewforum.php?f=46", "viewforum.php?f=4"]

for i in category_list:
    category_url = 'http://rutracker.org/forum/%s' % (i)
    c = get(category_url)
    soup = BeautifulSoup(c.text, 'lxml')
    _ = soup.find('table', {'class': 'forumline forum'})
    subcategory_list = _.findAll('h4', {'class': 'forumlink'})
    subcategory_list = [x.text for x in subcategory_list]
    # subcategory_list = list(map(get_href, subcategory_list))
    print(subcategory_list)
    # for j in subcategory_list:
    #     subcategory_url = f'http://rutracker.org/forum/{j}'
    #     t = get(subcategory_url)
    #     soup = BeautifulSoup(t, 'lxml')
    # with open('test1.html', 'w', encoding='UTF-8') as output_file:
    #     output_file.write(t.text)
    #
    #
    # if counter == 1:
    #     break
