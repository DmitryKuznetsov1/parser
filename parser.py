# coding: utf-8
from requests import get, Session
from bs4 import BeautifulSoup
import re


def rus_name(name):
    pattern = re.compile(r'[()]')
    a = pattern.split(name, maxsplit=1)
    b = a[0].split(r'/')
    c = b[0].rstrip()
    return c


def soup(url):
    u = get(url).text
    return BeautifulSoup(u, 'lxml')


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
count = 0
name_rus_list = []
# проходим по всех категориям
for i in category_list_href:
    category_url = 'http://rutracker.org/forum/%s' % (i)
    c = get(category_url)
    soup = BeautifulSoup(c.text, 'lxml')
    _ = soup.find('table', {'class': 'forumline forum'})
    subcategory_list = _.findAll('h4', {'class': 'forumlink'})
    subcategory_list = [[x.a.get('href'), x.text] for x in subcategory_list]
    counter = -1
    for x in range(len(subcategory_list)):
        counter += 1
        y = subcategory_list[counter][1].lower()
        if not(('фильмы' in y or 'кино' in y or 'кине' in y) and ('архив' not in y) and ('ищу' not in y)):
            subcategory_list.pop(counter)
            counter -= 1
    for j in range(len(subcategory_list)):
        z = subcategory_list[j][0]
        subcategory_url = 'http://rutracker.org/forum/%s' % (z)
        u = get(subcategory_url).text
        s = BeautifulSoup(u, 'lxml')
        x = s.find('div', {'class': 'bottom_info pad_2'}).findAll('b')
        for k in range(int(x[1].text)):
            subcategory_url_page = subcategory_url + '&start=%s' % (k*50)
            u = get(subcategory_url_page).text
            s = BeautifulSoup(u, 'lxml')
            x = s.findAll('div', {'class': 'torTopic'})
            for y in x:
                yy = y
                yy = yy.span
                if yy is not None and yy.text == '√':
                    count += 1
                    z = y.find('a', {'class': 'torTopic bold tt-text'}).get('href')
                    w = y.find('a', {'class': 'torTopic bold tt-text'}).text
                    result = re.split(r'/', w)
                    w = result[0].rstrip().lstrip()
                    name_rus = rus_name(w)
                    if name_rus not in name_rus_list:
                        name_rus_list.append(name_rus)
                    print(count, name_rus)
                    print(name_rus_list)
            #         counter += 1
            # print(counter)
