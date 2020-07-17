import ezsheets, openpyxl
# wb = openpyxl.Workbook('produceSales.xlsx')
# sheet = wb['Sheet']
fileName = input('enterfile name to be add (must be in folder)')

ezsheets.upload(fileName)
fullList =ezsheets.listSpreadsheets()
firstTup = list(fullList.keys())[0]
#print(firstTup)

ss = ezsheets.Spreadsheet(firstTup)
ss.downloadAsExcel('a_different_filename.xlsx')
ss.downloadAsODS('somthing_else.AsODS')