#! python3

import pyperclip, re

def dateValidater(date):
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])
   # print(str(day) + ' : ' + str(month) + ' : ' +str(year))
    if year > 3000 or year < 999: #year 1000 to 2999
        return False
    if month > 12 or month < 1:
        return False
    if month == 4 or 6 or 9 or 11:
        if day < 1 or day > 30:
            return False
    elif year % 4 ==0 and month ==2:
        if year % 100 != 0 and year % 400 !=0:
            if day < 1 or day > 28:
                return False
        if day < 1 or day > 29:
            return False
    elif month == 2:
        if day < 1 or day > 28:
            return False
    elif day < 1 or day > 31:
        return False
        
    return True
#i hate this part
dateValidaterRegex = re.compile(r'''(
    (09|06|04|11)+([1-2]+[0-9]|[3]+[0]|[0]+[1-9])+[1-2]+[0-9]+[0-9]+[0-9]#([1-30]+/+04|06|04|11+/+[1000-2999])
    |(01|03|05|07|08|10|12)+([1-2]+[0-9]|[3]+[0]|[0]+[1-9])+[1-2]+[0-9]+[0-9]+[0-9] #[01]|[03]|[04]|[07]|[08]|[10]|[12](01|03|05|07|08|10|12)
    |(2)+([2]+[0-8]|[0-1]+[1-9])+[1-2]+[0-9]+[0-9]+[0-9]
    )''', re.VERBOSE)

dateRegex = re.compile(r'''(
    (\d{2}) #day 00
    (/)  # '/'
    (\d{2}) # month mm
    (/)  # '/'
    (\d{4}) # year yyyy
    )''', re.VERBOSE)


text = str(pyperclip.paste())
#print(text)

matches = []
for groups in dateRegex.findall(text):
    #print('echo for')
    #print(groups[0])
    i =groups[3]+groups[1]+groups[5]
    #print(i)
    #i = groups[0]
    d = groups[1]
    m= groups[3]
    y= groups[5]
    # #print(i + ' print of i')
    goodDate = dateValidater(groups[0])
    if dateValidaterRegex.search(i):
        #print(groups[0])
        matches.append(groups[0])

    elif goodDate == True:
         matches.append(groups[0])


    # #print(gd)
    #goodDate = dateValidater(groups[0]) #call date validator
    #if goodDate == True:
        #matches.append(str(gd))

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No dates found.')
#31/02/2020 or 31/04/2021 and 01/01/2001 t 29/02/1999 d 30/04/2020 30/03/2020 po 28/02/1999