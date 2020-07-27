# import PyPDF2
# pdfFileObj = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())
# pdfFileObj.close()

# import PyPDF2
# # pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

# # print(pdfReader.isEncrypted)
# #pdfReader.getPage(0)
# pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# print(pdfReader.decrypt('rosebud'))
# pageObj = pdfReader.getPage(0)
# print(pageObj)
import PyPDF2
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

#ended at rotate