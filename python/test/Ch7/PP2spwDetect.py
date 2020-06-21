import re

pwlRegex = re.compile(r'\w{8,}')
pwlowerRegex = re.compile(r'[a-z]+')
pwUpperRegex = re.compile(r'[A-Z]+')
pwdigRegex = re.compile(r'[0-9]+')

def testPassword(pw):
    good_pw = True
    if pwlRegex.search(pw):
         if pwlowerRegex.search(pw) and pwUpperRegex.search(pw) and pwdigRegex.search(pw):
             print('idk')
             return good_pw
    else:
        return False

if __name__ == "__main__":
    pword = str(input())
    if testPassword(pword) == True:
        print(pword + ' is  GOOD password!!!!!')
    else:
        print('Sorry, bad pword')