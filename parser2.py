from requests import get, Session
from bs4 import BeautifulSoup
from time import sleep
import requests
import csv
import random
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '68.0.3440.106 YaBrowser/18.9.0.3467 Yowser/2.5 Safari/537.36'}

# proxies = {'http': 'socks5://roskomnadzor:Ug9dp9mpHscK4NtKsUgV@94.130.184.58:1080',
#            'https': 'socks5://roskomnadzor:Ug9dp9mpHscK4NtKsUgV@94.130.184.58:1080'}
def convert(a):
    return a.text
csv_file = 'movies.csv'


#cookies
s = requests.Session()
data = {"login_username": "Dmitry_Kuznetsov", "login_password":"dmitrykuznetsov1998"}
url_auth = "http://kinopoisk.ru"
r = s.post(url_auth, data=data)
s.cookies
counter = 0


a = [i for i in range(926)]
random.shuffle(a)

for i in a:
    main_url = f'https://www.kinopoisk.ru/top/navigator/m_act[num_vote]/100/m_act[rating]/1%3A/order/rating/page/' \
               f'{i + 1}/#results'
    r = get(main_url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    film_list = soup.find('div', {'class': 'tenItems'})
    els = film_list.findAll('div', {'class': 'name'})
    for name in els:
        movie_name = name.find('a').text
        counter += 1
        print(counter, movie_name)
        with open(csv_file, 'a', encoding='UTF-8', newline='') as file:
            movie = [counter, movie_name]
            writer = csv.writer(file, delimiter='~')
            writer.writerow(movie)
    sleep(random.uniform(60, 600))
