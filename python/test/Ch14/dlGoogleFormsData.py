#101rvxKKcjTBhAxPDUm7gllKopLDcfvL6D4TVQ6nXMKY
import ezsheets

#get form
ss = ezsheets.Spreadsheet('101rvxKKcjTBhAxPDUm7gllKopLDcfvL6D4TVQ6nXMKY')
#get sheet
sheet=ss[0]#.open('Form Responses 1')    #Form Responses 1
#create list
emailList =[]
finalList =[]
removed = ['','Enter Your Email']
#get emails with getCol
emailList = sheet.getColumn(4)
print(sheet.columnCount)
for i in emailList:
    if i in removed:
        continue
    finalList.append(i)
#print list
print(finalList)