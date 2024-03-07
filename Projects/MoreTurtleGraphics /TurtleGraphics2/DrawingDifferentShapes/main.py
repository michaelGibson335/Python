#turtle graphics to draw multiple shapes within shapes
#also generate different colors for each loop of sides

import turtle as t
from turtle import Screen
import random 

tom = t.Turtle()
tom.shape('arrow')

colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']

num_sides = 5

#fun to create the sides
def drawShape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tom.forward(100)
        tom.right(angle)

#loop to run the fun create sides and generate random colors from color list 
for shapeSide in range(3, 11):
    tom.color(random.choice(colors))
    drawShape(shapeSide)

screen = Screen()
screen.exitonclick()


