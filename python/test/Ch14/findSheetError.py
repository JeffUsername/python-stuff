import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

wrong = []
count = 2
next = ss[0].getRow(count)[1]
print(next)
while next != '':
        if int(ss[0].getRow(count)[0]) * int(ss[0].getRow(count)[1]) != int(ss[0].getRow(count)[2]):
            wrong.append('row ' + str(count))
        count +=1
        next = ss[0].getRow(count)[1]
print(count)
print(wrong)