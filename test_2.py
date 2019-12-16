"""
http://www.pythonchallenge.com/pc/def/ocr.html
<!--
find rare characters in the mess below:
-->
"""

import urllib.request
data = str(urllib.request.urlopen\
           ("http://www.pythonchallenge.com/pc/def/ocr.html").read())

data = ((max(data.split(), key=len)))[19:-10:]
data = ((max(data.split('--'), key=len)))

dct = {}
for i in data:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1
def rare_word():
    rare = ''
    for key, value in dct.items():
        if value == 1:
            rare += str(key)
    return rare            

print('http://www.pythonchallenge.com/pc/def/', rare_word(), '.html', sep='')

#http://www.pythonchallenge.com/pc/def/equality.html
