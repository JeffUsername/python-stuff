import PyPDF2, sys,os
from pathlib import Path
#get dic
test = input('enter f to fail and anything to succeed: ')
if test == 'f':
    pdfReader = PyPDF2.PdfFileReader(open('meetingminutes.pdf', 'rb'))
else:
    pdfReader = PyPDF2.PdfFileReader(open('encryptedminutes.pdf', 'rb'))

dicFile = open('dictionary.txt')

if pdfReader.isEncrypted == False:
    print('File is NOT!!! encrypted fool!')
    sys.exit()

#readlines of dic
for line in dicFile.readlines():
    #use line to test pword if statement, break if true test lower and upper.
    temp = line.replace('\n','')
    tim = pdfReader.decrypt(temp)
    if tim ==1:
        print('tim is great success!pw is: ' + line)
        sys.exit()
    t2 = temp.lower() 
    jim = pdfReader.decrypt(t2)
    print(jim)
    if jim == 1:
        print('jim is great success! pw is: ' + line)
        sys.exit()

print('sorry pw not here')