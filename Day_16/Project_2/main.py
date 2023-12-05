# from turtle import Turtle, Screen

# immy = Turtle()
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape('turtle')
# timmy.color('blue')
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ['Pikachu', "Squirtle", "Charmander"], align='l')
table.add_column("Type", ["Electric", "Water", "Fire"], align='l')
print(table)

