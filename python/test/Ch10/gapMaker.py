import os, re, random
from pathlib import Path

# get user input for searchPath
gapPath = Path(input('enter folder to be searched: '))
spams = 100
for spam in range(spams):
    if random.choice([True,False]) == True:
        idk = ''
        i = len(str(spam))
        while i < 4:
            idk +='0'
            i+=1
        eh ='testSpame' + idk + str(spam)+'.txt'
        #print(eh)
        meh =open(os.path.join(gapPath,eh),'w')
        meh.write('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!')
        meh.close()