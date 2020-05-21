import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_list = []
    for i in range(100):
        coin_list =coin_list + [random.randint(0, 1)]
        
    # Code that checks if there is a streak of 6 heads or tails in a row.
    j = 0
    while j+6 <= 100:
        #t = ''
        t = str(coin_list[j:j+6])
        #print(t)
        if t == '[0, 0, 0, 0, 0, 0]' or t == '[1, 1, 1, 1, 1, 1]':
            numberOfStreaks = numberOfStreaks + 1
            j+=5
        j+=1
print('Chance of streak: %s%%' % (numberOfStreaks / 1000000))