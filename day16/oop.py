#oop

import turtle
import prettytable
# timmy = turtle.Turtle()

# timmy.shape("turtle")
# timmy.color("DarkOrchid3")
# timmy.forward(100)
# # print(my_screen.canvheight)

# my_screen=turtle.Screen()

# my_screen.exitonclick()

table = prettytable.PrettyTable()

table.add_column("pokeman name",["pikachu","squirtle","charmander"])
table.add_column("type",["electric","water","fire"])
table.align = "l"
print(table)