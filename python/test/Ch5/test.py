myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

print(myCat['size'])
print( 'My cat has ' + myCat['color'] + ' fur.')

message = 'It was a bright cold day in April, and the clocks were strikingthirteen                              .'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)    