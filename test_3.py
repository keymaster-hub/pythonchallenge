"""
http://www.pythonchallenge.com/pc/def/ocr.html
<!--
find rare characters in the mess below:
-->
"""

import urllib.request
data = str(urllib.request.urlopen\
           ("http://www.pythonchallenge.com/pc/def/equality.html").read())

data = ((max(data.split(), key=len)))
data = ((max(data.split('--'), key=len)))
dct = {}
for i in data:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

for key, value in dct.items():
    print(key, value)

    

#print('http://www.pythonchallenge.com/pc/def/', rare_word(), '.html', sep='')

#http://www.pythonchallenge.com/pc/def/equality.html
