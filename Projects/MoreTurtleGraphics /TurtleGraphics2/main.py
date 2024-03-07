#this program creates a turtle icon and makes it skip 15 times
#along a dotted line

from turtle import Turtle, Screen

tomTurtle = Turtle()
tomTurtle.shape('turtle')
tomTurtle.color('coral')

#loop to skip the turtle icon 15 times along a dotted line
for i in range(15):
    tomTurtle.forward(10)
    tomTurtle.penup()
    tomTurtle.forward(10)
    tomTurtle.pendown()

screen = Screen()
screen.exitonclick()

