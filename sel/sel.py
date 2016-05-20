from lxml import html
import requests


#file = open('Sel.html', 'bw')

root = html.fromstring('<html></html>')

first_link = requests.get('http://selenium2.ru/docs.html')

first_page = html.fromstring(first_link.text)

first_page.make_links_absolute('http://selenium2.ru')

link_charts = first_page.find_class('toctree-wrapper compound')

#print(link_charts[0][0][0][0].xpath('(.//@href)[1]'))

def get_page(link_page):
    req_page = requests.get(link_page)
    html_page = html.fromstring(req_page.text)
    html_page.make_links_absolute('http://selenium2.ru')
    charts = html_page.find_class('item-page')
    #root.append(charts[0].getchildren()[0])
    #print(charts[0].xpath('(.//h2)[1]').text)
    root.append(charts[0][-1])
    print('Ok')

def content(page_class):
    for a_page in page_class[0].getchildren():
        #print(a_page[0].text)
        print(a_page[0].xpath('(.//@href)[1]')[0])
        root.append(html.fromstring('<h1>%s</h1>' % a_page[0].text))
        get_page(a_page[0].xpath('(.//@href)[1]')[0])

content(link_charts[0])
root.append(html.fromstring('<h1>Приложения</h1>'))
content(link_charts[1])

with open('Sel.html', 'bw') as file:
    file.write(html.tostring(root))
