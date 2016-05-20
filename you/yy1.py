Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '%D0%90%D0%BC%D1%85%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9'
'%D0%90%D0%BC%D1%85%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9'
>>> s ='%D0%90%D0%BC%D1%85%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9'
>>> s.encode()
b'%D0%90%D0%BC%D1%85%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9'
>>> import re
>>> p = re.compile(r'%( [0-9A-Fa-f][0-9A-Fa-f] )', re.VERBOSE)
>>> p.sub(r'\x\1',s)
'\\xD0\\x90\\xD0\\xBC\\xD1\\x85\\xD0\\xB0\\xD1\\x80\\xD1\\x81\\xD0\\xBA\\xD0\\xB8\\xD0\\xB9'
>>> p.sub(r'\x\1',s).encode()
b'\\xD0\\x90\\xD0\\xBC\\xD1\\x85\\xD0\\xB0\\xD1\\x80\\xD1\\x81\\xD0\\xBA\\xD0\\xB8\\xD0\\xB9'
>>> p.sub(r'\x\1',s).encode().encode()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    p.sub(r'\x\1',s).encode().encode()
AttributeError: 'bytes' object has no attribute 'encode'
>>> 
KeyboardInterrupt
>>>  p.sub(r'\u\1',s).encode()
 
SyntaxError: unexpected indent
>>> p.sub(r'\u\1',s).encode()
b'\\uD0\\u90\\uD0\\uBC\\uD1\\u85\\uD0\\uB0\\uD1\\u80\\uD1\\u81\\uD0\\uBA\\uD0\\uB8\\uD0\\uB9'
>>> p.sub(b'\u\1',s).encode()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    p.sub(b'\u\1',s).encode()
TypeError: sequence item 0: expected str instance, bytes found
>>>  p.sub('\u\1',s).encode()
 
SyntaxError: unexpected indent
>>> p.sub('\u\1',s).encode()
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-1: truncated \uXXXX escape
>>> p.sub(r'\x\1',s).encode()
b'\\xD0\\x90\\xD0\\xBC\\xD1\\x85\\xD0\\xB0\\xD1\\x80\\xD1\\x81\\xD0\\xBA\\xD0\\xB8\\xD0\\xB9'
>>> p.sub(r'\x\1',s).encode('ascii')
b'\\xD0\\x90\\xD0\\xBC\\xD1\\x85\\xD0\\xB0\\xD1\\x80\\xD1\\x81\\xD0\\xBA\\xD0\\xB8\\xD0\\xB9'
>>> '\xD0'
'Ð'
>>> p.sub(r'\\x\1',s).encode()
b'\\xD0\\x90\\xD0\\xBC\\xD1\\x85\\xD0\\xB0\\xD1\\x80\\xD1\\x81\\xD0\\xBA\\xD0\\xB8\\xD0\\xB9'
>>> p.sub(r'/\x\1',s).encode()
b'/\\xD0/\\x90/\\xD0/\\xBC/\\xD1/\\x85/\\xD0/\\xB0/\\xD1/\\x80/\\xD1/\\x81/\\xD0/\\xBA/\\xD0/\\xB8/\\xD0/\\xB9'
>>> p.sub(r'\1',s).encode()
b'D090D0BCD185D0B0D180D181D0BAD0B8D0B9'
>>> p.sub(r'\1'.encode(),s)
'D090D0BCD185D0B0D180D181D0BAD0B8D0B9'
>>> p.sub(r'1'.encode(),s)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    p.sub(r'1'.encode(),s)
TypeError: sequence item 0: expected str instance, bytes found
>>> p.sub(r'1'.encode(),s)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    p.sub(r'1'.encode(),s)
TypeError: sequence item 0: expected str instance, bytes found
>>> p.sub('\1'.encode(),s)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    p.sub('\1'.encode(),s)
TypeError: sequence item 0: expected str instance, bytes found
>>> p.sub(r'\1'.encode(),s)
'D090D0BCD185D0B0D180D181D0BAD0B8D0B9'
>>> 
