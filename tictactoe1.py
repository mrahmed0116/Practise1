'''
Tic tac toe game when using a coursework
'''
lines = "-------------"
cells= [' ',' ',' ',' ',' ',' ',' ',' ',' ']
game=0
winner = ' '
def output(cells):
    print(lines)
    print("| " + cells[0] + " | " + cells[1] + " | " + cells[2] + " |")
    print(lines)
    print("| " + cells[3] + " | " + cells[4] + " | " + cells[5] + " |")
    print(lines)
    print("| " + cells[6] + " | " + cells[7] + " | " + cells[8] + " |")
    print(lines)
def check(cells1):
    winner = ' '
    game = 0
    if cells1[0] == cells1[1] == cells1[2]:
        winner = cells1[0]
        if winner != ' ':
            game = game + 1
        # print('first row')
    if cells1[3] == cells1[4] == cells1[5]:
        winner = cells1[3]
        if winner != ' ':
            game = game + 1
        # print('second row')
    if cells1[6] == cells1[7] == cells1[8]:
        winner = cells1[6]
        if winner != ' ':
            game = game + 1
        # print('3rd row')
        # print(cells[6] + 'this is cell6')
    if cells1[0] == cells1[3] == cells1[6]:
        winner = cells1[0]
        if winner != ' ':
            game = game + 1
        # print('first column')
        # print(cells[6]+'this is cell6')
    if cells1[1] == cells1[4] == cells1[7]:
        winner = cells1[1]
        if winner != ' ':
            game = game + 1
        # print('second column')
    if cells1[2] == cells1[5] == cells1[8]:
        winner = cells1[2]
        if winner != ' ':
            game = game + 1
        # print('third column')
    if cells1[0] == cells1[4] == cells1[8]:
        winner = cells1[0]
        if winner != ' ':
            game = game + 1
        # print('first diagnomal')
    if cells1[2] == cells1[4] == cells1[6]:
        winner = cells1[2]
        if winner != ' ':
            game = game + 1
        #print('second diagonal')
    return (game,winner)
def update(cells2):
    game2 = 0
    winner2 = ' '
    x_list = [x for x in cells2 if x == 'X']
    o_list = [y for y in cells2 if y == 'O']
    _list= [z for z in cells2 if z==' ']
    t = len(x_list) + len(o_list)
    parity1 =''
    z = 'X'
    if t==9:
        game2, winner2 = check(cells2)
        return game2, winner2
    elif t<9:
        while t <9:
            #print(str(t)+'in while loop')

            if parity1 == 'X':
                z ='O'
            elif parity1 == 'O':
                z= 'X'
            x, y = input("Enter the coordinates").split(" ")
            parity1 = z
            if x.isdigit() and y.isdigit():
                if int(x) > 3 or int(y) > 3:
                    print('Coordinates should be from 1 to 3!')
                elif x == '1' and y == '1':
                    if cells2[6] == 'X' or cells2[6] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        cells[6] = z
                        game2, winner2 = check(cells2)
                        output(cells2)
                        # print(game1)
                elif x == '1' and y == '2':
                    if cells2[3] == 'X' or cells2[3] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        cells2[3] = z
                        game2, winner2 = check(cells2)
                        output(cells2)
                elif x == '1' and y == '3':
                    if cells2[0] == 'X' or cells2[0] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        cells2[0] = z
                        game2, winner2 = check(cells2)
                        #print(game2)
                        #print(winner2)
                        output(cells2)
                        # print(game1)
                        # print('game1 is this')
                elif x == '2' and y == '1':
                    if cells2[7] == 'X' or cells2[7] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        cells2[7] = z
                        game2, winner2 = check(cells2)
                        output(cells2)
                elif x == '2' and y == '2':
                    if cells2[4] == 'X' or cells2[4] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        cells2[4] = z
                        game2, winner2 = check(cells2)
                        output(cells2)
                elif x == '2' and y == '3':
                    if cells2[1] == 'X' or cells2[1] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        cells2[1] = z
                        game2, winner2 = check(cells2)
                        output(cells2)
                elif x == '3' and y == '1':
                    if cells2[8] == 'X' or cells2[8] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        cells2[8] = z
                        game2, winner2 = check(cells2)
                        output(cells2)
                elif x == '3' and y == '2':
                    if cells2[5] == 'X' or cells2[5] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        cells2[5] = z
                        game2, winner2 = check(cells2)
                        output(cells2)
                elif x == '3' and y == '3':
                    if cells2[2] == 'X' or cells2[2] == 'O':
                        print('This cell is occupied! Choose another one!')
                    else:
                        cells2[2] = z
                        game2, winner2 = check(cells2)
                        output(cells2)
            else:
                print('You should enter numbers!')
            if game2>0 and winner2 != ' ':
                return game2, winner2
            x_list = [x for x in cells2 if x == 'X']
            o_list = [y for y in cells2 if y == 'O']
            t = len(x_list) + len(o_list)
            if t>=9:
                return game2, winner2
            #print(t)
            #print('Value of t')
output(cells)
game, winner = update(cells)
#print(winner)
#print(game)
x1_list = [x for x in cells if x == 'X']
o1_list = [x for x in cells if x == 'O']
_1list = [x for x in cells if x == ' ']

if abs(len(x1_list) - len(o1_list)) > 1:
    print('Impossible')
elif ((len(x1_list) + len(o1_list) <5) or len(_1list)!=0) and (game==0 or winner==" "):
    print('Game not finished')
elif game==1 and winner != " ":
    print(winner+' wins')
elif winner==" " and game==0:
    print('Draw')
elif game>1:
    print('Impossible')