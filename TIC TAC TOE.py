# -*- coding: utf-8 -*-
import os
import random
import time
import keyboard


#  Display Game Title
def DisplayTitle():
    print("""
  _______ _____ _____   _______       _____   _______ ____  ______
 |__   __|_   _/ ____| |__   __|/\   / ____| |__   __/ __ \|  ____|
    | |    | || |         | |  /  \ | |         | | | |  | | |__
    | |    | || |         | | / /\ \| |         | | | |  | |  __|
    | |   _| || |____     | |/ ____ \ |____     | | | |__| | |____
    |_|  |_____\_____|    |_/_/    \_\_____|    |_|  \____/|______|

                                                                   """).center(75, " ")


#  Display Instructions Header
def Header():
    print("""
                        I N S T R U C T I O N S

                                  1|2|3
                                  -----
                                  4|5|6
                                  -----
                                  7|8|9

       pick a number from 1-9 to assign an 'X' or 'O' to an empty grid cell
                      |Players 1 & 2 are assigned randomly|
       |Player 1 will be assigined 'X'| & |Player 2 will be assigned 'O'|

""")


#  Display Grid Reference
def GameHeader():
    print("""

                                  1|2|3
                                  -----
                                  4|5|6
                                  -----
                                  7|8|9

            """)


#  Gets Name Input
def EnterPlayerNames():
    global n1, n2
    n1 = raw_input("ENTER NAME OF A PLAYER: ")
    print('\n')
    n2 = raw_input("ENTER NAME OF THE OTHER PLAYER: ")
    while n1 == n2 and n1 <> "":
        print("This name has been taken.")
        n2 = raw_input("ENTER NAME OF THE OTHER PLAYER: ")


# Chooses The  First Player At Player
def ChooseFirstPlayer():
    global n1, n2, p1, p2, name, sign, current
    gen_num = random.randint(0, 1)
    if gen_num == 0:
        p1 = n1, 'X'
        p2 = n2, 'O'
    else:
        p1 = n2, 'X'
        p2 = n1, 'O'
    current = p1
    print('\n')
    print(">>>" + "||" + p1[name].upper() + "||" + " HAS BEEN ASSIGNED TO PLAYER 1<<<").center(75, " ")
    print("<<<" + "||" + p2[name].upper() + "||" + " HAS BEEN ASSIGNED TO PLAYER 2>>>").center(75, " ")


#  Displays The Board
def PrintBoard():
    #  top section
    print("  " + " |" + "  " + " |" + " ").center(72, " ")
    print("   " + "|" + " " + "  |" + " ").center(72, " ")
    print(" " + Board[0] + " |" + " " + Board[1] + " |" + " " + Board[2]).center(72, " ")
    print("   " + "|" + " " + "  |" + " ").center(72, " ")

    #  grid separator
    print(" " + "---|---|---").center(72, " ")

    #  mid section
    print("   " + "|" + " " + "  |" + " ").center(72, " ")
    print(" " + Board[3] + " |" + " " + Board[4] + " |" + " " + Board[5]).center(72, " ")
    print("   " + "|" + " " + "  |" + " ").center(72, " ")

    #  grid separator
    print(" " + "---|---|---").center(72, " ")

    #  lower section
    print("  " + " |" + " " + "  |" + " ").center(72, " ")
    print(" " + Board[6] + " |" + " " + Board[7] + " |" + " " + Board[8]).center(72, " ")
    print("  " + " |" + " " + "  |" + " ").center(72, " ")


#  Current Player PLays A Turn
def PlayTurn():
    global Board, current, Ekey
    valid = False
    print('\n')

    # if statement for player is cpu or real...
    if current[0] <> "":

        GetInput()
        choice = Ekey

        try:
            choice = int(choice)
            while choice == 0 or choice > 9:
                print("NUMBER OUT OF RANGE!")
                # choice = raw_input("Choose another Number: ")
                GetInput()
                choice = Ekey
                choice = int(choice)

            while not valid:
                if Board[choice - 1] == " ":
                    Board[choice - 1] = current[sign]
                    valid = True

                elif Board[choice - 1] == current[sign]:
                    print("You already played this cell.")
                    print("Choose Another.")
                    # choice = raw_input("Choose another cell: ")
                    GetInput()
                    choice = Ekey
                    choice = int(choice)
                    if Board[choice - 1] == " ":
                        Board[choice - 1] = current[sign]
                        valid = True

                elif Board[choice - 1] <> current[sign] or Board[choice - 1] <> " ":
                    print("The other player occupies this cell.")
                    print("Choose Another.")
                    # choice = raw_input("Choose another cell: ")
                    GetInput()
                    choice = Ekey
                    choice = int(choice)
                    if Board[choice - 1] == " ":
                        Board[choice - 1] = current[sign]
                        valid = True

        except:
            print '\n'
            print "E N T E R    A    N U M B E R!".center(75, " ")
            print '\n'

    else:
        Cpumode()


# Swaps Current Player
def SwapPlayer():
    global p1, p2, current
    if current[sign] == p1[sign]:
        current = p2
    else:
        current = p1


# Checks For Win
def CheckforTic():
    global Board, p1, p2, winner, EndGame, count
    count = 9
    while not EndGame:

        if Board[0] == p1[sign] and Board[1] == p1[sign] and Board[2] == p1[sign]:
            EndGame = True
            winner = p1[name]
            break
        elif Board[3] == p1[sign] and Board[4] == p1[sign] and Board[5] == p1[sign]:
            EndGame = True
            winner = p1[name]
            break
        elif Board[6] == p1[sign] and Board[7] == p1[sign] and Board[8] == p1[sign]:
            EndGame = True
            winner = p1[name]
            break
        elif Board[0] == p1[sign] and Board[3] == p1[sign] and Board[6] == p1[sign]:
            EndGame = True
            winner = p1[name]
            break
        elif Board[1] == p1[sign] and Board[4] == p1[sign] and Board[7] == p1[sign]:
            EndGame = True
            winner = p1[name]
            break
        elif Board[2] == p1[sign] and Board[5] == p1[sign] and Board[8] == p1[sign]:
            EndGame = True
            winner = p1[name]
            break
        elif Board[0] == p1[sign] and Board[4] == p1[sign] and Board[8] == p1[sign]:
            EndGame = True
            winner = p1[name]
            break
        elif Board[2] == p1[sign] and Board[4] == p1[sign] and Board[6] == p1[sign]:
            EndGame = True
            winner = p1[name]
            break

        if Board[0] == p2[sign] and Board[1] == p2[sign] and Board[2] == p2[sign]:
            EndGame = True
            winner = p2[name]
            break
        elif Board[3] == p2[sign] and Board[4] == p2[sign] and Board[5] == p2[sign]:
            EndGame = True
            winner = p2[name]
            break
        elif Board[6] == p2[sign] and Board[7] == p2[sign] and Board[8] == p2[sign]:
            EndGame = True
            winner = p2[name]
            break
        elif Board[0] == p2[sign] and Board[3] == p2[sign] and Board[6] == p2[sign]:
            EndGame = True
            winner = p2[name]
            break
        elif Board[1] == p2[sign] and Board[4] == p2[sign] and Board[7] == p2[sign]:
            EndGame = True
            winner = p2[name]
            break
        elif Board[2] == p2[sign] and Board[5] == p2[sign] and Board[8] == p2[sign]:
            EndGame = True
            winner = p2[name]
            break
        elif Board[0] == p2[sign] and Board[4] == p2[sign] and Board[8] == p2[sign]:
            EndGame = True
            winner = p2[name]
            break
        elif Board[2] == p2[sign] and Board[4] == p2[sign] and Board[6] == p2[sign]:
            EndGame = True
            winner = p2[name]
            break

        # Checks For Empty Cells
        for j in range(9):
            if Board[j] <> " ":
                count -= 1

            # Checks For Draw
            if count == 0:
                EndGame = True
                winner = "Draw"
                break

        break


# Displays Game Results
def OutputResults():
    global winner, n1count, n2count, n1, n2

    print '\n'
    if winner <> "Draw":
        if winner == n1:
            n1count += 1
            print (winner + " IS THE    W I N N E R!!!").center(75, " ")
            print '\n'
            print(n1 + " HAS WON " + str(n1count) + " Game(s)!").center(75, " ")
            print(n2 + " HAS WON " + str(n2count) + " Game(s)!").center(75, " ")

        elif winner == n2:
            n2count += 1
            print (winner + " IS THE    W I N N E R!!!").center(75, " ")
            print '\n'
            print(n1 + " HAS WON " + str(n1count) + " Game(s)!").center(75, " ")
            print(n2 + " HAS WON " + str(n2count) + " Game(s)!").center(75, " ")

    else:
        print (winner + "!!!").center(75, " ")
        print(n1 + " HAS WON " + str(n1count) + " Game(s)!").center(75, " ")
        print(n2 + " HAS WON " + str(n2count) + " Game(s)!").center(75, " ")


# Resets The Board
def InitBoard():
    global Board
    Board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


#   Changes The First Player To Second Player
def SwitchFirstPlayer():
    global p1, p2, current
    temp = p1
    p1 = p2
    p2 = temp
    print('\n')
    print(">>>" + "||" + p1[name].upper() + "||" + " HAS BEEN ASSIGNED TO PLAYER 1<<<").center(75, " ")
    print("<<<" + "||" + p2[name].upper() + "||" + " HAS BEEN ASSIGNED TO PLAYER 2>>>").center(75, " ")
    current = p1


def Cpumode():
    global loopcount, move
    cmove = 20
    moved = False
    if moved == False:
        while Board[move] <> " ":
            move = random.randint(0,8)
        moved = True

    playpick = random.randint(0,1)
    while True:
        if loopcount < 1:
            if playpick == 0:
                if Board[4] == " ":
                    move = 4
                else:
                    if loopcount <> 2:
                        randomposition = random.randrange(0, 9, 2)
                        while randomposition == 4 or Board[randomposition] <> " ":
                            randomposition = random.randrange(0, 9, 2)
                        move = randomposition
                        loopcount += 1
            else:
                if loopcount <> 2:
                    randomposition = random.randrange(0, 9, 2)
                    while randomposition == 4 or Board[randomposition] <> " ":
                        randomposition = random.randrange(0, 9, 2)
                    move = randomposition
                    loopcount += 1
        elif loopcount <> 2:
            randomposition = random.randrange(0, 9, 2)
            while randomposition == 4 or Board[randomposition] <> " ":
                randomposition = random.randrange(0, 9, 2)
            move = randomposition
            loopcount += 1

        #  play possible wins
        for x,y,z in possiblewins:
            if Board[x] == current[1] and Board[y] == current[1] and Board[z] == " ":
                move = z
                break
            elif Board[x] == current[1] and Board[y] == " " and Board[z] == current[1]:
                move = y
                break
            elif Board[x] == " " and Board[y] == current[1] and Board[z] == current[1]:
                move = x
                break

        #check for possible player win
        for x,y,z in possiblewins:
            if Board[x] == " " and Board[y] <> " " and Board[z] <> " ":
                if Board[x] == " " and Board[y] <> current[1] and Board[z] <> current[1]:
                    cmove = x
                    break
            elif Board[x] <> " " and Board[y] == " " and Board[z] <> " ":
                if Board[x] <> current[1] and Board[y] == " " and Board[z] <> current[1]:
                    cmove = y
                    break
            elif Board[x] <> " " and Board[y] <> " " and Board[z] == " ":
                if Board[x] <> current[1] and Board[y] <> current[1] and Board[z] == " ":
                    cmove = z
                    break

        #Decide on whether to play defensive or offensive
        for x,y,z in possiblewins:

            if (
            (Board[x] == " " and Board[y] == current[1] and Board[z] == current[1]) or
            (Board[x] == current[1] and Board[y] == " " and Board[z] == current[1]) or
            (Board[x] == current[1] and Board[y] == current[1] and Board[z] == " ")
                ):
                Board[move] = current[1]
                break

            else:

                if cmove < 10:
                    Board[cmove] = current[1]
                    break
                else:
                    Board[move] = current[1]
                    break
        # Ends player AI turn
        break


#  Gets Input From Player
def GetInput():
    global Ekey, Key
    Keypress = True
    while Keypress:
        Ekey = ""
        Ekey = keyboard.read_key(suppress=False)
        Key = ""
        Key = keyboard.read_event(suppress=False)

        if Key <> 'KeyboardEvent(' + str(Ekey) + ' down)':
            Ekey = str(Ekey)
            Keypress = False


# Start Of Code Execution
PlayAgain = ""
NewGame = True
Ekey = ""
Key = ""
possiblewins = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6] ]

while NewGame:

    Board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    #   Name Variables for Players
    n1 = ""
    n2 = ""

    #   Arrays To Store Player Names and Signs [X / O]
    p1 = []
    p2 = []

    #   Variables To Store The Players' Wins
    # noinspection PyRedeclaration
    n1count = 0
    # noinspection PyRedeclaration
    n2count = 0

    #   Index values for names and signs
    name = 0
    sign = 1

    #   Current Player Variable
    current = []

    winner = ""
    ContinueGame = True
    # noinspection PyRedeclaration
    EndGame = False

    #   Variable To Count Number OF Empty Cells Left
    count = 0

    #indicates whether first random move has been played by AI if middle cell had been played.
    loopcount = 0
    move = random.randint(1,8)

    DisplayTitle()
    time.sleep(3)
    os.system("cls")
    Header()
    os.system("pause")
    os.system("cls")
    EnterPlayerNames()
    ChooseFirstPlayer()
    time.sleep(3)
    os.system('cls')

    while ContinueGame:
        GameHeader()
        PrintBoard()
        while not EndGame:
            PlayTurn()
            SwapPlayer()
            os.system("cls")
            GameHeader()
            PrintBoard()
            CheckforTic()
        OutputResults()

        #   Players Choose Between Reset The Game or Continuing
        print '\n'
        print("Press [P] To PLAY AGAIN **OR** [N] To Start A NEW GAME")
        PlayAgain = raw_input()
        PlayAgain = str(PlayAgain)
        while PlayAgain.lower() <> 'p' and PlayAgain.lower() <> 'n':
            print("Press [P] To PLAY AGAIN **OR** [N] To Start A NEW GAME")
            PlayAgain = str(raw_input())

        if PlayAgain.upper() == "P":
            EndGame = False
            InitBoard()
            SwitchFirstPlayer()
            os.system('cls')
            time.sleep(.25)
        else:
            ContinueGame = False
            EndGame = True
            n1count = 0
            n2count = 0
            os.system('cls')
