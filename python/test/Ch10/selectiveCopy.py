#! python3
import shutil, os, re

# get user input for copyPath
copyPath = input('enter folder to be searched: ')
# get user input for pastePath, if none create folder in where ever
pastePath = input('enter folder to paste files: ')

# get user input for file type
extType = input('enter file type, ie .txt or .pdf: ')
# search folder tree
    #use os.walk
for folderName, subfolders, filenames in os.walk(copyPath):
    #print('The current folder is ' + folderName)
    for subfolder in subfolders:
        #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        temp = 'meh'
    for filename in filenames:
        dataPattern = re.compile(r'.*?'+extType)
        mo = dataPattern.search(filename)   #verify with regex
        if mo != None:
            temp2 = folderName+'\\'+filename
            shutil.copy(temp2, pastePath)   #copy and paste files.
            #print(folderName+ '   :    '+filename)  
            #print(pastePath)  
