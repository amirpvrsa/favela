from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")


# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)

# for i in range(0,50):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
# #     timmy.pendown()

screen.colormode(255)
# for i in range(4,10):
#     timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
#     for n in range(i):
#         timmy.forward(25)
#         timmy.right(360/i)
        


def random_color():
    timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))


def random_direction():
    angle=[90,180,270,360]
    timmy.right(angle[random.randint(0,3)])
# timmy.pensize(10)
timmy.speed(15)
# for i in range(200):
#     random_color()
#     random_direction()
#     timmy.forward(40)
for i in range(36):
    timmy.circle(50)
    timmy.right(10)
    random_color()

screen.exitonclick()
