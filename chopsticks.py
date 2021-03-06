#We are using the turtle library for graphics, the random to generate random moves and time to delay the computers move.
import turtle as t
import random
import time

#Sets up the window.
t.setup(width=480, height=360, startx=400, starty=50)

#Initializing the turtles(stand for hands with shapes) and numbers on hands(you always start with ones)
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
for items in Shapes_to_register: #using for loop to register so we don't have to ty
    t.register_shape(items)

#---------------setting gloabal variables-------------------
    #hands related#
valueonhand = [1, 1, 1, 1]#list contain finger numbers for each hands
    #use when play#
ownhand=0 #used in each turn choosing hands and adding hands. can be 0,1,2,3
opponenthand=0 #same with above. can be 0,1,2,3
movenottomake = [] #list used in hard mode, results of predictions for if taking a move can potntially cause the computer to lose in the next round
handlist = [[clhand, crhand, plhand, prhand], ["cl", "cr", "pl", "pr"]]
    #whole game related#
move = 0 #steps you take to lose or win
level = "" #difficulty level. can be equal to three different strings
whoseturn= "" #used for big while loops. can be equal to two different strings
whowin="" #going to be used for demostratingh winning/losing screen
#---------------end of setting global variables-------------

#----------------------functions-------------------------
def handinposition(): #set turtles into "hands" and set them to the right positions
	global move
	global valueonhand
	valueonhand = [1, 1, 1, 1]
	clhand.penup()
	crhand.penup()
	prhand.penup()
	plhand.penup()
	clhand.setposition(-120,80)
	crhand.setposition(120,80)
	plhand.setposition(-120,-80)
	prhand.setposition(120,-80)
	clhand.showturtle()
	crhand.showturtle()
	plhand.showturtle()
	prhand.showturtle()
	clhand.shape(cl1)
	crhand.shape(cr1)
	plhand.shape(pl1)
	prhand.shape(pr1)
	move = 0

def beginguide(): #command.logo+instructions+level, ends with clear background
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
        begin = input("Who should start? Computer 'c', you 'y' or flip a coin 'f'")
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
    t.bgpic("clearscreen.gif")


def easy(): #Changes own and opponent's hands randomly, computer has no skills in this mode exept not picking a hand that is already out.
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

def howtowincomputer(handvalue): #take in valueonhand(),
    liste = []  #return list of moves that will make the computer win in this round[num for com hand, num pl hand]
    for player in range(2,4):
        for comp in range(0,2):
            if handvalue[player] + handvalue[comp] == 5:
                liste.append(int(comp))
                liste.append(int(player))
    return liste

def createmovenottomake(handvalue): #reporter.take in valueonhand(global list of numbers on four hands)
    global movenottomake #generate a list of moves that can cause the computer to lose in the next round
    resultsofpossiblemoves = []#list of values of player's hands possible values, and then we use this to test if the player can use those numbers to win.
    computerhand = []
    result = []
    for comp in range(0,2):
        for player in range(2,4):
            if handvalue[player] + handvalue[comp] > 5:
                resultsofpossiblemoves.append(handvalue[player] + handvalue[comp] -5)
            else:
                resultsofpossiblemoves.append(handvalue[player] + handvalue[comp])   
    for comp in range(0,2):
        computerhand.append(handvalue[comp])
    for possibilities in range(0,4):
        for comp in range(0,2):
            if computerhand[comp] + resultsofpossiblemoves[possibilities] == 5:
                if not possibilities+1 in result:
                    result.append(possibilities+1)
    movenottomake = result


        
def rhandavformove(num): #take in a number represents move to take, can be 1234
    global valueonhand #boolean."are hands available for move?"
    if num==1:
        if valueonhand[0]==5 or valueonhand[2]==5:
            return False
        else:
            return True
    else:
        if num==2:
            if valueonhand[0]==5 or valueonhand[3]==5:
                return False
            else:
                return True
        else:
            if num==3:
                if valueonhand[1]==5 or valueonhand[2]==5:
                    return False
                else:
                    return True
            else:
                if num==4:
                    if valueonhand[1]==5 or valueonhand[3]==5:
                        return False
                    else:
                        return True

def domove (move): #sets ownhand and opponenthand
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

def medium(): #computer has a new skill of seeing the moves that can make him win
    global ownhand
    global opponenthand
    global valueonhand
    listtowin = howtowincomputer(valueonhand)
    if listtowin != []:
        ownhand = listtowin[0]
        opponenthand = listtowin[1]
    else:
        easy()#if computer doesn't see moves for him to win in this round, he picks a random move just like in easy mode

def hard(): #on top of medium, computer now can predict whether a move can give the player a chance to win in the next round. and he won't do that move
    global movenottomake
    global ownhand
    global opponenthand
    global valueonhand
    createmovenottomake(valueonhand)
    a = 0
    finish = False
    listtowin = howtowincomputer(valueonhand)
    if listtowin !=[]:
        ownhand = listtowin[0]
        #UI stuff
        opponenthand = listtowin[1]
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
                movenottomake.append(a)
                if len(movenottomake) == 4:
                    easy()
                    finish = True

def computerplay(): #HOF contains other funcs. ABSTRACTION! SO CLEAN AND READABLE
    global ownhand
    global valueonhand
    global opponenthand
    if level=="e":
        easy()
    elif level=="m":
        medium()
    else:
        hard()
    

def gameover(list):#input valueonhand, return 0:no one or 1:com wins or 2:player wins JEAN
    if list[0] == 5 and list[1] == 5:
        return 2
    elif list[2] == 5 and list[3] == 5:
        return 1
    else:
        return 0


def finishturn(): #updating the valueonhand, also display handout is hand reaches 5
    global valueonhand
    global opponenthand
    global ownhand
    global handlist
    def updatenumbers():
        global valueonhand
        global opponenthand
        global ownhand
        global handlist
        valueonhand[opponenthand] = valueonhand[opponenthand] + valueonhand[ownhand]
        while valueonhand[opponenthand] > 5:
            valueonhand[opponenthand] -= 5
        if valueonhand[opponenthand] == 5:
            handlist[0][opponenthand].shape(eval(handlist[1][opponenthand]+"5"))
    def updatehands(): 
        global valueonhand
        if valueonhand[0] == 5:
            clhand.shape(handoutshape)
        else:
            clhand.shape(eval("cl"+str(valueonhand[0])))
        if valueonhand[1] == 5:
            crhand.shape(handoutshape)
        else:
            crhand.shape(eval("cr"+str(valueonhand[1])))
        if valueonhand[2] == 5:
            plhand.shape(handoutshape)
        else:
            plhand.shape(eval("pl"+str(valueonhand[2])))
        if valueonhand[3] == 5:
            prhand.shape(handoutshape)
        else:
            prhand.shape(eval("pr"+str(valueonhand[3])))
    updatenumbers()
    updatehands()

    

def playerplay(): #let the player choose which hand to use as augent, and which opponet's hand to use as addent
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
        choice = input("Do you want to increase the opponents 'l' or 'r' hand? (your perspective) ")
        if choice == "l" or choice == "r":
            if choice == "l" and valueonhand[0] != 5:
                opponenthand = 0
                break
            elif choice == "r" and valueonhand[1] != 5:
                opponenthand = 1
                break
        

def s():
    t.bgpic("looserscreen.gif")
def s1():
    t.bgpic("looserscreen2.gif")
def s2():
    t.bgpic("looserscreen3.gif")
def s3():
    t.bgpic("looserscreen4.gif")


def losingscreen(): #animation
    s()
    t.ontimer(s1, 100)
    t.ontimer(s2, 200)
    t.ontimer(s3, 300)
    t.ontimer(s, 400)
    t.ontimer(s1, 500)
    t.ontimer(s2, 600)
    t.ontimer(s3, 700)
    t.ontimer(s, 800)
            

def w():
    t.bgpic("winnerscreen.gif")
def w2():
    t.bgpic("winnerscreen2.gif")
def w3():
    t.bgpic("winnerscreen3.gif")

def winningscreen(): #animation
    w()
    t.ontimer(w2, 200)
    t.ontimer(w3, 400)
    t.ontimer(w, 600)
    t.ontimer(w2, 800)
    t.ontimer(w3, 1000)
    t.ontimer(w, 1200)

def hideturtle():
	clhand.hideturtle()
	crhand.hideturtle()
	plhand.hideturtle()
	prhand.hideturtle()

def finishgame(num): #after game, display win/lose screen and ask if want to play again
    global game
    global valueonhand
    if num == 2:
        hideturtle()
        winningscreen()
        print("It took you " + str(move) + " to win. Good job!")
        choice = input("You wanna play again? Type 'Yes'!")
        if choice == 'Yes':
            game = True
        else:
            game = False
    elif num == 1:
        hideturtle()
        losingscreen()
        print("You lost after " + str(move) + " moves. Too bad!")
        choice = input("You wanna play again? Type 'Yes'!")
        print(choice)
        if choice == 'Yes':
            game = True
            valueonhand = [1, 1, 1, 1]
        else:
            game = False
#-------------------end of functions---------------------

#----------------------------GAME-----------------------------------
#this is the actual game play. with abstraction, it appears to be simple and human-read-friendly
game = True
while game == True:
	beginguide()
	handinposition()
	while gameover(valueonhand) == 0:
		if whoseturn == "c":
			time.sleep(2)#so the player have time to understand computer's move
			computerplay()
			finishturn()
			whoseturn = "y"
		if not gameover(valueonhand) == 0:
			break
		while whoseturn == "y":
			playerplay()
			whoseturn = "c"
		finishturn()
		move += 1
	finishgame(gameover(valueonhand))
t.bye()
#-------------------------end of GAME----------------------------









    
