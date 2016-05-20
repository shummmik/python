Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import win32com.client as win32
>>> w = win32.Dispatch('Word.Application')
>>> xd = w.Documents.Add()
>>> xd.ActiveDocument
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    xd.ActiveDocument
  File "C:\Python34\lib\site-packages\win32com\client\dynamic.py", line 527, in __getattr__
    raise AttributeError("%s.%s" % (self._username_, attr))
AttributeError: Add.ActiveDocument
>>> w.Documents.Add()
<COMObject Add>
>>> xd = w.ActiveDocument
>>> help(xd.Tables.Add())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    help(xd.Tables.Add())
  File "<COMObject <unknown>>", line 4, in Add
pywintypes.com_error: (-2147352562, 'Недопустимое число параметров.', None, None)
>>> help(xd.Tables)
Help on CDispatch in module win32com.client object:

class CDispatch(win32com.client.dynamic.CDispatch)
 |  The dynamic class used as a last resort.
 |  The purpose of this overriding of dynamic.CDispatch is to perpetuate the policy
 |  of using the makepy generated wrapper Python class instead of dynamic.CDispatch
 |  if/when possible.
 |  
 |  Method resolution order:
 |      CDispatch
 |      win32com.client.dynamic.CDispatch
 |      builtins.object
 |  
 |  Methods inherited from win32com.client.dynamic.CDispatch:
 |  
 |  __AttrToID__(self, attr)
 |  
 |  __LazyMap__(self, attr)
 |  
 |  __bool__(self)
 |  
 |  __call__(self, *args)
 |      Provide 'default dispatch' COM functionality - allow instance to be called
 |  
 |  __eq__(self, other)
 |      # Delegate comparison to the oleobjs, as they know how to do identity.
 |  
 |  __getattr__(self, attr)
 |  
 |  __getitem__(self, index)
 |  
 |  __init__(self, IDispatch, olerepr, userName=None, UnicodeToString=None, lazydata=None)
 |  
 |  __int__(self)
 |  
 |  __len__(self)
 |  
 |  __ne__(self, other)
 |  
 |  __repr__(self)
 |  
 |  __setattr__(self, attr, value)
 |  
 |  __setitem__(self, index, *args)
 |  
 |  __str__(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from win32com.client.dynamic.CDispatch:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from win32com.client.dynamic.CDispatch:
 |  
 |  __hash__ = None

>>> dir(xd.Tables
    )
['_ApplyTypes_', '_FlagAsMethod', '_LazyAddAttr_', '_NewEnum', '_Release_', '__AttrToID__', '__LazyMap__', '__bool__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_builtMethods_', '_enum_', '_find_dispatch_type_', '_get_good_object_', '_get_good_single_object_', '_lazydata_', '_make_method_', '_mapCachedItems_', '_oleobj_', '_olerepr_', '_print_details_', '_proc_', '_unicode_to_string_', '_username_', '_wrap_dispatch_']
>>> print(xd.Tables.__doc__)

    The dynamic class used as a last resort.
    The purpose of this overriding of dynamic.CDispatch is to perpetuate the policy
    of using the makepy generated wrapper Python class instead of dynamic.CDispatch
    if/when possible.
  
>>> help(w.Documents)
Help on CDispatch in module win32com.client object:

class CDispatch(win32com.client.dynamic.CDispatch)
 |  The dynamic class used as a last resort.
 |  The purpose of this overriding of dynamic.CDispatch is to perpetuate the policy
 |  of using the makepy generated wrapper Python class instead of dynamic.CDispatch
 |  if/when possible.
 |  
 |  Method resolution order:
 |      CDispatch
 |      win32com.client.dynamic.CDispatch
 |      builtins.object
 |  
 |  Methods inherited from win32com.client.dynamic.CDispatch:
 |  
 |  __AttrToID__(self, attr)
 |  
 |  __LazyMap__(self, attr)
 |  
 |  __bool__(self)
 |  
 |  __call__(self, *args)
 |      Provide 'default dispatch' COM functionality - allow instance to be called
 |  
 |  __eq__(self, other)
 |      # Delegate comparison to the oleobjs, as they know how to do identity.
 |  
 |  __getattr__(self, attr)
 |  
 |  __getitem__(self, index)
 |  
 |  __init__(self, IDispatch, olerepr, userName=None, UnicodeToString=None, lazydata=None)
 |  
 |  __int__(self)
 |  
 |  __len__(self)
 |  
 |  __ne__(self, other)
 |  
 |  __repr__(self)
 |  
 |  __setattr__(self, attr, value)
 |  
 |  __setitem__(self, index, *args)
 |  
 |  __str__(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from win32com.client.dynamic.CDispatch:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from win32com.client.dynamic.CDispatch:
 |  
 |  __hash__ = None

>>> print(w.Documents.__doc__)

    The dynamic class used as a last resort.
    The purpose of this overriding of dynamic.CDispatch is to perpetuate the policy
    of using the makepy generated wrapper Python class instead of dynamic.CDispatch
    if/when possible.
  
>>> dir(w.Documents)
['_ApplyTypes_', '_FlagAsMethod', '_LazyAddAttr_', '_NewEnum', '_Release_', '__AttrToID__', '__LazyMap__', '__bool__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_builtMethods_', '_enum_', '_find_dispatch_type_', '_get_good_object_', '_get_good_single_object_', '_lazydata_', '_make_method_', '_mapCachedItems_', '_oleobj_', '_olerepr_', '_print_details_', '_proc_', '_unicode_to_string_', '_username_', '_wrap_dispatch_']
>>> dir(w.Documents.Add())
['_ApplyTypes_', '_FlagAsMethod', '_LazyAddAttr_', '_NewEnum', '_Release_', '__AttrToID__', '__LazyMap__', '__bool__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_builtMethods_', '_enum_', '_find_dispatch_type_', '_get_good_object_', '_get_good_single_object_', '_lazydata_', '_make_method_', '_mapCachedItems_', '_oleobj_', '_olerepr_', '_print_details_', '_proc_', '_unicode_to_string_', '_username_', '_wrap_dispatch_']
>>> dir(w.Documents.Add)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(xd.Tables.Add)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(xd.Tables.Add())
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dir(xd.Tables.Add())
  File "<COMObject <unknown>>", line 4, in Add
pywintypes.com_error: (-2147352562, 'Недопустимое число параметров.', None, None)
>>> dir(xd.Tables.Add(3,4))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dir(xd.Tables.Add(3,4))
  File "<COMObject <unknown>>", line 4, in Add
TypeError: The Python instance can not be converted to a COM object
>>> xd.Tables.Add(3,4)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    xd.Tables.Add(3,4)
  File "<COMObject <unknown>>", line 4, in Add
TypeError: The Python instance can not be converted to a COM object
>>> dir(xd.Range)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(xd.Range())
['_ApplyTypes_', '_FlagAsMethod', '_LazyAddAttr_', '_NewEnum', '_Release_', '__AttrToID__', '__LazyMap__', '__bool__', '__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_builtMethods_', '_enum_', '_find_dispatch_type_', '_get_good_object_', '_get_good_single_object_', '_lazydata_', '_make_method_', '_mapCachedItems_', '_oleobj_', '_olerepr_', '_print_details_', '_proc_', '_unicode_to_string_', '_username_', '_wrap_dispatch_']
>>> xd.Tables.Add(xd.Range(),3,4)
<COMObject Add>
>>> xd.Tables.Add(xd.Range(0,0),3,4)
<COMObject Add>
>>> xd.Tables.Add(xd.Range(0,0),6,4)
<COMObject Add>
>>> xd.SaveAs(os.path.abspath(r'x.docx'))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    xd.SaveAs(os.path.abspath(r'x.docx'))
NameError: name 'os' is not defined
>>> import os
>>> xd.SaveAs(os.path.abspath(r'x.docx'))
>>> xd.Close()
>>> w.Close()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    w.Close()
  File "C:\Python34\lib\site-packages\win32com\client\dynamic.py", line 527, in __getattr__
    raise AttributeError("%s.%s" % (self._username_, attr))
AttributeError: Word.Application.Close
>>> w.Quit()
>>> del xd
>>> import requests
>>> from lxml import html
>>> p = requests.get('http://www.wordreference.com/enru/run')
>>> root = html.fromstring(p)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    root = html.fromstring(p)
  File "C:\Python34\lib\site-packages\lxml\html\__init__.py", line 866, in fromstring
    is_full_html = _looks_like_full_html_unicode(html)
TypeError: expected string or buffer
>>> root = html.fromstring(p.text)
>>> r = root.body.xpath('.//span[id="pronWR"]')
>>> len(r)
0
>>> r = root.body.xpath('.//span[@id="pronWR"]')
>>> len(r)
1
>>> print(r[0])
<Element span at 0x47a7a20>
>>> print(r[0].text)
/rʌn/
>>> r1 = root.body.find_class('WRD')
>>> len(r1)
1
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru"]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru*"]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru"*]')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru"*]')
  File "src\lxml\lxml.etree.pyx", line 1587, in lxml.etree._Element.xpath (src\lxml\lxml.etree.c:58124)
  File "src\lxml\xpath.pxi", line 307, in lxml.etree.XPathElementEvaluator.__call__ (src\lxml\lxml.etree.c:167145)
  File "src\lxml\xpath.pxi", line 227, in lxml.etree._XPathEvaluatorBase._handle_result (src\lxml\lxml.etree.c:166104)
lxml.etree.XPathEvalError: Invalid expression
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru\*"]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:*"]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:3781"]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:2214"]')
>>> len(r1)
1
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:&"]')
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:?"]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:[\d\d\d\d]"]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:.')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:.')
  File "src\lxml\lxml.etree.pyx", line 1587, in lxml.etree._Element.xpath (src\lxml\lxml.etree.c:58124)
  File "src\lxml\xpath.pxi", line 307, in lxml.etree.XPathElementEvaluator.__call__ (src\lxml\lxml.etree.c:167145)
  File "src\lxml\xpath.pxi", line 227, in lxml.etree._XPathEvaluatorBase._handle_result (src\lxml\lxml.etree.c:166104)
lxml.etree.XPathEvalError: Unfinished literal
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:."]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="enru:...."]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id=*]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id="*"]')
>>> len(r1)
0
>>> r1 = root.body.find_class('WRD')[0].xpath('.//tr[@id!=""]')
>>> len(r1)
7
>>> r1[0].text
>>> print(r1[0].text)
None
>>> 
>>> import json
>>> p1 = requests.get('https://dictionary.yandex.net/dicservice.json/lookup?ui=ru&srv=tr-text&text=be&lang=en-ru&flags=23')
>>> js = json.load(p1.text)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    js = json.load(p1.text)
  File "C:\Python34\lib\json\__init__.py", line 265, in load
    return loads(fp.read(),
AttributeError: 'str' object has no attribute 'read'
>>> js = json.loads(p1.text)
>>> js
{'def': [{'tr': [{'ex': [{'tr': [{'text': 'быть в субботу'}], 'text': 'be on saturday'}], 'syn': [{'asp': 'несов', 'text': 'существовать', 'pos': 'гл'}], 'asp': 'несов', 'text': 'быть', 'mean': [{'text': 'have'}, {'text': 'exist'}], 'pos': 'гл'}, {'mean': [{'text': 'occur'}], 'asp': 'несов', 'text': 'происходить', 'pos': 'гл'}, {'mean': [{'text': 'mean'}], 'syn': [{'asp': 'несов', 'text': 'значить', 'pos': 'гл'}], 'asp': 'несов', 'text': 'означать', 'pos': 'гл'}, {'ex': [{'tr': [{'text': 'пребывать в гармонии'}], 'text': 'be in harmony'}], 'syn': [{'asp': 'несов', 'text': 'пребывать', 'pos': 'гл'}], 'asp': 'несов', 'text': 'жить', 'mean': [{'text': 'live'}, {'text': 'stay'}], 'pos': 'гл'}], 'ts': 'biː', 'text': 'be', 'pos': 'гл'}], 'head': {'more': True}}
>>> print(js)
{'def': [{'tr': [{'ex': [{'tr': [{'text': 'быть в субботу'}], 'text': 'be on saturday'}], 'syn': [{'asp': 'несов', 'text': 'существовать', 'pos': 'гл'}], 'asp': 'несов', 'text': 'быть', 'mean': [{'text': 'have'}, {'text': 'exist'}], 'pos': 'гл'}, {'mean': [{'text': 'occur'}], 'asp': 'несов', 'text': 'происходить', 'pos': 'гл'}, {'mean': [{'text': 'mean'}], 'syn': [{'asp': 'несов', 'text': 'значить', 'pos': 'гл'}], 'asp': 'несов', 'text': 'означать', 'pos': 'гл'}, {'ex': [{'tr': [{'text': 'пребывать в гармонии'}], 'text': 'be in harmony'}], 'syn': [{'asp': 'несов', 'text': 'пребывать', 'pos': 'гл'}], 'asp': 'несов', 'text': 'жить', 'mean': [{'text': 'live'}, {'text': 'stay'}], 'pos': 'гл'}], 'ts': 'biː', 'text': 'be', 'pos': 'гл'}], 'head': {'more': True}}
>>> print(js['text'])
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    print(js['text'])
KeyError: 'text'
>>> print(js["text"])
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    print(js["text"])
KeyError: 'text'
>>> pprint
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    pprint
NameError: name 'pprint' is not defined
>>> 
>>> 
>>> from pprint import pprint
>>> pprint(js)
{'def': [{'pos': 'гл',
          'text': 'be',
          'tr': [{'asp': 'несов',
                  'ex': [{'text': 'be on saturday',
                          'tr': [{'text': 'быть в субботу'}]}],
                  'mean': [{'text': 'have'}, {'text': 'exist'}],
                  'pos': 'гл',
                  'syn': [{'asp': 'несов',
                           'pos': 'гл',
                           'text': 'существовать'}],
                  'text': 'быть'},
                 {'asp': 'несов',
                  'mean': [{'text': 'occur'}],
                  'pos': 'гл',
                  'text': 'происходить'},
                 {'asp': 'несов',
                  'mean': [{'text': 'mean'}],
                  'pos': 'гл',
                  'syn': [{'asp': 'несов',
                           'pos': 'гл',
                           'text': 'значить'}],
                  'text': 'означать'},
                 {'asp': 'несов',
                  'ex': [{'text': 'be in harmony',
                          'tr': [{'text': 'пребывать в гармонии'}]}],
                  'mean': [{'text': 'live'}, {'text': 'stay'}],
                  'pos': 'гл',
                  'syn': [{'asp': 'несов',
                           'pos': 'гл',
                           'text': 'пребывать'}],
                  'text': 'жить'}],
          'ts': 'biː'}],
 'head': {'more': True}}
>>> 
>>> 
>>> js["text"]
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    js["text"]
KeyError: 'text'
>>> 
