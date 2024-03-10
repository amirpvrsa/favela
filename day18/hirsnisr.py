from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
screen = Screen()
screen.setworldcoordinates(-350,-350,350,350)

# timmy.shape("turtle")
screen.colormode(255)
# def random_color():
#     timmy.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))


# def random_direction():
#     angle=[90,180,270,360]
#     timmy.right(angle[random.randint(0,3)])
    
# colors = colorgram.extract('image.jpg',100)
# rgb_colors=[]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_collor = (r,g,b)
#     rgb_colors.append(new_collor)
# print(rgb_colors)
color_list = [(249, 248, 244), (250, 245, 248), (243, 250, 246), (236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34), (11, 97, 52), (169, 181, 232), (241, 169, 155), (252, 7, 40), (10, 84, 100), (63, 98, 8), (14, 51, 250), (250, 11, 8),(249, 248, 244), (250, 245, 248), (243, 250, 246), (236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34), (11, 97, 52), (169, 181, 232), (241, 169, 155), (252, 7, 40), (10, 84, 100), (63, 98, 8), (14, 51, 250), (250, 11, 8)]
timmy.penup()
timmy.goto(-350,-350)
for n in range(10):
    for i in range(10):
        timmy.color(random.choice(color_list))
        timmy.dot(20)
        timmy.forward(70)
    y_pos = (n+1)*70-350
    timmy.goto(-350,y_pos)











screen.exitonclick()