"""
http://www.pythonchallenge.com/pc/def/peak.html
http://www.pythonchallenge.com/pc/def/banner.p
"""

from urllib.request import urlopen
import pickle

base_url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = urlopen(base_url).read()

data = pickle.loads(data)
for i in data:
    print("".join([a * b for a, b in i]))
    
print('http://www.pythonchallenge.com/pc/def/channel.html')
#http://www.pythonchallenge.com/pc/def/channel.html




