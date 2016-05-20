# -*- coding: utf-8 -*- 
import urllib, requests
URLY = 'http://www.youtube.com/get_video_info'

class YoutubeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def encod(data):
    #deco!@!!!!
    return urllib.parse.unquote_plus(data)#,encoding='utf-8')#cp1251

def encod_l(data):
    data[1] = encod(data[1])
    return data

def in_dict(data):
    return dict([param.split('=') for param in data.split('&')])

def in_dict_en(data):
    return dict([encod_l(param.split('=')) for param in data.split('&')])

def get_id(url): #проверка на  None
    try:
        parametrs = urllib.parse.urlparse(url)
        
        id_v = in_dict(parametrs.query)['v']
        
    except Exception:
        id_v = url
    return id_v

def get_links(url):
    
    parms = {'video_id': get_id(url)}
    
    f_config = requests.get(URLY, params=parms) #, headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"})
    
    #try:
    #...     raise MyError(2*2)
    #... except MyError as e:
    #...     print 'My exception occurred, value:', e.value
    #My exception occurred, value: 4

    meta_inf = in_dict(f_config.text)
    
    if meta_inf['status'] == 'fail':
        raise YoutubeError(encod(meta_inf['reason']))
    title = encod(meta_inf['title'])
    dict_links = list()
    for link in encod(meta_inf['adaptive_fmts']).split(','):
        print(link)
        d = in_dict_en(link)
        dict_links.append(d)
    return [title, dict_links]
