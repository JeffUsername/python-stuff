board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}


def chesstester(game):
    Tcounter = 0
    bkC = 0
    wkC = 0
    wqC = 0
    bqC = 0
    brC = 0
    wrC = 0
    bnC = 0
    wnC = 0
    bbC = 0
    wbC = 0
    bpC = 0 
    wpC = 0
    boardTest = True
    for i,j in game.items():
            #print('echo ' + i + ' ' + j)
            
            if ord(i[1]) > 104 or ord(i[1]) < 97:   #y valuse off board
                boardTest = testfail("OFF THE BOARD!!")
                break
            if int(i[0]) > 8 or int(i[0]) < 1:   #x valuse off board
                boardTest = testfail("OFF THE BOARD!!")
                break
            #cases
            if j == 'bking': #oh god why
                bkC += 1
            if j == 'wking':
                wkC += 1
            if j == 'bqueen':
                bqC += 1
            if j == 'wqueen':
                wqC += 1
            if j == 'brook':
                brC += 1
            if j == 'wrook':
                wrC += 1
            if j == 'bknight':
                bnC += 1
            if j == 'wknight':
                wnC += 1
            if j == 'bbishop':
                bbC += 1
            if j == 'wbishop':
                wbC += 1
            if j == 'bpawn':
                bpC += 1
            if j == 'wpawn':
                wpC += 1

            #final check
            if bkC > 1 or wkC > 1 or wqC > 1 or bqC > 1: #check royals
                boardTest = testfail("Too much Royalty")
                break
            if brC > 2 or wrC > 2 or bnC > 2 or wnC > 2 or bbC > 2 or wbC > 2: #check retainers
                 boardTest = testfail("Too many Retainers")
                 break
            if wpC > 8 or bpC > 8: #check pawns
                 boardTest = testfail("Too many Pawns")
                 break
            if j  !=  '':
                Tcounter += 1
            if Tcounter >32:   #check for too many pieces
                boardTest = testfail("too many peices!!")
                #break
            
    #print('bp ' + str(wpC) + ' : ' + 'wp' + str(wpC))
    if boardTest == True:
        print('Good Board')
    


def testfail(reason):
    print("invalid chess, " + reason)
    return False

if __name__ == "__main__":
    chesstester(board)