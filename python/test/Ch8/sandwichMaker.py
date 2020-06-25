import pyinputplus as pyip
import re
cost = 0.00  #for running total

sammaches = int(input('Enter the number of sandwiched you want: ')) #get number of sammaches

for len in range(sammaches):  #iterates by number of sammies
    print(len)
    getCostRegex = re.compile(r'(\d+\.\d+)')
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered= True) #get meat
    cost += 1.00
    meat = pyip.inputMenu(['chicken $5.00', 'turkey $6.90', 'ham $7.00', 'tofu $4.20'], numbered= True) #get meat
    findCost = getCostRegex.search(meat) #regex for dollars
    cost += float(findCost.group(0)) #add to cost
    cheaseYN = pyip.inputYesNo('Do you want the upcharge for cheese? ') #ask for cheese
   # print(cheaseYN)
    if cheaseYN == 'yes' or cheaseYN == 'y': #if cheese
        chees = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered= True) #get cheeses
        cost += 1.00    #add to cost
    condYN = pyip.inputYesNo('Do you want the upcharge for each condinment? ') #ak for condiments
    if condYN =='yes' or condYN =='y': #if condis
        condiments = ['mayo', 'mustard', 'lettuce','tomato'] #list of codnis
        for condiment in condiments: #loop to ask each option
            promt = pyip.inputYesNo('Do you want the upcharge for %s: ' % condiment)
            if promt =='yes' or promt == 'y': #adds 1 to cost for each yes
                cost += 1.00
    
print(cost) #print total

