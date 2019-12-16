"""
http://www.pythonchallenge.com/pc/def/map.html
"""
import string


def decrypt(word: string, step: int):
    step = step % 26
    alph = string.ascii_lowercase + string.ascii_lowercase[0:step] +\
           string.ascii_uppercase + string.ascii_uppercase[0:step]
    list = []
    for x in word:
        if x.isalpha():
            list += [alph[alph.index(x) + step]]
        else:
            list += x
    return list


question = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr\
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr \
ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle \
qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
print(*decrypt(question, 2), sep='')
print('http://www.pythonchallenge.com/pc/def/', \
      (*decrypt('map', 2)), '.html', sep='')

#http://www.pythonchallenge.com/pc/def/ocr.html
