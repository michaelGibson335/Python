#turtle graphics to draw random colored lines in random directions

import turtle as t
from turtle import Screen
import random 

tom = t.Turtle()
tom.shape('arrow')

#lists containing colors and directions for lines to go(north, south, west, east)
colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
directions = [0, 90, 180, 270]

#loop to generate lines with colors and directions pulled from list above
for i in range(200):
    tom.color(random.choice(colors))
    tom.pensize(10)
    tom.forward(30)
    tom.setheading(random.choice(directions))
    



screen = Screen()
screen.exitonclick()


