
def printTable(tab): #sets ip recursion
    h = len(tab)
    w = len(tab[0])
    lLen =0
    printT_Helper(tab, h, w, lLen)
    

def printT_Helper(tab, h, w, lLen): #recursive helper
    
    if w>0:
        t = str(tab[0][w-1] + ' '+ tab[1][w-1] + ' ' + tab[2][w-1])
        s = len(t)
        
        if s > lLen:
            lLen = s
        z =  printT_Helper(tab, h, w-1, lLen) #rec call
        #print(z)
        t = t.rjust(((z-lLen)+ lLen), '-')
        print(t)
        if lLen < z:
            lLen = z
        return z
    else:
        #print(lLen)
        return lLen


if __name__ == "__main__":
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
    
    printTable(tableData)