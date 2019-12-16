"""
http://www.pythonchallenge.com/pc/def/ocr.html
<!--
One small letter, surrounded by EXACTLY three big bodyguards
on each of its sides.
-->
"""

import urllib.request
data = str(urllib.request.urlopen\
           ("http://www.pythonchallenge.com/pc/def/equality.html").read())

data = ((max(data.split(), key=len)))
data = 'xxxx' + ((max(data.split('--'), key=len))) + 'xxxx'


def secret_word():
    word = ''
    full = '' 
    for i in range(len(data)):
        if data[i].islower():
            
            word += data[i]
        elif data[i].isupper():
            if data[i:i+3].isupper() and \
               data[i-3-len(word):i-len(word)].isupper() and\
               data[i+3].islower() and \
               data[i-4-len(word)].islower():
                    
               
                    full +=  word
                    
                
            else:
                word = ''
    return(full)            
print(secret_word()) 

                                              
                
                    

         
           
            
                
print(secret_word())

    

#print('http://www.pythonchallenge.com/pc/def/', rare_word(), '.html', sep='')

#http://www.pythonchallenge.com/pc/def/equality.html
