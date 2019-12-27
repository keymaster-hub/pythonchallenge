"""
http://www.pythonchallenge.com/pc/def/channel.html

http://www.pythonchallenge.com/pc/def/channel.zip
welcome to my zipped list.
hint1: start from 90052
hint2: answer is inside the zip

"""
import re
from zipfile import ZipFile as z

start = 90052
file = z('channel.zip', 'r')
next_index = start
comments = []

while True:
    data = str(file.read(str(next_index) + '.txt'))
    comments.append((file.getinfo(str(next_index) + '.txt'))\
                    .comment.decode('utf-8'))
    next_index = ''.join(re.findall(r'[0-9]', data))
    if len(str(next_index)) == 0:
        break
                           
print(''.join(comments))
print('http://www.pythonchallenge.com/pc/def/hockey.html')
print('http://www.pythonchallenge.com/pc/def/oxygen.html')

#http://www.pythonchallenge.com/pc/def/hockey.html
#http://www.pythonchallenge.com/pc/def/oxygen.html
