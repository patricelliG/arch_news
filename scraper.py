#!/usr/bin/env python3

import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.archlinux.org/news/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

body = soup.body

updates = {}
for row in body.find_all('tr'):
    (date, change, author) = row.text.split('\n')[1:4]
    print('date: {}\nchange: {}\nauthor: {}\n'.format(date, change, author))
    updates[date] = change

