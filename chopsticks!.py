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
opponentshand=0 #same with above. can be 0,1,2,3
recentchoice=0
movenottomake = []
    #whole game related
move = 0 #steps you take to lose or win
level = "" #difficulty level. can be equal to three different strings
whoseturn= "" #used for big while loops. can be equal to two different strings
whowin="" #going to be used for demostratingh winning/losing screen
#---------------end of setting global variables-------------

#----------------------functions-------------------------

def waituntilclick(): #holds screen still click. return x coordinate and y coordinate
    return([x,y])

def hidehand(): #command.hide all four hands turtles
    return()

def showhand():#command.hide all four hands turtles
    return()

def handinposition():
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
    t.clearscreen()

def computerplay(): #big function contain other funcs.
    def easy(): #Changes own and opp hand. LAI
        global ownhand
        global valueonhand
        if valueonhand[0] == 0:
            ownhand = 1
        elif valuesonhand[1] == 2:
            ownhand = 0
        else:
            ownhand = random.randint(0,1)
        time.sleep(1)
        global opponents_hand
        if valueonhand[2] == 0:
            opponenthand = 3
        elif valueonhand[3] == 0:
            opponenthand = 2
        else:
            opponenthand = random.randint(2,3)

    def howtowincomputer(handvalue): #take in valueonhand,
        list = []         #return list of wining move[num for com hand, num pl hand]
        for player in range(2,4):
            for comp in range(0,2):
                if handvalue[player] + handvalue[comp] == 5:
                    list.append(int(comp))
                    list.append(int(player))
        return list

    def medium():
        global ownhand
        global opponentshand
        list = howtowincomputer(valueonhand)
        if howtowincomputer() != []:
            ownhand = list[0]
            #UI stuff
            opponentshand = list[1]
        else:
            easy()

    def movenottomake(handvalue): #reportor.take in valueonhand
        
        return list #list of move not to take
        

    

def gameover(list):#input valueonhand, return 0:no one or 1:com wins or 2:player wins JEAN
    if list[0] == 0 and list[1] == 0:
        return 2
    elif list[2] == 0 and list[3] == 0:
        return 1
    else:
        return 0

def finishturn(): #updating the valueonhand + the UI hands VEDI
    return ()

def playerplay(): #choosehand with textinput and change global own and opp hand. JEAN
    global ownhand
    global opponentshand
    while True:
        coice = input("Do you want to use your left 'l' or right 'r' hand? ")
        if coice == "l" or choice == "r":
            break
        if coice == "l":
            ownhand = 2
        else:
            ownhand = 3
    while True:
        coice = input("Do you want to increase the opponents 'l' or 'r' hand? (your perspective) ")
        if coice == "l" or choice == "r":
            break
        if choice == "l":
            opponentshand = 0
        else:
            opponentshand = 1

def finishgame(num): #command,input0/1/2 from gameover(),show w/l screen+print score in terminal/shell
    if num == 2: #should be place all the way done outside the while loop
        pass
    elif num == 1:
        pass
        #computer wins screen
        #print in terminal
        #ask to play again?
        #close the window

#-------------------end of functions---------------------

#----------------------------GAME-----------------------------------

beginguide()
handinposition()
while gameover(valueonhand) == False:
    while whoseturn == "c":
        computerplay()
        finishturn()
        whoseturn == "y"
    if not gameover(valueonhand) == 0:
        break
    while whoseturn == "y":
        playerplay()
        finishturn()
        whoseturn = "c"
    move += 1
    if not gameover(valueonhand) == 0:
        break
finishgame(gameover(valueonhand))

        

#-------------------------end of GAME----------------------------








    
