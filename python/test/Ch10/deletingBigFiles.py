#! python3
import os, re
from pathlib import Path

# get user input for copyPath
copyPath = Path(input('enter folder to be searched: '))

for folderName, subfolders, filenames in os.walk(copyPath): #os walk
    #print('The current folder is ' + folderName)
    # for subfolder in subfolders:
    #     temp = 'meh'
    for filename in filenames:
        temp2 = folderName+'\\'+filename
        if os.path.getsize(temp2) > 104857600: #get file size
            print(os.path.abspath(temp2))   #print abspath