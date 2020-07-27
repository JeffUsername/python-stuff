#!
import os, PyPDF2, re, shutil, send2trash #imports
from pathlib import Path

def walk(wP, boole, pword):
    paths = []
    #print(str(boole) + ' : ' + wP)
    for folderName, subfolders, filenames in os.walk(wP):
        for subfolder in subfolders:
            lazy = 'lazy'
        for filename in filenames:
            #print('FILE INSIDE ' + folderName + ': '+ filename)
            if filename[-4:] =='.pdf':
                #thing  = test file
                print(folderName +'/'+filename)
                #test pword, continue if fails
                pdfFile = open(folderName+'/'+filename, 'rb')
                pdfReader = PyPDF2.PdfFileReader(pdfFile)
                #test encrypt
                if pdfReader.isEncrypted and boole == False:
                   i = pdfReader.decrypt(pword)
                   if i == 0:
                       continue
                elif pdfReader.isEncrypted:
                    continue    #boole true
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                #print('past pagewrite')
                if boole == True:
                    pdfWriter.encrypt(pword)
                    tim = filename[0:-4]+'_encrypted'+filename[-4:]
                    print('true boole')
                else:
                    print('false boole')
                    tim = re.sub('_encrypted','',filename)
                resultPdf = open(tim, 'wb')
                pdfWriter.write(resultPdf)
                resultPdf.close()
                pdfFile.close()
                #test encryped file
                if boole == True:
                    try:
                        pdfReader = PyPDF2.PdfFileReader(open(folderName+'/'+tim, 'rb'))
                        pdfReader.getPage(0)
                    except:
                        stop = False
                    if stop:
                        print('problem')
                        continue
                #if true delete old file
                temp = os.path.abspath(tim)
                #print(temp)
                # #move new file to current dir
                shutil.move(temp,folderName)
                #send2trash.send2trash(filename)
                os.unlink(folderName+'/'+filename)#filename)
    #             paths.append(folderName+'\\'+filename)
    # for p in paths:
    #     print(p)
    #     send2trash.send2trash(p)


#ask id encrypting or decryting
test = input('enter search to decrypt or encrypt: ')
walkPath = 'C:/A Live in area/back to scool/python stuff/python-stuff/python/test/Ch15/New folder' #ask later
pword = 'swordfish'
if test[0] == 'e':
    walk(walkPath, True, pword)
elif test[0] == 'd':
    walk(walkPath, False, pword)
else:
    print('Need something that start with an e or d')