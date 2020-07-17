import ezsheets
ss = ezsheets.Spreadsheet('1QWeskhphyhEjIcdBziAvaFwkDni08AJaftSNnUQzkpE')
print(ss.title)
i =ezsheets.listSpreadsheets()
#print(i.values())
#print(i.items())
for item in i.items():
    print(item[1])