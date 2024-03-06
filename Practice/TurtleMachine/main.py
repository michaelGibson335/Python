# # #import anotherModule


# # #print(anotherModule.another_variable)

# # #test import Turtle class from turtle module and making objects
# # #testing various methods to change shape and color 
# # from turtle import Turtle, Screen
# # timmy = Turtle()
# # print(timmy)
# # timmy.shape("turtle")
# # timmy.color('red')
# # timmy.forward(100)

# #more object testing
# #testing canvas screen with a turtle graphics
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

#test pretty table
from prettytable import PrettyTable 

table = PrettyTable()
table.add_column("Pokemon Name", ["Bulbasaur", "Squirtle", "Charmander"])
table.add_column("Type",["Grass/Poison", "Water", "Fire"])
table.align = 'l'
print(table)

