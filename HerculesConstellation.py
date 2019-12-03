import turtle
import time

#printed the text and used sleep() to pause for 30 seconds , then screen.clear() executes
star=turtle.Turtle()
screen = turtle.Screen()

#To make the turtle run in full screen
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

star.hideturtle()
star.pencolor("white")
screen.bgcolor("grey")
star.penup()
style = ("courier",30)
star.write("Midterm Project",font=style,align='center')
star.goto(-7,-42)
star.write("Hercules Constellation",True,font=style,align='center')
star.goto(-37,-85)
star.write("Srikar Reddy",True,font=style,align='center')
star.pendown()
star.hideturtle()
time.sleep(7.5)
screen.clear()

#Display the background image
screen.bgpic("hercules.gif")
time.sleep(7.5)
screen.clear()

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

hercules=[[52,253],[28,192],[9,127],[-79,94],[-189,105],[-142,233],[-189,105],[-79,94],
          [9,127],[29,9],[-29,0],[-79,94],[-29,0],[-72,-108],[-200,-24],[-230,-29],[-200,-24],
          [-72,-108],[-29,0],[29,9],[82,-151],[97,-169],[82,-151],[-58,-266]]
drawConstell(hercules)
time.sleep(7.5)

#listing the important stars




























