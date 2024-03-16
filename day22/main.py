from turtle import Turtle, Screen
from pad import Paddle
from ball import Ball
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
# screen.tracer(0)
pad = Paddle()
ball = Ball()

screen.listen()
screen.onkey((pad.upr), "Up")
screen.onkey((pad.downr), "Down")
screen.onkey((pad.upl), "w")
screen.onkey((pad.downl), "s")
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance() < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()