Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from lxml import html
>>> import requests
>>> sess = requests.Session()
>>> sess.auth = ('eleasddsa@gmail.com', '123456qwe89')
>>> req_page = sess.get('https://geekbrains.ru/events#all')
>>> root = html.fromstring(req_page.text)
>>> list_names = root.body.find_class('row flex')
>>> list_names
[<Element div at 0x46a0330>]
>>> len(list_names)
1
>>> list_names = root.body.find_class('row flex')[0].getchildren()
>>> len(list_names)
221
>>> list_names[9][1]
<Element div at 0x46a0330>
>>> list_names[9][1][0]
<Element a at 0x46b6570>
>>> list_names[9][1][0][0].text
'MySQL. Оптимизируем запросы'
>>> list_names[9][1][0].values('href')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list_names[9][1][0].values('href')
TypeError: values() takes no arguments (1 given)
>>> list_names[9][1][0].attrib
{'href': '/events/239'}
>>> list_names[9][1][0].attrib('')
KeyboardInterrupt
>>> list_names[9][1][0].attrib('href')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list_names[9][1][0].attrib('href')
TypeError: 'lxml.etree._Attrib' object is not callable
>>> 
KeyboardInterrupt
>>> list_names[9][1][0].attrib['href']
'/events/239'
>>> req_page.cookies
<RequestsCookieJar[Cookie(version=0, name='_session_id', value='UjZhK2ZNK1Z5MzRzM2xKVnBycVNwVFAyYmYvRFNscDdJWHJzSHFNQlZnODZmS2QxamxWSWFxK1VxeGhONm02UHJUdG51UHdET2ltSzVxQkYzWkNwQ21ILy9VT2V2MHZydDYvRXE3cjB5amhFK3FxajY5cHVKY2tiTHovZC9kK2EtLUd6WEtkYmNHZEQxd2RES2d3TEpHYkE9PQ%3D%3D--b504e1e83c5c285fd1b7cf01faed3448a0dea5f9', port=None, port_specified=False, domain='geekbrains.ru', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)]>
>>> import csv
>>> with open('c:/1.mp4','wb') as out:
	ree = requests.get('https://www.youtube.com/cb1adbfb-4bf1-4763-b126-f92ded9b1269', stream=True)
	for chuck in ree.iter_content(1024):
		out.write(chuck)

		
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    with open('c:/1.mp4','wb') as out:
PermissionError: [Errno 13] Permission denied: 'c:/1.mp4'
>>> with open('1.mp4','wb') as out:
	ree = requests.get('https://www.youtube.com/cb1adbfb-4bf1-4763-b126-f92ded9b1269', stream=True)
	for chuck in ree.iter_content(1024):
		out.write(chuck)

		
513
>>> spamWriter = csv.writer(open('eggs.csv', 'w'), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
>>> spamWriter.writerow(['Spam'] * 5 + ['Baked Beans'])
40
>>> spamWriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
37
>>> del spamWriter
>>> with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    
13
13
16
>>> with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar='|')

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    
13
13
16
>>> with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=' ')

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    
13
13
16
>>> with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

    
13
13
16
>>> 'link_ev'.join('/qwe')
'/link_evqlink_evwlink_eve'
>>> str.join('link_ev','/qwe')
'/link_evqlink_evwlink_eve'
>>> os.path.join('link_ev','qwe')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    os.path.join('link_ev','qwe')
NameError: name 'os' is not defined
>>> import os
>>> os.path.join('link_ev','qwe')
'link_ev\\qwe'
>>> page = sess.get('https://geekbrains.ru/events/6/attend')
>>> root = html.fromstring(page.text)
>>> l1 = root.body.find_class('row')[0]getchilren()[0].[1].text
SyntaxError: invalid syntax
>>> l1 = root.body.find_class('row')[0].getchilren()[0].[1].text
SyntaxError: invalid syntax
>>> l1 = root.body.find_class('row')[0].getchilren()[0][1].text
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    l1 = root.body.find_class('row')[0].getchilren()[0][1].text
AttributeError: 'HtmlElement' object has no attribute 'getchilren'
>>> l1 = root.body.find_class('row')[0].getchilren()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    l1 = root.body.find_class('row')[0].getchilren()
AttributeError: 'HtmlElement' object has no attribute 'getchilren'
>>> l1 = root.body.find_class('row')[0][0][1]
>>> l1 = root.body.find_class('row')[0][0][1].text
>>> l1
>>> l1 = root.body.find_class('row')[0][0][1]
>>> l1
<InputElement 42391e0 name='authenticity_token' type='hidden'>
>>> root_ev.body.find_class('row')[0].getchildren()[0].getchildren()[1].text
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    root_ev.body.find_class('row')[0].getchildren()[0].getchildren()[1].text
NameError: name 'root_ev' is not defined
>>> root.body.find_class('row')[0].getchildren()[0].getchildren()[1].text
>>> root.body.find_class('row')[0].getchildren()[0].getchildren()[1]
<InputElement 42391e0 name='authenticity_token' type='hidden'>
>>> root.body.find_class('row')[0]
<Element div at 0x42394b0>
>>> root.body.find_class('row')[0][0]
<Element form at 0x4239570>
>>> root.body.find_class('row')[0][0][0]
<InputElement 4239540 name='utf8' type='hidden'>
>>> root.body.find_class('row')[0].getchildren()
[<Element form at 0x4239510>]
>>> root.body.find_class('row')
[<Element div at 0x4239570>]
>>> len(root.body.find_class('row'))
1
>>> len(root.body.find_class('row')[0].getchildren())
1
>>> len(root.body.find_class('row')[0].getchildren()[0].getchildren())
11
>>> oot.body.find_class('row')[0].getchildren()[0].getchildren()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    oot.body.find_class('row')[0].getchildren()[0].getchildren()
NameError: name 'oot' is not defined
>>> root.body.find_class('row')[0].getchildren()[0].getchildren()[1]
<InputElement 42391e0 name='authenticity_token' type='hidden'>
>>> root.body.find_class('row')[0].getchildren()[0].getchildren()[0]
<InputElement 4239510 name='utf8' type='hidden'>
>>> root.body.find_class('row')[0].getchildren()[0].getchildren()[3]
<InputElement 4239600 name='user[email]' type='email'>
>>> page.cookies
<RequestsCookieJar[Cookie(version=0, name='_session_id', value='WFJyVjFFL1ArVFFLWGwrQ2wzaXFJcUpIME1xamZ5QkFZdmwwM0VyNGhnQ2pEMmtwU1hyeGJyTzFtVUltdlRNN29NY01ybXpLSmcrbis4RDh5RW10Q2JuRThiaVExdGY0MWs2NXZjNkh0UUFnWkxjd05rRXZYM1VvYTc5Q1hBNEhIT2VLV2pPY29WMWRmcThHOUZCeVcveGNnOEoySU9sSGlIWVJQWEg1M3JzNXJhZFl3dzVCZU1sczdhR1FMY1Yyam90TDdjM3Z2b3g3ZVNxQlRENnRpcXVCQU90cEowTkVmbkh5MVlXdjE5OEJCK1Flanp4aFpPODJ5RWdlNGQwaWdRY3BDcm1aQW9xSThhOUdXcWlSL3c5SFkrM2t6Q1luby9VT3V2SDZQK1ArTUFXQWk5bHVQVGtoT1ZEY05QMUdKT3ljQTFFZGRHczN5c01KODFTczJob0xrV2VnOTVGNzdZaDViV2g5UUQ0PS0tdzRndzJYNGtGcktLWGRnbkE1SEQ3dz09--9d68b6e002cece52f8cb4b74006dae9a0ed1ef62', port=None, port_specified=False, domain='geekbrains.ru', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)]>
>>> sess.auth = ('eleasddsa@gmail.com', '123456qwe89')
>>> page = sess.get('https://geekbrains.ru/events/6/attend')
>>> root = html.fromstring(page.text)
>>> root.body.find_class('row')[0].getchildren()
[<Element form at 0x422b990>]
>>> sess.post('https://geekbrains.ru/login', {
     'username': 'eleasddsa@gmail.com',
     'password': '123456qwe89',
     'remember': 1,
})
<Response [422]>

>>> sess.post('https://geekbrains.ru/login', {
     'username': 'eleasddsa@gmail.com',
     'password': '123456qwe89',
     'remember': 1})
<Response [422]>


>>> page = sess.get('https://geekbrains.ru/events/6/attend')
>>> root = html.fromstring(page.text)
>>> root.body.find_class('row')[0].getchildren()
[<Element form at 0x468ba20>]
>>> 
