#import turtle graphic from turtle module and screen draw class
from turtle import Turtle, Screen

#draw a square with the turtle class and methods
tomTurtle = Turtle()
tomTurtle.shape('turtle')
tomTurtle.color('red', 'green')

for i in range(4):
    tomTurtle.forward(100)
    tomTurtle.left(90)
    









screen = Screen()
screen.exitonclick()