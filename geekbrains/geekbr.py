# -*- coding: utf-8 -*-

import requests, csv
from lxml import html

sess = requests.Session()
sess.get('https://geekbrains.ru/login')
#emaill = 
#проверка на 422!!!!!!!!!!!!!!
sess.post('https://geekbrains.ru/login', {
	'utf8': '✓',
	'authenticity_token': 'CTVDLHXK4gFXkbdXRRwPv7IjE+Tpna1ikCqrzP4mgvJGCgkguV4gjVH1+GL+m+g==',
     'user[email]': 'eleasddsa@gmail.com',
     'user[password]': '123456qwe89',
     'user[remember_me]': 1})
sess.post('https://geekbrains.ru/login', {
	'utf8': '✓',
	'authenticity_token': sess.cookies['remember_user_token'],
     'user[email]': 'eleasddsa@gmail.com',
     'user[password]': '123456qwe89',
     'user[remember_me]': 1})

def html_page(linkk):
    page = sess.get(linkk)
    root = html.fromstring(page.text)
    root.make_links_absolute('https://geekbrains.ru')
    return root

def dict_event(link_ev):
    root_ev = html_page(link_ev)
    l0 = root_ev.body.find_class('row')[0][0][1].text
    #print(root_ev.body.find_class('row')[0][0][1].text)
    #print(root_ev.find_class('row')[0][0].getchildren())
    if root_ev.body.find_class('row')[0][0][4].tag == 'video':
        l1 = 'mp4'
        l2 = root_ev.body.find_class('row')[0][0][4][0].attrib['src']
    elif root_ev.body.find_class('row')[0][0][4][0].tag == 'iframe':
        l1 = 'youtube'
        l2 = root_ev.body.find_class('row')[0][0][4][0].attrib['src']
    else:
        l1 = '-'
        l2 = '-'
    l3 = html.tostring(root_ev.body.find_class('row')[0][0][5]).decode('cp1251')
    return {'title': l0, 'serv': l1, 'link': l2, 'content': l3}
#req_page = sess.get('https://geekbrains.ru/events#all')

#print(page1.text)
#root = html.fromstring(req_page.text)
root = html_page('https://geekbrains.ru/events#all')
list_names = root.find_class('row flex')[0].getchildren()
list_events = []


for name in list_names: # переделать под одну сессию
    print('%s/attend' % name[0].attrib['href'])
    sess.get('%s/attend' % name[0].attrib['href'])
    list_events.append(dict_event(name[0].attrib['href']))
    

with open('names.csv', 'w') as csv_file:
    column_names = ['title', 'serv', 'link', 'content']
    writer = csv.DictWriter(csv_file, fieldnames=column_names, delimiter='|')

    writer.writeheader() #write first row
    writer.writerows(list_events)
