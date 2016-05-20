
import requests
from lxml import html


def Get_children(link_p, name_c):
    """
    функция
    """
    page_req = requests.get(link_p)
    page = html.fromstring(page_req.text)
    page.make_links_absolute('http://rus-linux.net')
    #print(name_c.split(' ')[0])
    #print(page.body.xpath(".//h1[contains(text(),'%s')]" % name_c.split(' ')[0])[0].getparent().tag)
    try:
        return page.body.xpath(".//h1[contains(text(),'%s')]" % name_c.split(' ')[0])[0].getparent().getchildren()
    except (IndexError):
        print('index Error')
        try:
            return page.body.xpath(".//h1[text()='%s']" % name_c.split(' ')[0])[0].getparent().getchildren()##############
        except (IndexError):
            print('index Error')
            return page.body.xpath(".//h1[contains(text(),'%s')]" % name_c.split(' ')[1])[0].getparent().getchildren()


def Loop_Chart(childs, lin, bool1 = True, bool2 = False, bool3 = False):

    in_tag = bool3  #конец статьи в tag
    jamp = bool2  # проверка на тег h2
    hr_bool = bool1

    end_pod_chart = False  # проверка на второй тег h2
    new_link_bool = False  # проверка на конец
    NG_bool = False

    new_link = ''

    ii = 0
    #print(len(childs))

    for pod_chart in childs:
        ii += 1
        #print(ii)

        if len(childs) == ii and jamp:
            Loop_Chart(pod_chart.getchildren(), lin, bool2=True)
            break

        if len(childs) == ii:
            if end_pod_chart:
                break
            print('end')
            #jamp = True
            Loop_Chart(childs, lin, bool1=False, bool2=True)
            continue

        if end_pod_chart and pod_chart.tag == 'hr':
            #print('hr2')
            pod_charts2 = Get_children(new_link, name_chart)  ####################
            Loop_Chart(pod_charts2, lin)
            #print(new_link)
            new_link_bool, end_pod_chart = False, False
            break

        if pod_chart.tag == 'hr' and not hr_bool:
            #print('not hr')
            hr_bool = True
            continue

        if new_link_bool:
            #print('link')
            if len(pod_chart.xpath(".//a")) == 0:
                #print('link = 0')
                new_link_bool, end_pod_chart = False, False
                break

            new_link = pod_chart.xpath("(.//a)[last()]")[0].values()[0]  ##################[last()]
            if new_link == lin :
                break
            if new_link == 'http://rus-linux.net/MyLDP/BOOKS/Architecture-Open-Source-Applications/index.html':
                break
            if new_link == 'http://www.vistrails.org':
                print(new_link)
                new_link_bool = False
                jamp = True
            else:
                print(new_link)
                new_link_bool = False
                end_pod_chart = True
                continue

        if pod_chart.tag == 'h2' or pod_chart.tag == 'h3':
            #print('h2')
            jamp = True
        elif not jamp and not end_pod_chart:
            #print("jamp")
            continue

        if pod_chart.tag == 'hr' and hr_bool:############

            if name_chart == 'NGINX' and not NG_bool:
                NG_bool = True
                continue
            #print('hr')
            new_link_bool = True
            jamp = False
            continue

        if NG_bool:
            #print('NG')
            NG_bool = False
            continue

        if jamp:
            #print('in')
            root.append(pod_chart)
            continue


f_save = open('Arh.html', 'bw')

first = requests.get('http://rus-linux.net/MyLDP/BOOKS/Architecture-Open-Source-Applications/index.html')

parsed_body = html.fromstring(first.text)

root = html.fromstring('<html></html>')

#t1 = parsed_body.body.xpath(".//img[@alt = 'Обложка 1-го тома']")[0].getparent().xpath(".//table/tbody/tr/td[2]/a") #1 and n uninclude

parsed_body.make_links_absolute('http://rus-linux.net')

link_charts = parsed_body.body.xpath(".//table/tbody/tr/td[2]/a")



#print((len(root)))


for link_chart in link_charts:

    if len(link_chart.getchildren()) == 0:
        continue

    name_chart = link_chart.getchildren()[0].text
    if not name_chart[0].istitle():
        name_chart = name_chart.upper()
    print(name_chart)
    print((list(link_chart.values())))
    pod_charts = Get_children(link_chart.values()[0], name_chart)
    Loop_Chart(pod_charts, list(link_chart.values())[0])

f_save.write(html.tostring(root))

f_save.close()
