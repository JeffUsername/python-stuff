# #! python3
import os, re, sys
from pathlib import Path

# get user input for searchPath
folderPath =  Path('C:\ch10 tests')#Path(input('input folder path: ')) #get path
if folderPath.exists() ==False:
    sys.exit('Not found')  
prefix = 'testSpame'#input('enter prefix of folder, ie spam in spam01.txt: ') #get prefix


first = True
#count = 0
for counter,filename in enumerate(os.listdir(folderPath)):
        dataPattern = re.compile(r'([{}])(\d\d)?(\d\d)(.txt)'.format(prefix))
        mo = dataPattern.search(filename)   #verify with regex
        if mo == None:
            continue
        dataPat = re.compile(r'''^(.*?)
            (\d\d)?
            (\d\d)
            (.*?)$''', re.VERBOSE)
        mo2 = dataPat.search(filename)
        if first == True:
            first = False
            count = mo2.group(3)
            print(first)
        
        #check current against count
        current =0
        current = mo2.group(3)
        if count != current:
            current = count
        if int(current) < 10:
            temp = '0'+ str(current)
        else:
             temp = str(current)
        
        
        #rename file
        newfilename =  mo2.group(1) + mo2.group(2)+temp+ mo2.group(4)
        absWorkingDir = os.path.abspath(folderPath)
        filename = os.path.join(absWorkingDir, filename)
        newfilename = os.path.join(absWorkingDir, newfilename)
        print(f'Renaming "{filename}" to "{newfilename}"...')
        
        count=int(count)+ 1