# import os
# RANDOM FOR GETTING RANDOM INTEGERS
import random
# FOR MAKING IT BEAUTFUL / COLORFUL
from colorama import Fore, Back, Style
#FOR COLORFUL PROGRAM
from time import sleep
#TO HAVE SLEEP
from os import system, name
#INTRODUCTION
print(Fore.BLACK + Back.WHITE + 'WELCOME TO TIC TAC TOE GAME',Style.RESET_ALL)
print(Fore.CYAN+Back.WHITE+'HOPE U WILL LIKE THE GAME !',Style.RESET_ALL)
#DEVELOPER NAME
print(Fore.GREEN,'GAME BY ---> NAMAN ANAND\n',Style.RESET_ALL)
r = 1 # for move number
player1 = 1 # whose turn we want we allot value 1
player2 = 0 
####################################################################################################################################################
#GAMEBOARD2 IF NEEDED FOR LATER IN PROJECT
GameBoard_2 = ["_","_","_",
               "_","_","_",
               "_","_","_"]
####################################################################################################################################################

# MAIN LIST WE HAVE MADE FOR STORING THE GAME PLAY
GameBoard = [" "," "," ",
             " "," "," ",
             " "," "," "]
####################################################################################################################################################
#THIS ARRAY I AM USING FOR SEEING WHETHER THAT INDEX IS FILLED OR NOT
A = [0,0,0,0,0,0,0,0,0]
####################################################################################################################################################
# FOR display of the main board 
def Blue_board():
     print(Fore.LIGHTBLUE_EX)
     print("   |   |   ")
     print(" "+GameBoard[0]+" "+"|"+" "+GameBoard[1]+" "+"|"+" "+GameBoard[2]+" ")
     print("---|---|---")
     print(" "+GameBoard[3]+" "+"|"+" "+GameBoard[4]+" "+"|"+" "+GameBoard[5]+" ")
     print("---|---|---")
     print(" "+GameBoard[6]+" "+"|"+" "+GameBoard[7]+" "+"|"+" "+GameBoard[8]+" ")
     print("   |   |   ")
####################################################################################################################################################
#THIS IS MAIN BOARD
# PLAYERS WILL PLAY IN THIS BOARD
def MainBoard():
     print(Fore.LIGHTYELLOW_EX)
     print("   |   |   ")
     print(" "+GameBoard[0]+" "+"|"+" "+GameBoard[1]+" "+"|"+" "+GameBoard[2]+" ")
     print("---|---|---")
     print(" "+GameBoard[3]+" "+"|"+" "+GameBoard[4]+" "+"|"+" "+GameBoard[5]+" ")
     print("---|---|---")
     print(" "+GameBoard[6]+" "+"|"+" "+GameBoard[7]+" "+"|"+" "+GameBoard[8]+" ")
     print("   |   |   ")
####################################################################################################################################################

# IndexBoard ->Display indexes
def Indexboard():
    #  print(Fore.LIGHTBLUE_EX)
     print(Fore.LIGHTGREEN_EX)
     print("   |   |   ")
     print(" "+'1'+" "+"|"+" "+'2'+" "+"|"+" "+'3'+" ")
     print("---|---|---")
     print(" "+'4'+" "+"|"+" "+'5'+" "+"|"+" "+'6'+" ")
     print("---|---|---")
     print(" "+'7'+" "+"|"+" "+'8'+" "+"|"+" "+'9'+" ")
     print("   |   |   ")

####################################################################################################################################################
# print("OUR GAME BOARD IS ->")
# Blue_board()
# print()
####################################################################################################################################################
# RulesForGame
# I WILL DISPLAY AFTER EVERY MOVE SO THAT IF A NEW PLAYER COME HE CAN ALSO PLAY INSTEAD OF PREV PLAYER
def RulesForGame():
    print(Fore.LIGHTCYAN_EX)
    print("GAME RULE ")
    print('TO FILL A PARTICULAR BOX , ENTER THE VALUE OF THE INDEX ')
    print('INDEX ARE AS GIVEN BELOW : ')
    Indexboard()
####################################################################################################################################################
####################################################################################################################################################
#THIS IS USED FOR CHANGING TURNS BETWEEN PLAYER
def TurnChanger():
    global r
    global player1
    global  player2
    r = r+1
    #increase the value each time we call
    #making which player to be active
    if r%2==0:
        player1 = 0
        player2 = 1
    else:
        player1 = 1
        player2 = 0
####################################################################################################################################################
#SEEING WHOSE CHANCE IS NOW
def whoseChance():
    global r
    global player1
    global  player2
    if(player1==1):
        print(Fore.LIGHTMAGENTA_EX+'PLAYER 1 CHANCE')
    else :
        print(Fore.GREEN+'PLAYER 2 CHANCE')
####################################################################################################################################################
#CHECK INVALID STEPS
def InvalidStepChecker(i):
        n1 = 1
        if i<1:
            # if value is less than 1 then we have to exit
            print(Fore.RED)
            print('PLEASE ENTER VALUE B/W 1 TO 9')
            n1 = 0
        elif i>9:
            # if value is greater than 9 then we have to exit
            print(Fore.RED)
            print('PLEASE ENTER VALUE B/W 1 TO 9')
            n1 = 0
        elif A[i-1]!=0:
            # if the value is already filled 
            print(Fore.RED)
            print('THIS POSITION IS ALREADY FILLED')
            n1 = 0
        return n1
####################################################################################################################################################
def WinnerChecker():
    # either it should be in row fill for player 1 to win
    if((GameBoard[0]=='X') and (GameBoard[1]=='X') and (GameBoard[2]=='X')):
        print('CONGRATS Player 1 !! U HAVE WON')
        return 1
    elif((GameBoard[3]=='X') and (GameBoard[4]=='X') and (GameBoard[5]=='X')):
        print('CONGRATS Player 1 !! U HAVE WON')
        return 1
    elif((GameBoard[6]=='X') and (GameBoard[7]=='X') and (GameBoard[8]=='X')):
        print('CONGRATS Player 1 !! U HAVE WON')
        return 1
    #either it should be in column fill for player 1 to win
    elif((GameBoard[0]=='X') and (GameBoard[3]=='X') and (GameBoard[6]=='X')):
        print('CONGRATS Player 1 !! U HAVE WON')
        return 1
    elif((GameBoard[1]=='X') and (GameBoard[4]=='X') and (GameBoard[7]=='X')):
        print('CONGRATS Player 1 !! U HAVE WON')
        return 1
    elif((GameBoard[2]=='X') and (GameBoard[5]=='X') and (GameBoard[8]=='X')):
        print('CONGRATS Player 1 !! U HAVE WON')
        return 1
    #either it should be diagonal fill for player 1 to win
    elif((GameBoard[0]=='X') and (GameBoard[4]=='X') and (GameBoard[8]=='X')):
        print('CONGRATS Player 1 !! U HAVE WON')
        return 1
    elif((GameBoard[2]=='X') and (GameBoard[4]=='X') and (GameBoard[6]=='X')):
        print('CONGRATS Player 1 !! U HAVE WON')
        return 1
    elif((GameBoard[0]=='O') and (GameBoard[1]=='O') and (GameBoard[2]=='O')):
    # either it should be in row fill for player 2 to win
        print('CONGRATS PLAYER 2 !! U HAVE WON')
        return 2
    elif((GameBoard[3]=='O') and (GameBoard[4]=='O') and (GameBoard[5]=='O')):
        print('CONGRATS PLAYER 2 !! U HAVE WON')
        return 2
    elif((GameBoard[6]=='O') and (GameBoard[7]=='O') and (GameBoard[8]=='O')):
        print('CONGRATS PLAYER 2 !! U HAVE WON')
        return 2
    #either it should be in column fill for player 2 to win
    elif((GameBoard[0]=='O') and (GameBoard[3]=='O') and (GameBoard[6]=='O')):
        print('CONGRATS PLAYER 2 !! U HAVE WON')
        return 2
    elif((GameBoard[1]=='O') and (GameBoard[4]=='O') and (GameBoard[7]=='O')):
        print('CONGRATS PLAYER 2 !! U HAVE WON')
        return 2
    elif((GameBoard[2]=='O') and (GameBoard[5]=='O') and (GameBoard[8]=='O')):
        print('CONGRATS PLAYER 2 !! U HAVE WON')
        return 2
    #either it should be in diagonal fill for player 2 to win
    elif((GameBoard[0]=='O') and (GameBoard[4]=='O') and (GameBoard[8]=='O')):
        print('CONGRATS PLAYER 2 !! U HAVE WON')
        return 2
    elif((GameBoard[2]=='O') and (GameBoard[4]=='O') and (GameBoard[6]=='O')):
        print('CONGRATS PLAYER 2 !! U HAVE WON')
        return 2
    else:
        return 5
####################################################################################################################################################
#MULTIPLAYER
def PlayMultiPlayer():
    print('PLAYER 1 -> X ')
    print('PLAYER 2 -> O ')
    #taking the already defined global variables
    global r
    global player2
    global player1
    while r!=10:   
        # DISPLAYING RULES AFTER EACH GAME 
        RulesForGame()
        # DISPLAY WHO WILL MOVE
        whoseChance()
        i = int(input("ENTER INPUT NUMBER  : "))
        #CHECKING FOR INVALID STEPS
        o = InvalidStepChecker(i)
        if o==0:
            MainBoard()
            continue
        A[i-1]= 1
        if(player1==1):
            GameBoard[i-1]= 'X'
        elif(player2==1):
            GameBoard[i-1]= 'O'
        #DISPLAYING MAIN BOARD AFTER EACH MOVE
        MainBoard()
        #CHECKING IF ANYONE HAD WIN
        q = WinnerChecker()
        if (q==1):
            quit()
        elif(q==2):
            quit()
        TurnChanger()
        # print(player1," ",player2," ")
    if r==10:
        print(Fore.LIGHTCYAN_EX)
        print("RESULT ->")
        print("THE GAME HAS BEEN DRAWN")
        print("BOTH PLAYERS PERFORMED WELL")


####################################################################################################################################################
# for who will play first
def whoPlayFirst():
    return random.randint(1,2)

####################################################################################################################################################
####################################################################################################################################################
# BETWEEN GAME PLAY MOSTLY ALL PROCEDURE SAME SO I HAVE NOT COMMENTED EVERY TIME PLEASE SEE MY MULTIPLAYER COMMENETS TO VIEW ANYTHING IF NOT SPECIFIED
####################################################################################################################################################

# if u want to play easy game with as single player 1
def PlaySinglePlayerAsPlayer1():
    print(Fore.WHITE)
    UserName = input("NAME OF USER : ")
    print(UserName," U ARE PLAYER 1 ")
    print('PLAYER 1 -> X ')
    print('PLAYER 2 -> O ')
    # print("DO U WANT 1ST MOVE OR 2ND TYPE Y FOR FIRST ELSE U WILL B")
    # PLAYER 1 AND PLAYER 2 ARE ABOVE DEFINED ; TO USE IT AS GLOBAL WE MENTION GLOBAL
    global r
    global player1
    global player2
    while r!=10: 
        whoseChance()
        if(player1==1):
            RulesForGame()
            i = input("ENTER INPUT NUMBER : ")
            i = int(i)
            o = InvalidStepChecker(i)
            if o==0:
                MainBoard()
                # sleep(2)
                # system('clear')
                continue
            A[i-1]= 1
            GameBoard[i-1]= 'X'
        if(player2==1):
            #EASY GAME SO I AM USING RANDOM
            var1 = random.randint(1, 9)
            o = InvalidStepChecker(var1)
            if o==0:
                MainBoard()
                # sleep(2)
                # system('clear')
                continue
            A[var1-1]= 1
            GameBoard[var1-1]= 'O'
        MainBoard()
        q = WinnerChecker()
        if (q==1):
            quit()
        elif(q==2):
            quit()
        TurnChanger()
        # print(player1," ",player2," ")
    if r==10:
        print(Fore.LIGHTCYAN_EX)
        print("RESULT ->")
        print("THE GAME HAS BEEN DRAWN")
        print("BOTH PLAYERS PERFORMED WELL")


####################################################################################################################################################

# if u want to play easy game with as single player 2
def PlaySinglePlayerAsPlayer2():
    UserName = input("USER NAME : ")
    print(UserName," U ARE PLAYER 2 ")
    print('PLAYER 1 -> X ')
    print('PLAYER 2 -> O ')
    # print("DO U WANT 1ST MOVE OR 2ND TYPE Y FOR FIRST ELSE U WILL B")
    global r
    global player1
    global player2
    while r!=10: 
        whoseChance()
        if(player2==1):
            RulesForGame()
            i = input("ENTER INPUT NUMBER : ")
            # try:  
            #     i = int(i)
            # except ValueError:
            #      print("That's not an int!")
            # i have specifically mentioned user to enter number here 
            i = int(i)
            o = InvalidStepChecker(i)
            if o==0:
                MainBoard()
                # sleep(2)
                # system('clear')
                continue
            A[i-1]= 1
            GameBoard[i-1]= 'X'
        if(player1==1):
            # EASY GAME SO USING RANDOM
            var1 = random.randint(1, 9)
            o = InvalidStepChecker(var1)
            if o==0:
                MainBoard()
                # sleep(2)
                # system('clear')
                continue
            A[var1-1]= 1
            GameBoard[var1-1]= 'O'
        MainBoard()
        q = WinnerChecker()
        if (q==1):
            quit()
        elif(q==2):
            quit()
        TurnChanger()
        # print(player1," ",player2," ")
    if r==10:
        print(Fore.LIGHTCYAN_EX)
        print("RESULT ->")
        print("THE GAME HAS BEEN DRAWN")
        print("BOTH PLAYERS PERFORMED WELL")


####################################################################################################################################################
# play easy game as single player
def PlayAsSinglePlayer():
    t5 = whoPlayFirst()
    print(Fore.GREEN)
    print("WHO WILL PLAY FIRST IS RANDOMLY DECIDED ")
    if (t5==1):
        PlaySinglePlayerAsPlayer1()
    else:
        PlaySinglePlayerAsPlayer2()
####################################################################################################################################################
# ASKING DIFFICULT LEVEL EASY OR HARD
def AskDifficulty():
    print(Fore.CYAN)
    print("YOU WANT TO PLAY GAME OF WHICH DIFFICULTY LEVEL :-")
    print("ENTER ONE OF CHOICES")
    print(Fore.LIGHTBLUE_EX)
    print("EASY      -> A ")
    print(Fore.LIGHTMAGENTA_EX)
    print("DIFFICULT -> B ")
    print(Fore.LIGHTBLACK_EX)
    print("EXIT ANY OPTION OTHER THAN ABOVE")
    print(Fore.LIGHTYELLOW_EX)
    qwerty = input("INPUT : ")
    if qwerty=='A':
        print("OUR GAME BOARD IS ->")
        Blue_board()
        print()
        PlayAsSinglePlayer()
    elif qwerty=='B':
        print("OUR GAME BOARD IS ->")
        Blue_board()
        print()
        print("DO U WANT TO PLAY FIRST OR SECOND MOVE")
        print(" enter 1 for playing first ")
        print("       2 for playing second ")
        print("       else exit           ")
        print(Fore.LIGHTCYAN_EX)
        naman1 = int(input("WHICH MOVE U WANT : "))
        if naman1==1:
            computerAIvsHuman()
        elif naman1 ==2 :
            computerAIvsHuman2()
        else:
            quit()
    else:
        quit()
####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################
# /REAL CODE DOWN THIS HAS SOME ERRORS SO I COMMENTED
# def mostefficentmove():
#     a1point = -100
#     a2movenumber = 10
#     for i in range(1,9):
#         if A[i-1]==0:
#             GameBoard[i-1]='X'
#             a2point= MinMax(0,False)
#             # a2point = MinMax()
#             GameBoard[i-1]=' '
#             if(a2point>a1point):
#                 a1point = a2point
#                 a2movenumber=i

#     GameBoard[a2movenumber-1]='X'
#     return
####################################################################################################################################################
# def MinMax(v,ismax):    
#     global r
#     op = WinnerCheckerAI()
#     if op==1:
#         return 2
#     elif op==2:
#         return -2
#     elif r==10:
#         return 0
#     if ismax:
#          a1point = -100
#          for i in range(1,9):
#              if A[i-1]==0:
#                  GameBoard[i-1]='X'
#                  a2point= MinMax(GameBoard,0,False)
#                  GameBoard[i-1]=' '
#                  if(a2point>a1point):
#                      a1point = a2point
#          return a1point
#     else :
#         a1point =1000
#         for i in range(1,9):
#              if A[i-1]==0:
#                  GameBoard[i-1]='O'
#                  a2point= MinMax(v+1,False)
#                  GameBoard[i-1]=' '
#                  if(a2point<a1point):
#                     a1point = a2point
#         return a1point
# ####################################################################################################################################################
# GAMEPLACE = {1: ' ', 2: ' ', 3: ' ',
#              4: ' ', 5: ' ', 6: ' ',
#              7: ' ', 8: ' ', 9: ' '}
####################################################################################################################################################
#CHECKING WHO WIN IN AI VS HUMAN
def WinnerCheckerAI():
    if((GameBoard[0]=='X') and (GameBoard[1]=='X') and (GameBoard[2]=='X')):
        return 1
    elif((GameBoard[3]=='X') and (GameBoard[4]=='X') and (GameBoard[5]=='X')):
        return 1
    elif((GameBoard[6]=='X') and (GameBoard[7]=='X') and (GameBoard[8]=='X')):
        return 1
    elif((GameBoard[0]=='X') and (GameBoard[3]=='X') and (GameBoard[6]=='X')):
        return 1
    elif((GameBoard[1]=='X') and (GameBoard[4]=='X') and (GameBoard[7]=='X')):
        return 1
    elif((GameBoard[2]=='X') and (GameBoard[5]=='X') and (GameBoard[8]=='X')):
        return 1
    elif((GameBoard[0]=='X') and (GameBoard[4]=='X') and (GameBoard[8]=='X')):
        return 1
    elif((GameBoard[2]=='X') and (GameBoard[4]=='X') and (GameBoard[6]=='X')):
        return 1
    elif((GameBoard[0]=='O') and (GameBoard[1]=='O') and (GameBoard[2]=='O')):
        return 2
    elif((GameBoard[3]=='O') and (GameBoard[4]=='O') and (GameBoard[5]=='O')):
        return 2
    elif((GameBoard[6]=='O') and (GameBoard[7]=='O') and (GameBoard[8]=='O')):
        return 2
    elif((GameBoard[0]=='O') and (GameBoard[3]=='O') and (GameBoard[6]=='O')):
        return 2
    elif((GameBoard[1]=='O') and (GameBoard[4]=='O') and (GameBoard[7]=='O')):
        return 2
    elif((GameBoard[2]=='O') and (GameBoard[5]=='O') and (GameBoard[8]=='O')):
        return 2
    elif((GameBoard[0]=='O') and (GameBoard[4]=='O') and (GameBoard[8]=='O')):
        return 2
    elif((GameBoard[2]=='O') and (GameBoard[4]=='O') and (GameBoard[6]=='O')):
        return 2
    else:
        return -1
####################################################################################################################################################
# THIS HAS SOME ERROR SO I COMMENTED
# def playAgainstComputer():
#     UserName = input("NAME : ")
#     print(UserName," U ARE PLAYER 2 ")
#     print('PLAYER 1 -> X ')
#     print('PLAYER 2 -> O ')
#     # print("DO U WANT 1ST MOVE OR 2ND TYPE Y FOR FIRST ELSE U WILL B")
#     global r
#     global player1
#     global player2
#     while r!=10: 
#         whoseChance()
#         if(player2==1):
#             RulesForGame()
#             i = input("ENTER INPUT NUMBER : ")
#             try:  
#                 i = int(i)
#             except ValueError:
#                  print("That's not an int!")
#             o = InvalidStepChecker(i)
#             if o==0:
#                 MainBoard()
#                 # sleep(2)
#                 # system('clear')
#                 continue
#             A[i-1]= 1
#             GameBoard[i-1]= 'X'
#         if(player1==1):
#             mostefficentmove()
#         MainBoard()
#         q = WinnerChecker()
#         if (q==1):
#             quit()
#         elif(q==2):
#             quit()
#         TurnChanger()
#         # print(player1," ",player2," ")
#         if r==10:
#             print(Fore.LIGHTCYAN_EX)
#             print("RESULT ->")
#             print("THE GAME HAS BEEN DRAWN")
#             print("BOTH PLAYERS PERFORMED WELL")
#         # quit()
# playAgainstComputer()
####################################################################################################################################################
 # CHECKING WHO WON AT HUMAN VS AI IN HARD GAME
def WinnerCheckerInAI():
    if WinnerCheckerAI()==1:
        print(Fore.YELLOW)
        print(Back.LIGHTCYAN_EX)
        print("CONGRATS ! U HAVE DEFEATED COMPUTER ")
        print(Style.RESET_ALL)
        quit()
    elif WinnerCheckerAI()==2:
        print(Back.LIGHTCYAN_EX)
        print(Fore.YELLOW)
        print("Sorry U lost ! COMPUTER AI WON ! ")
        print(Style.RESET_ALL)
        quit()
    else:
        return
####################################################################################################################################################
def computerAIvsHuman():
    print(Fore.WHITE)
    UserName = input("PLEASE ENTER YOUR NAME : ")
    print('PLAYER 1 -> X ')
    print('PLAYER 2 -> O ')
    print(UserName , " U ARE PLAYER 1")
    # print("DO U WANT 1ST MOVE OR 2ND TYPE Y FOR FIRST ELSE U WILL B")
    global r
    global player1
    global player2
    while r!=10: 
        whoseChance()
        if(player1==1):
            RulesForGame()
            i = input("ENTER INPUT NUMBER : ")
            i = int(i)
            o = InvalidStepChecker(i)
            if o==0:
                MainBoard()
                # sleep(2)
                # system('clear')
                continue
            A[i-1]= 1
            GameBoard[i-1]= 'X'
        if(player2==1):
            computermove()
        MainBoard()
        q = WinnerCheckerInAI()
        if (q==1):
            quit()
        elif(q==2):
            quit()
        TurnChanger()
        # print(player1," ",player2," ")
    if r==10:
        print(Fore.LIGHTCYAN_EX)
        print("RESULT ->")
        print("THE GAME HAS BEEN DRAWN")
        print("BOTH PLAYERS PERFORMED WELL")
####################################################################################################################################################
def computermove():
    print(Fore.BLUE)
    GamePoints = -1000
    MostEffMove = -1
    for x in range(1,10):
         if GameBoard[x-1]==' ':
            GameBoard[x-1]='O'
            h=0
            pointInThisMove = MinMaxFunc(GameBoard,h,False)
            # print("Check at ",x," THE POINTS FOR THIS MOVE : ",pointInThisMove)
            GameBoard[x-1]=' '
            if(pointInThisMove>GamePoints):
                MostEffMove=x
                GamePoints=pointInThisMove
    GameBoard[MostEffMove-1]='O'
    A[MostEffMove-1]=1
    print("COMPUTER CHANCE :")
    print("MOVE : ",MostEffMove)
    return
####################################################################################################################################################
def checkArrFill():
    for j in range(1,10):
        if GameBoard[j-1]==' ':
            return False
    return True
####################################################################################################################################################
def MinMaxFunc(GameBoard,height,isMax):
    if WinnerCheckerAI()==1:
        return -2
    elif WinnerCheckerAI()==2:
        return 2
    elif checkArrFill()==True:
        return 0
    
    if isMax:
            GamePoints = -1000
            for x in range(1,10):
                if GameBoard[x-1]==' ':
                    GameBoard[x-1]='O'
                    h=0
                    pointInThisMove = MinMaxFunc(GameBoard,0,False)
                    GameBoard[x-1]=' '
                    if(pointInThisMove>GamePoints):
                        GamePoints=pointInThisMove
            return GamePoints
    else:
            GamePoints = 1000
            for x in range(1,10):
                if GameBoard[x-1]==' ':
                    GameBoard[x-1]='X'
                    h=0
                    pointInThisMove = MinMaxFunc(GameBoard,height+1,True)
                    GameBoard[x-1]=' '
                    if(pointInThisMove<GamePoints):
                        GamePoints=pointInThisMove
            return GamePoints
####################################################################################################################################################
####################################################################################################################################################
def computerAIvsHuman2():
    print(Fore.WHITE)
    UserName = input("PLEASE ENTER YOUR NAME : ")
    print('PLAYER 1 -> O ')
    print('PLAYER 2 -> X ')
    print(UserName , " U ARE PLAYER 2")
    # print("DO U WANT 1ST MOVE OR 2ND TYPE Y FOR FIRST ELSE U WILL B")
    global r
    global player1
    global player2
    while r!=10: 
        whoseChance()
        if(player1==1):
            computermove()
        if(player2==1):
            RulesForGame()
            i = input("ENTER INPUT NUMBER : ")
            i = int(i)
            o = InvalidStepChecker(i)
            if o==0:
                MainBoard()
                # sleep(2)
                # system('clear')
                continue
            A[i-1]= 1
            GameBoard[i-1]= 'X'
        MainBoard()
        q = WinnerCheckerInAI()
        if (q==1):
            quit()
        elif(q==2):
            quit()
        TurnChanger()
        # print(player1," ",player2," ")
    if r==10:
        print(Fore.LIGHTCYAN_EX)
        print("RESULT ->")
        print("THE GAME HAS BEEN DRAWN")
        print("BOTH PLAYERS PERFORMED WELL")
####################################################################################################################################################
# def computermove():
#     print(Fore.BLUE)
#     GamePoints = -1000
#     MostEffMove = -1
#     for x in range(1,10):
#          if GameBoard[x-1]==' ':
#             GameBoard[x-1]='O'
#             h=0
#             pointInThisMove = MinMaxFunc(GameBoard,h,False)
#             # print("Check at ",x," THE POINTS FOR THIS MOVE : ",pointInThisMove)
#             GameBoard[x-1]=' '
#             if(pointInThisMove>GamePoints):
#                 MostEffMove=x
#                 GamePoints=pointInThisMove
#     GameBoard[MostEffMove-1]='O'
#     A[MostEffMove-1]=1
#     print("COMPUTER CHANCE :")
#     print("MOVE : ",MostEffMove)
#     return
# ####################################################################################################################################################
# def checkArrFill():
#     for j in range(1,10):
#         if GameBoard[j-1]==' ':
#             return False
#     return True
# ####################################################################################################################################################
# def MinMaxFunc(GameBoard,height,isMax):
#     if WinnerCheckerAI()==1:
#         return -2
#     elif WinnerCheckerAI()==2:
#         return 2
#     elif checkArrFill()==True:
#         return 0
    
#     if isMax:
#             GamePoints = -1000
#             for x in range(1,10):
#                 if GameBoard[x-1]==' ':
#                     GameBoard[x-1]='O'
#                     h=0
#                     pointInThisMove = MinMaxFunc(GameBoard,0,False)
#                     GameBoard[x-1]=' '
#                     if(pointInThisMove>GamePoints):
#                         GamePoints=pointInThisMove
#             return GamePoints
#     else:
#             GamePoints = 1000
#             for x in range(1,10):
#                 if GameBoard[x-1]==' ':
#                     GameBoard[x-1]='X'
#                     h=0
#                     pointInThisMove = MinMaxFunc(GameBoard,height+1,True)
#                     GameBoard[x-1]=' '
#                     if(pointInThisMove<GamePoints):
#                         GamePoints=pointInThisMove
#             return GamePoints
####################################################################################################################################################

####################################################################################################################################################
# computerAIvsHuman()
####################################################################################################################################################
#Our Main Program Starts from here
print(Fore.BLUE+"DO U WANT TO PLAY SINGLE OR MULTIPLAYER")
print(Fore.LIGHTGREEN_EX)
print("PRESS :  S FOR SINGLE PLAYER ")
print("         M FOR MULTI  PLAYER ")
print("         ANY OTHER Key FOR EXIT ")
print(Fore.LIGHTWHITE_EX)
variable1 = input("GAME TYPE : ")
#IF ELSE FOR SINGLE / MULTI / EXIT
if(variable1=="S"):
    AskDifficulty()
elif(variable1=="M"):
    print("OUR GAME BOARD IS ->")
    Blue_board()
    print()
    PlayMultiPlayer()
else:
    quit()
####################################################################################################################################################