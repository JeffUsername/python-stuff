import re
madFile = open('madlibs.txt')   #open/read file
readme = madFile.read()
myMadFile = open('myMadLibs.txt','a')
#myMadLib = myMadLib.write()     #setup output file
tim2=''
for word in readme.split():
    test = re.compile(r'^AD.*|^NO.*|^VE.*')
    test2 = re.compile(r'[.,!?;:]')
    if test.search(word):
        print('Enter a(n) %s' % word)
        temp = input()
        if test2.search(word[-1]):
            word = temp + word[-1]
        else:
            word = temp
    tim= word + ' '
    myMadFile.write(tim)     #setup output file
    
    tim2 +=tim
print(tim2)
madFile.close()     #close files
myMadFile.close()