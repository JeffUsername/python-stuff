def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    print(number)
    return number


num = input()
try:  
    num = int(num)
    while num != 1:
        num = collatz(num)

except ValueError:
    print('Enter an int, stupid')