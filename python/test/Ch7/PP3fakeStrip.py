import re

# namesRegex = re.compile(r' (\w*\s*)* ')
# othersRegex = re.compile(r'(\w*\s*)*')

def fakeStrip(x, y):

    if y =='': #use the cutter for front and back
        namesRegex = re.compile(r'^(\s*)(.*)(\s)*$')
        idk = namesRegex.search(x)
        print(idk.group(2))
    else: #now use regex
        idk2 = othersRegex = re.sub(y,'',x)
        print(idk2)

print('enter thing to be edited')
thing = input()
print('enter what will be removed, or nothing for white space')
control = input()
fakeStrip(thing, control)