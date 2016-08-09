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
    input("Chopsticks - Press any key to start")
    t.bgpic("instructions.gif") #instructions screen
    input("Instructions - Press any key to continue")
    t.bgpic("levels.gif")
    while True:
        level = str(input("What level do you wanna play? Type 'h' for hard, 'm' for medium and 'e' for easy: "))
        if level == "h" or level =="m" or level == "e":
            break
    t.bgpic(level+".gif")
    t.clearscreen()

def computerplay(): #big function contain other funcs. return???not sure yet
    return()

def gameover(list):#input valueonhand, return true or false
    return()
    
#-------------------end of functions---------------------

#----------------------------GAME-----------------------------------

beginguide()
handinposition()
while gameover(valueonhand) == False:
    while whoseturn == "c":
        computerplay()
        whoseturn == "y"
    if not gameover(valueonhand) == 0:
        break
    while whoseturn == "y":
        pass
        

#-------------------------end of GAME----------------------------








    
