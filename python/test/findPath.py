#! python3
import os, re,pyinputplus as pyip
def findPath(pathStart):
    paths = []
    datePattern = re.compile(r'.*?'+pathStart+r'.*?')
    for folderName, subfolders, filenames in os.walk('C:\A Live in area\\'):#\A Live in area\\back to scool\\'):
        mo1 = datePattern.search(folderName)
        #print('Folder: '+folderName)
        if mo1 !=None:
            #print('Conetent Fold: '+folderName)
            paths.append(folderName)

        for subfolder in subfolders:
            mo2 = datePattern.search(subfolder)
            if mo2 !=None:
                # print('Content Sub: '+folderName+subfolder)
                paths.append(folderName+subfolder)
                #folderName + subfolder
    # datePattern = re.compile(r'(C:.*?)+pathStart+(.*?)')

    # for amerFilename in os.listdir('.'):
    #     mo = datePattern.search(amerFilename)
    #     if mo ==None:
    #         continue
    #     paths.append(mo)
    if len(paths) > 0:
        finalPath = pyip.inputMenu(paths, numbered= True)
    else:
        finalPath = 'noting'
    return finalPath
    #return paths

rim =findPath(input('enter folder: '))
print(rim)