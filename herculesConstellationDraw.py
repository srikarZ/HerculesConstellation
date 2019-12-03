import turtle
import time

screen=turtle.Screen()

#Displaying circles at vertices for hercules constellation
screen.bgpic("stars.gif")
def drawConstell(constell):
#The starting point of the constellation
    star=turtle.Turtle()
    star.speed(0)
    star.penup()
    star.goto(constell[0])
    star.begin_fill()  
    star.circle(2)
    star.end_fill()
    star.pendown()
#Repeat for the rest of the constell list
    for stars in constell:
        star.goto(stars)
        star.begin_fill()  
        star.circle(2)
        star.end_fill()

    star.penup()
    #myPen.goto(800,800)

hercules=[[90,255],[87,234],[85,211],[46,186],[-20,205],[-3,255]]
drawConstell(hercules)
