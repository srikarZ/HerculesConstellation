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
time.sleep(30)
screen.clear()

#Displayed image
screen.bgpic("hercules.png")
time.sleep(30)




