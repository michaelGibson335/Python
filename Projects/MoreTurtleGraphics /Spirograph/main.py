#turtle graphics to draw multiple circles in repeated motion to create a spirograph

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
    color = (r, g, b)
    return color

tom.speed('fastest')

#loop to create circles and find existing position and shift over by exising size of gap
def drawSpirograph(sizeOfGap):
    for i in range(int(360 / sizeOfGap)):
        tom.color(randomColors())
        tom.circle(100)
        tom.setheading(tom.heading() + sizeOfGap)

drawSpirograph(random.randint(2, 20))



    



screen = Screen()
screen.exitonclick()


