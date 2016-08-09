import turtle as t
import random
import time

t.setup(width=480, height=360, startx=50, starty=50)

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
ownhand = "" 
opponentshand = "" 
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
    
    

#-------------------end of functions---------------------

#----------------------------GAME-----------------------------------


#-------------------------end of GAME----------------------------








    
