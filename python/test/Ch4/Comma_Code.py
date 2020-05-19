def comma_code(thing):
    j = ''
    h = len(thing)
    for i in range(h):
        if i == len(thing)-1:
           j = j + "and " + thing[i] #add ", and " + [i]
        else:
          j = j + thing[i]+ ", "  #add ", " + [i] 

    return j

spam = ['apples', 'bananas', 'tofu', 'cats']

str_of_spam = comma_code(spam)

print(str_of_spam)
spam = []

str_of_spam = comma_code(spam)

print(str_of_spam)