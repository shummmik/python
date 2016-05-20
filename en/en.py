# -*- coding: utf-8 -*-
import requests, os, json
#from lxml import html
import win32com.client as win32
from pprint import pprint

page = 'http://www.wordreference.com/enru/'
f_open = open(u'words.txt', 'r')
list_words = list()

startpage = 'https://dictionary.yandex.net/dicservice.json/lookup?ui=ru&srv=tr-text&text='
endpage = '&lang=en-ru'

for line in f_open:
    list_words.append(line[:-1])

f_open.close()
word = win32.Dispatch('Word.Application')

word.Visible = 0
docx = word.Documents.Add()
docx.Tables.Add(docx.Range(0, 0), len(list_words), 2)
table = docx.Tables(1)

n = 1

for word1 in list_words:
    page = requests.get('%s%s%s' % (startpage, word1, endpage))
    #print(page.text)  # .encode(encoding='utf-8'))
    js = json.loads(page.text)

    #pprint(js)
    column2 = ''  # переделать под объект COM
    table.Cell(n, 1).Range.Text = word1
   
    print(len(js['def']))

    for i in js['def']:
        column2 = column2 + (('--%s [%s] (%s) -%s \n' %
        (i['text'], i['ts'], i['pos'], i['tr'][0]['text'])) +
        ('' if i['tr'][0].get('mean')==None else ('%s\n' % (', '.join([j['text'] for j in i['tr'][0]['mean']])))) +
        ('' if i['tr'][0].get('syn')==None else ('%s\n' % (', '.join([j['text'] for j in i['tr'][0]['syn']])))) +
        ('' if i['tr'][0].get('ex')==None else ('%s\n' % (', '.join([('%s - %s' %(j['text'], j['tr'][0]['text'])) for j in i['tr'][0]['ex']])))))
    #pprint(column2)

    table.Cell(n, 2).Range.Text = column2[:-1]
    n += 1
docx.SaveAs(os.path.abspath(r'x.docx'))
docx.Close()
del docx
word.Quit()
del word





