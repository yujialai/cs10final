import turtle as t
import random
import time

t.setup(width=480, height=360, startx=400, starty=50)

#initializing the sprites and numbers
clhand = t.Turtle()
crhand = t.Turtle()
prhand = t.Turtle()
plhand = t.Turtle()
clhand.speed(0)
crhand.speed(0)
plhand.speed(0)
prhand.speed(0)
pl1 = "1Pl.gif"
pr1 = "1Pr.gif"
cl1 = "1Cl.gif"
cr1 = "1Cr.gif"
pl2 = "2Pl.gif"
pr2 = "2Pr.gif"
cl2 = "2Cl.gif"
cr2 = "2Cr.gif"
pl3 = "3Pl.gif"
pr3 = "3Pr.gif"
cl3 = "3Cl.gif"
cr3 = "3Cr.gif"
pl4 = "4Pl.gif"
pr4 = "4Pr.gif"
cl4 = "4Cl.gif"
cr4 = "4Cr.gif"
pl5 = "5Pl.gif"
pr5 = "5Pr.gif"
cl5 = "5Cl.gif"
cr5 = "5Cr.gif"
handoutshape = "handoutshape.gif"
Shapes_to_register = [pl1, pl2, pl3, pl4, pl5, pr1, pr2, pr3, pr4, pr5, cl1, cl2, cl3, cl4, cl5, cr1, cr2, cr3, cr4, cr5, handoutshape]
for items in Shapes_to_register:
    t.register_shape(items)

#---------------setting gloabal variables-------------------
    #hands related
valueonhand = [1, 1, 1, 1]#list contain finger numbers for each hands
    #use when play
ownhand=0 #used in each turn choosing hands and adding hands. can be 0,1,2,3
opponenthand=0 #same with above. can be 0,1,2,3
movenottomake = []
    #whole game related
move = 0 #steps you take to lose or win
level = "" #difficulty level. can be equal to three different strings
whoseturn= "" #used for big while loops. can be equal to two different strings
whowin="" #going to be used for demostratingh winning/losing screen
#---------------end of setting global variables-------------

#----------------------functions-------------------------



def handinposition():
    valueonhand = [1, 1, 1, 1]
    clhand.penup()
    crhand.penup()
    prhand.penup()
    plhand.penup()
    clhand.setposition(-120,80)
    crhand.setposition(120,80)
    plhand.setposition(-120,-80)
    prhand.setposition(120,-80)
    clhand.shape(cl1)
    crhand.shape(cr1)
    plhand.shape(pl1)
    prhand.shape(pr1)
    
def beginguide(): #command.logo+instructions+level, ends with clear bg
    global level
    global whoseturn
    t.bgpic("logo.gif")
    input("Chopsticks - Press enter to start")
    t.bgpic("instructions.gif") #instructions screen
    input("Instructions - Press enter to continue")
    t.bgpic("levels.gif")
    while True:
        level = str(input("What level do you wanna play? Type 'h' for hard, 'm' for medium and 'e' for easy: "))
        if level == "h" or level =="m" or level == "e":
            break
    t.bgpic(level+".gif")
    while True:
        begin = input("Who should sart? Computer 'c', you 'y' or flip a coin 'f'")
        if begin == "c" or begin == "y" or begin == "f":
            break
    if begin == "c":
        whoseturn = "c"
    elif begin == "y":
        whoseturn = "y"
    else:
        t.bgpic("flipcoin.gif")
        if random.randint(0,1) == 1:
             print("You start!")
             whoseturn = "y"
        else:
            print("Computer starts!")
            whoseturn = "c"
        time.sleep(1)
    t.clearscreen()

def computerplay(): #big function contain other funcs.
    def easy(): #Changes own and opp hand. LAI
        global ownhand
        global valueonhand
        global opponenthand
        if valueonhand[0] == 5:
            ownhand = 1
        elif valueonhand[1] == 5:
            ownhand = 0
        else:
            ownhand = random.randint(0,1)
        time.sleep(1)
        if valueonhand[2] == 5:
            opponenthand = 3
        elif valueonhand[3] == 5:
            opponenthand = 2
        else:
            opponenthand = random.randint(2,3)

    def howtowincomputer(handvalue): #take in valueonhand,
        list = []         #return list of wining move[num for com hand, num pl hand]
        for player in range(2,3):
            for comp in range(0,1):
                if handvalue[player] + handvalue[comp] == 5:
                    list.append(int(comp))
                    list.append(int(player))
        return list

    def medium():
        global ownhand
        global opponenthand
        list = howtowincomputer(valueonhand)
        if howtowincomputer() != []:
            ownhand = list[0]
            #UI stuff
            opponenthand = list[1]
        else:
            easy()

    def movenottomake(handvalue): #reportor.take in valueonhand
        global movenottomake
        resultsofpossiblemoves = []
        playershand = []
        result = []
        for comp in range(0,2):
            for player in range(2,4):
                if handvalue[player] + handvalue[comp] > 5:
                    resultsofpossiblemoves.append(handvalue[player] + handvalue[comp] -5)
                else:
                    resultsofpossiblemoves.append(handvalue[player] + handvalue[comp])   
        for player in range(0,2):
            playershand.append(handvalue[player])
        for player in range(0,2):
            for possibilities in range(0,4):
                if playershand[player] + resultsofpossiblemoves[possibilities] == 5:
                    if not result.contains(possibilities):
                        result.append(possibilities)
        movenottomake = result

        
    def rhandavformove(num): #take in num rep. move to take, can be 1234
        global valueonhand #boolean.are hands available for move?
        if num==1:
            if valueonhand[0]==0 or valueonhand[2]==0:
                return False
            else:
                return True
        else:
            if num==2:
                if valueonhand[0]==0 or valueonhand[3]==0:
                    return False
                else:
                    return True
            else:
                if num==3:
                    if valueonhand[1]==0 or valueonhand[2]==0:
                        return False
                    else:
                        return True
                else:
                    if num==4:
                        if valueonhand[1]==0 or valueonhand[3]==0:
                            return False
                        else:
                            return True
    def domove (move):
        global ownhand
        global opponenthand
        if move == 1:
            ownhand = 0
            opponenthand = 2
        elif move == 2:
            ownhand = 0
            opponenthand = 3
        elif move == 3:
            ownhand = 1
            opponenthand = 2
        elif move == 4:
            ownhand = 1
            opponenthand = 3


    def medium():
        global ownhand
        global opponenthand
        list = howtowincomputer()
        if howtowincomputer() != []:
            ownhand = list[0]
            #UI stuff
            opponenthand = list[1]
        else:
            easy()    

    def hard():
        global movenottomake
        global ownhand
        global opponenthand
        movenottomake()
        a = 0
        finish = False
        if not howtowincomputer() == []:
            ownhand = howtowincomputer()[0]
            #UI stuff
            opponenthand = howtowincomputer()[1]
        elif len(movenottomake) == 4:
            easy()
        else:
            while finish == False :
                a = random.randint(1,4)
                while a in movenottomake:
                    a = random.randint(1,4)
                if rhandavformove(a) == True:
                    domove(a)
                    finish = True
                    # the finish variable stops the while block
                else:
                    movesnottomake.append(a)
                    if len(movesnottomake) == 4:
                        easy()
                        finish = True
    if level=="e":
        easy()
    elif level=="m":
        medium()
    else:
        hard()
    

def gameover(list):#input valueonhand, return 0:no one or 1:com wins or 2:player wins JEAN
    if list[0] == 0 and list[1] == 0:
        return 2
    elif list[2] == 0 and list[3] == 0:
        return 1
    else:
        return 0


def finishturn(): #updating the valueonhand + the UI hands VEDI
    global valueonhand
    global opponenthand
    global ownhand
    def updatenumbers():
        global valueonhand
        global opponenthand
        global ownhand
        valueonhand[opponenthand] = valueonhand[opponenthand] + valueonhand[ownhand]
        while valueonhand[opponenthand] > 5:
            valueonhand[opponenthand] -= 5
    def updatehands(): 
        global valueonhand
        clhand.shape(eval("cl"+str(valueonhand[0])))
        crhand.shape(eval("cr"+str(valueonhand[1])))
        plhand.shape(eval("pl"+str(valueonhand[2])))
        prhand.shape(eval("pr"+str(valueonhand[3])))
    updatenumbers()
    updatehands()

    

def playerplay(): #choosehand with textinput and change global own and opp hand. JEAN
    global ownhand
    global opponenthand
    global valueonhand
    while True:
        choice = input("Do you want to use your left 'l' or right 'r' hand? ")
        if choice == "l" or choice == "r":
            if choice == "l" and valueonhand[2] != 5:
                ownhand = 2
                break
            elif choice == "r" and valueonhand[3] != 5:
                ownhand = 3
                break
    while True:
        choice = input("Do you want to increase the opponents 'l' or 'r' hand (your perspective)? ")
        if choice == "l" or choice == "r":
            if choice == "l" and valueonhand[0] != 5:
                opponenthand = 0
                break
            elif choice == "r" and valueonhand[1] != 5:
                ownhand = 1
                break

def losingscreen():
    t.bgpic("looserscreen.gif")
    time.sleep(.2)
    t.bgpic("looserscreen2.gif")
    time.sleep(.2)
    t.bgpic("looserscreen3.gif")
    time.sleep(.2)
    t.bgpic("looserscreen4.gif")
            
def winningscreen():
    t.bgpic("winningscreen.gif")
    time.sleep(.2)
    t.bgpic("winningscreen2.gif")
    time.sleep(.2)
    t.bgpic("winningscreen3.gif")


def finishgame(num): #command,input0/1/2 from gameover(),show w/l screen+print score in terminal/shell
    global game
    if num == 2: #should be place all the way done outside the while loop
        # winningscreen():
        t.bgpic("winnerscreen.gif")
        print("It took you " + str(move) + " to win. Good job!")
        choice = input("You wanna play again? Type 'Yes'!")
        if choice == 'Yes':
            game = True
        else:
            game = False
    elif num == 1:
        # losingscreen():
        print("You lost after " + str(move) + " moves. Too bad!")
        choice = input("You wanna play again? Type 'Yes'!")
        if choice == 'Yes':
            game = True
        else:
            game = False
        #computer wins screen
        #print in terminal
        #ask to play again?
        #close the window

#-------------------end of functions---------------------

#----------------------------GAME-----------------------------------


beginguide()
game = True
while game == True:
    handinposition()
    while gameover(valueonhand) == False:
        if whoseturn == "c": #to make sure the hands are not updated before a move
            print("entering computer")
            while whoseturn == "c":
                print("computer while loop")
                computerplay()
                whoseturn == "y"
            print("finishing computer")
            finishturn()
        if not gameover(valueonhand) == 0:
            break
        print("entering player")
        while whoseturn == "y":
            print("player while loop")
            playerplay()
            whoseturn = "c"
        print("finishing player")
        finishturn()
        move += 1
        if not gameover(valueonhand) == 0:
            break
    finishgame(gameover(valueonhand))
t.bye()
        

#-------------------------end of GAME----------------------------








    
