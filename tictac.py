import random
def entering(pl):
    inp=input('Enter the position to play in x y format: ').split()
    x=int(inp[0])-1
    y=int(inp[1])-1
    if tictac[x][y]==0:
        tictac[x][y]=pl
    else:
        print('Position already occupied\nTry Again')
        entering(pl)
        
def centering(pl):
    x=random.randint(-1,2)
    y=random.randint(-1,2)
    if tictac[x][y]==0:
        tictac[x][y]=pl
    else:
        centering(pl)
    
tictac=[[0,0,0],
        [0,0,0],
        [0,0,0]]
f=0
p=input("Do you wanna play it as 2 player or 1 player?(1/2): ")
if p=='2':
    for i in range(9):
        if i%2==0:
            print("\nPlayer 1's turn")
            entering(1)
        else:
            print("\nPlayer 2's turn")
            entering(2)
        print(tictac[0])
        print(tictac[1])
        print(tictac[2])
        for j in range(3):
            if tictac[j].count(tictac[j][0])==3 and tictac[j][0]!=0:
                print('Player ' + str(tictac[j][0])+' Wins!!!')
                f=1
                break
            elif tictac[0][j]==tictac[1][j] and tictac[1][j]==tictac[2][j] and tictac[0][j]!=0:
                print('Player ' + str(tictac[0][j])+' Wins!!!')
                f=1
                break
            elif tictac[0][0]==tictac[1][1] and tictac[1][1]==tictac[2][2] and tictac[0][0]!=0:
                f=1
                print('Player ' + str(tictac[0][0])+' Wins!!!')
                break
            elif tictac[0][2]==tictac[1][1] and tictac[1][1]==tictac[2][0] and tictac[0][2]!=0:
                f=1
                print('Player ' + str(tictac[0][0])+' Wins!!!')
                break
        if f:
            break
    else:
        print("DRAW   :(")
elif p=='1':
    for i in range(9):
        if i%2==0:
            print("\nPlayer 1's turn")
            entering(1)
        else:
            print("\nComputer's turn")
            centering(2)
        print(tictac[0])
        print(tictac[1])
        print(tictac[2])
        for j in range(3):
            if tictac[j].count(tictac[j][0])==3 and tictac[j][0]!=0:
                if tictac[j][0]==2:
                    print("Computer Wins!!!")
                else:
                    print('Player ' + str(tictac[j][0])+' Wins!!!')
                f=1
                break
            elif tictac[0][j]==tictac[1][j] and tictac[1][j]==tictac[2][j] and tictac[0][j]!=0:
                if tictac[0][j]==2:
                    print("Computer Wins!!!")
                else:
                    print('Player ' + str(tictac[j][0])+' Wins!!!')
                f=1
                break
            elif tictac[0][0]==tictac[1][1] and tictac[1][1]==tictac[2][2] and tictac[0][0]!=0:
                f=1
                if tictac[0][0]==2:
                    print("Computer Wins!!!")
                else:
                    print('Player ' + str(tictac[j][0])+' Wins!!!')
                break
            elif tictac[0][2]==tictac[1][1] and tictac[1][1]==tictac[2][0] and tictac[0][2]!=0:
                f=1
                if tictac[0][2]==2:
                    print("Computer Wins!!!")
                else:
                    print('Player ' + str(tictac[j][0])+' Wins!!!')
                break
        if f:
            break
    else:
        print("DRAW   :(")
    
else:
    print("Invalid Input")
