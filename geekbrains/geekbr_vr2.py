Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> sess = requests.Session()
>>> sess.auth = requests.HTTPDigestAuth('eleasddsa@gmail.com', '123456qwe89')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sess.auth = requests.HTTPDigestAuth('eleasddsa@gmail.com', '123456qwe89')
AttributeError: 'module' object has no attribute 'HTTPDigestAuth'
>>> sess.auth = requests.auth.HTTPDigestAuth('eleasddsa@gmail.com', '123456qwe89')
>>> page = sess.get('https://geekbrains.ru/events/6/attend')
>>>  root = html.fromstring(page.text)
 
SyntaxError: unexpected indent
>>> root = html.fromstring(page.text)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    root = html.fromstring(page.text)
NameError: name 'html' is not defined
>>> from lxml import html
>>> root = html.fromstring(page.text)
>>> root.body.find_class('row')[0].getchildren()
[<Element form at 0x4400180>]
>>> sess.post('https://geekbrains.ru/login')
<Response [422]>
>>> page = sess.get('https://geekbrains.ru/events/6/attend')
>>> root = html.fromstring(page.text)
>>> root.body.find_class('row')[0].getchildren()
[<Element form at 0x430fe70>]
>>> login = 'eleasddsa@gmail.com'
>>> password = '123456qwe89'
>>> url = 'https://geekbrains.ru/login'
>>> headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
    'DNT':'1'
}
>>> session = requests.session()
>>> data = session.get(url, headers=headers).content
>>> page = html.fromstring(data)
>>> form = page.forms[3]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    form = page.forms[3]
IndexError: list index out of range
>>> form = page.forms[0]
>>> form = page.forms[1]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    form = page.forms[1]
IndexError: list index out of range
>>> form = page.forms[0]
>>> form.fields['user_email'] = login
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    form.fields['user_email'] = login
  File "C:\Python34\lib\site-packages\lxml\html\__init__.py", line 1141, in __setitem__
    self.inputs[item].value = value
  File "C:\Python34\lib\site-packages\lxml\html\__init__.py", line 1207, in __getitem__
    "No input element with the name %r" % name)
KeyError: "No input element with the name 'user_email'"
>>> form.fields['user[email]'] = login
>>> form.fields['user[password]'] = password
>>> form.fields['user[remember_me]'] = 1
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    form.fields['user[remember_me]'] = 1
  File "C:\Python34\lib\site-packages\lxml\html\__init__.py", line 1141, in __setitem__
    self.inputs[item].value = value
  File "C:\Python34\lib\site-packages\lxml\html\__init__.py", line 1646, in value
    self.set('value', value)
  File "src\lxml\lxml.etree.pyx", line 824, in lxml.etree._Element.set (src\lxml\lxml.etree.c:49803)
  File "src\lxml\apihelpers.pxi", line 570, in lxml.etree._setAttributeValue (src\lxml\lxml.etree.c:21791)
  File "src\lxml\apihelpers.pxi", line 1437, in lxml.etree._utf8 (src\lxml\lxml.etree.c:30434)
TypeError: Argument must be bytes or unicode, got 'int'
>>> response = session.post(form.action, data=form.form_values())
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    response = session.post(form.action, data=form.form_values())
  File "C:\Python34\lib\site-packages\requests\sessions.py", line 511, in post
    return self.request('POST', url, data=data, json=json, **kwargs)
  File "C:\Python34\lib\site-packages\requests\sessions.py", line 454, in request
    prep = self.prepare_request(req)
  File "C:\Python34\lib\site-packages\requests\sessions.py", line 388, in prepare_request
    hooks=merge_hooks(request.hooks, self.hooks),
  File "C:\Python34\lib\site-packages\requests\models.py", line 293, in prepare
    self.prepare_url(url, params)
  File "C:\Python34\lib\site-packages\requests\models.py", line 353, in prepare_url
    raise MissingSchema(error)
requests.exceptions.MissingSchema: Invalid URL '/login': No schema supplied. Perhaps you meant http:///login?
>>> 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://geekbrains.ru/login
Cookie: _ym_uid=1458837363785801031; _session_id=SnNBNXR5MWtxS2E0QTFDNlhvdVBRYnJFSUUveFd5QUc2QjV1Wjl2bFh4cUxaQnBjQ0FMd0ZzUi9GSkQ3SFRNSDZGTTJNM00vWGNMRlZuYTNWUlJHRDV1M2x2Q3lrTS8vWEI1WGxDWlJTSk4vSHd0UVdWTFFYTE0zdHRDRTdsZ0stLUFUSGNGTVd5ZnBnWWhybkoxQWdMVWc9PQ%3D%3D--5795c4f17e4fb215bbe4280e172e29096f21bd79; _ym_isad=0; _ym_visorc_26577858=w
Connection: keep-alive'
SyntaxError: EOL while scanning string literal
>>> headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive',
    'DNT':'1'
}
>>> sess.post('https://geekbrains.ru/login', {
     'user[email]': 'eleasddsa@gmail.com',
     'user[password]': '123456qwe89',
     'user[remember_me]': 1})
<Response [422]>
>>> sess.post('https://geekbrains.ru/login', {
	'utf8': '✓',
	'authenticity_token': 'CTVDLHXK4gFXkbdXRRwPv7IjE+Tpna1ikCqrzP4mgvJGCgkguV4gjVH1+GL+m+g==',
     'user[email]': 'eleasddsa@gmail.com',
     'user[password]': '123456qwe89',
     'user[remember_me]': 1})
<Response [200]>
>>> page = sess.get('https://geekbrains.ru/events/6/attend')
>>> root = html.fromstring(page.text)
>>> root.body.find_class('row')[0].getchildren()
[<Element div at 0x430fcc0>, <Element div at 0x4439cf0>]
>>> root.body.find_class('row')[0][0][1].text
'Java Junior. Что нужно знать для успешного собеседования?'
>>> root_ev.body.find_class('row')[0][0][4].text
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    root_ev.body.find_class('row')[0][0][4].text
NameError: name 'root_ev' is not defined
>>> root_ev.body.find_class('row')[0][0][4]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    root_ev.body.find_class('row')[0][0][4]
NameError: name 'root_ev' is not defined
>>> root.body.find_class('row')[0][0][1].text
'Java Junior. Что нужно знать для успешного собеседования?'
>>> root.body.find_class('row')[0][0][1]
<Element h1 at 0x430fcc0>
>>> root.body.find_class('row')[0][0][2]
<Element div at 0x430fed0>
>>> root.body.find_class('row')[0][0][3]
<Element div at 0x430fcc0>
>>> root.body.find_class('row')[0][0][4]
<Element div at 0x430fed0>
>>> root.body.find_class('row')[0][0][4][0]
<Element iframe at 0x430fcc0>
>>> root.body.find_class('row')[0][0][4].text_content
<bound method HtmlElement.text_content of <Element div at 0x4439cf0>>
>>> root.body.find_class('row')[0][0][4].attrib
{'class': 'text-center m-b-md'}
>>> root.body.find_class('row')[0][0][4].itertext
<built-in method itertext of HtmlElement object at 0x04439CF0>
>>> root.body.find_class('row')[0][0][4].values
<built-in method values of HtmlElement object at 0x04439CF0>
>>> root.body.find_class('row')[0][0][4]
<Element div at 0x4439cf0>
>>> str(root.body.find_class('row')[0][0][4])
'<Element div at 0x4439cf0>'
>>> root.body.find_class('row')[0][0][4].tag
'div'
>>> 
