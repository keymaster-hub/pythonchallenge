"""
http://www.pythonchallenge.com/pc/def/peak.html
http://www.pythonchallenge.com/pc/def/banner.p
"""

import urllib.request
import pickle

base_url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = urllib.request.urlopen(base_url).read()
data = pickle.loads(data)
for i in range(len(data)):
    print(data[i])
    


"""
data[0] = str(data[0][2:])
data[-1] = str(data[-1][0:-1])
for i in data:
    print(i)
"""


