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
time.sleep(10)
screen.clear()

#Display the background image
screen.bgpic("hercules.gif")
time.sleep(10)
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
    star.circle(3.6)
    star.end_fill()
    star.pendown()
#Repeat for the rest of the constell list
    for stars in constell:
        star.goto(stars)
        star.begin_fill()  
        star.circle(3.6)
        star.end_fill()

    star.penup()
    #myPen.goto(800,800)

hercules=[[52,253],[28,192],[9,127],[-79,94],[-189,105],[-142,233],[-189,105],[-79,94],
          [9,127],[29,9],[-29,0],[-79,94],[-29,0],[-72,-108],[-200,-24],[-230,-29],[-200,-24],
          [-72,-108],[-29,0],[29,9],[82,-151],[97,-169],[82,-151],[-58,-266]]
drawConstell(hercules)
time.sleep(10)
screen.clear()

#listing the important stars

drawConstell(hercules)
sty = ('Courier', 10, 'bold')
star.color('black')
star.penup()
star.goto(29,9)
star.dot()
star.write(" Zeta 2.81",align='left',font=sty)
star.goto(-72,-108)
star.dot()
star.write(" Sarin 3.14",align='left',font=sty)
star.goto(82,-151)
star.dot()
star.write(" Kornephoros 2.77",align='left',font=sty)
star.goto(-58,-266)
star.dot()
star.write("  Rasalgethi 3.48",align='left',font=sty)





























