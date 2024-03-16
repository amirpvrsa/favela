from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(550, 500)
user_bet = screen.textinput(title = "make your bet.",prompt= "which turtle will win ?")
#print(user_bet)



all_turtles=[]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
i=0
for index in range(6):
    col = Turtle()
    col.penup()
    col.shape("turtle")
    col.color(colors[index])
    col.goto(x = -220, y = -190+(i*60))
    all_turtles.append(col)
    i+=1
finish = True

while finish:
    for i in all_turtles:
        i.forward(random.randint(0,10))
        if i.xcor()>245:
            finish=False
            winner=i
if user_bet == winner.color()[0]:
    print("you win!!!")
else:
    print(f"you lost, winner is {winner.color()[0]} turtle")



screen.exitonclick()