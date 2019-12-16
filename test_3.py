"""
http://www.pythonchallenge.com/pc/def/equality.html
<!--
One small letter, surrounded by EXACTLY three big bodyguards
on each of its sides.
-->
"""

import urllib.request
data = str(urllib.request.urlopen\
           ("http://www.pythonchallenge.com/pc/def/equality.html").read())

data = (max(data.split(), key=len))
data = (max(data.split('--'), key=len))
data = data.replace('\\n','')

def secret_word():
    word = ''
    for i in range(len(data)):
        if data[i].islower() and \
           data[i-3:i].isupper() and \
           data[i+1:i+4].isupper() and \
           data[i-4].islower() and \
           data[i+4].islower():
            word += data[i]
    return word

print('http://www.pythonchallenge.com/pc/def/', secret_word(), '.php', sep='')

#http://www.pythonchallenge.com/pc/def/linkedlist.php