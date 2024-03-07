#turtle graphics to draw random colored lines in random directions

import turtle as t
from turtle import Screen
import random 

tom = t.Turtle()
tom.shape('arrow')
t.colormode(255)

#fun to generate random numbers for r, g, b 
def randomColors(): 
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomColors = (r, g, b)
    return randomColors

#lists containing colors and directions for lines to go(north, south, west, east)

directions = [0, 90, 180, 270]
tom.pensize(10)

#loop to generate lines with colors and directions pulled from list above
for i in range(200):
    tom.color(randomColors())
    tom.forward(30)
    tom.setheading(random.choice(directions))
    



screen = Screen()
screen.exitonclick()


