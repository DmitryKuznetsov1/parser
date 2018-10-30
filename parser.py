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
# Фильмы, Наше кино, Артхаус и авторское кино, DVD, HD, Мультсериалы соответсвенно
category_list_href = ["viewforum.php?f=7", "viewforum.php?f=22", "viewforum.php?f=124", "viewforum.php?f=93",
                 "viewforum.php?f=2198", "viewforum.php?f=4"]

for i in category_list_href:
    category_url = 'http://rutracker.org/forum/%s' % (i)
    c = get(category_url)
    soup = BeautifulSoup(c.text, 'lxml')
    _ = soup.find('table', {'class': 'forumline forum'})
    subcategory_list = _.findAll('h4', {'class': 'forumlink'})
    # subcategory_list_href = [x.a.get('href') for x in subcategory_list]
    # subcategory_list_name = [x.text for x in subcategory_list]
    subcategory_list = [[x.a.get('href'), x.text] for x in subcategory_list]
    counter = -1
    for x in range(len(subcategory_list)):
        counter += 1
        y = subcategory_list[counter][1].lower()
        if not(('фильмы' in y or 'кино' in y or 'кине' in y) and 'архив' not in y):
            subcategory_list.pop(counter)
            counter -= 1

    # print(subcategory_list_name)
    for j in subcategory_list:
        print(j)
    #     subcategory_url = f'http://rutracker.org/forum/{j}'
    #     t = get(subcategory_url)
    #     soup = BeautifulSoup(t, 'lxml')
    # with open('test1.html', 'w', encoding='UTF-8') as output_file:
    #     output_file.write(t.text)

