from turtle import Turtle, Screen
import time
from food import Food
from snakes import Snake
screen = Screen()
screen.setup(width=600,  height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
# tims=[]

# for i in range(3):
#     tim = Turtle(shape="square")
#     tim.color("white")
#     tim.penup()
#     tim.goto(-(20*i),0)
#     tims.append(tim)

snake = Snake()
score = Turtle()
a=0
score.goto(0,280)
score.color("white")
score.ht()
food = Food()
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)  

life = True
while life:
    score.write(f"Score : {a}", False, align="center",font=(18))
    screen.update()
    time.sleep(0.1)   
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        a+=1
        snake.extend()
        score.clear()
    
    
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        score.goto(0,0)
        score.write("Game over!", False,align="center", font=(44) )
        screen.exitonclick()






        





screen.exitonclick()