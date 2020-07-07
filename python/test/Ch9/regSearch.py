#! python3
import sys, os, re
from pathlib import Path

#Promt for location name
tim = 'C:'
folderPath = os.path.abspath(Path(input('input folder: ')))
#folderPath = Path(input('Enter path to search folder: '))
#print('your input--> ' + str(folderPath))

#validate path
if folderPath.exists() ==False:
    sys.exit('Not found')     
#Enter search term
term = input('Enter terms for search: ')
test = '.txt'
#Get datatype of .txt's  in folder
#folderDir = folderPath.glob('*.txt') #glob search for any txt to list
folderDir = folderPath.glob('*'+test)
for txtFile in folderDir: #iterate list
    theFile = open(txtFile) #open file
    fixed = os.path.basename(txtFile)
    print('++++++'+fixed.upper()+'++++++')
    reading = theFile.readlines() #read by lines
    for line in reading:
        find = re.compile(term) #regex
        line = re.sub('\n','',line) #get rid of all the extra newlines
        if find.search(line): #validate line
            print(line)
           #print(line) 
    theFile.close()
    print('------------------------------------------------------------------------')
    