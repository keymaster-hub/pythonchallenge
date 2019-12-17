"""
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
and the next nothing is 44827
"""

import urllib.request
base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
data = str(urllib.request.urlopen(base_url + '12345').read()).split(' ')
digits = data[-1][:-1]

while digits.isdigit():
    data = \
    str(urllib.request.urlopen(base_url + digits).read()).split(' ')
    digits = data[-1][:-1]
    print(base_url + digits)
 
digits = '8022'
while digits.isdigit():
    data = \
    str(urllib.request.urlopen(base_url + digits).read()).split(' ')
    digits = data[-1][:-1]
    print(base_url + digits)
    
print('http://www.pythonchallenge.com/pc/def/' + digits[2:])

#http://www.pythonchallenge.com/pc/def/peak.html
