#! python3
import os, re, sys
from pathlib import Path

# get user input for searchPath
searchPath =  Path(input('input folder path: '))
if searchPath.exists() ==False:
    sys.exit('Not found')  
prefix = input('enter prefix of folder, ie spam in spam01.txt: ')

folderDir = searchPath.glob('*'+prefix+'*')
#print(list(folderDir))
counter = 0
first = True
for txtFile in folderDir:
    # dataPattern = re.compile(prefix + '\d+'+ '.txt')
    # mo = dataPattern.search(txtFile)   #verify with regex
    pathPattern = re.compile(r'(.*)(\d\d\d\d)(.txt)$')
    mo = pathPattern.search(str(txtFile))
    if counter == 0:
        counter = int(mo.group(2))
    newtxtFile =txtFile
    count = int(mo.group(2))
    if count != counter+1:
        print('echo in first now false')
        temp = counter +1
        idk =''
        i = len(str(temp))
        while i < 4:
            idk +='0'
            i+=1
        newtxtFile = str(txtFile)[0:-8]+idk+str(counter)+'.txt'
    print(newtxtFile)
        #absWorkingDir = os.path.abspath(searchPath)
        #amerFilename = os.path.join(absWorkingDir, amerFilename)
        #euroFilename = os.path.join(absWorkingDir, euroFilename)

    counter = counter + 1       

    # if mo != None:
    #     print(mo)