from turtle import Turtle, Screen
move = 30
class Paddle:
    def __init__(self):
        self.paddles_r=[]
        self.paddles_l=[]
        self.createpaddle_r()
        self.createpaddle_l()

    def createpaddle_r(self):
        self.positions=[(280,20),(280,0),(280,-20)]
        for i in range(3):
            self.pad = Turtle(shape="square")
            self.pad.goto(self.positions[i])
            self.pad.setheading(90)
            self.pad.penup()
            self.pad.color("white")
            self.paddles_r.append(self.pad)
    def createpaddle_l(self):
        self.positions=[(-280,20),(-280,0),(-280,-20)]
        for i in range(3):
            self.pad = Turtle(shape="square")
            self.pad.goto(self.positions[i])
            self.pad.penup()
            self.pad.setheading(90)
            self.pad.color("white")
            self.paddles_l.append(self.pad)
    def upr(self):
        for i in range(3):
            self.paddles_r[i].forward(10)
    def downr(self):
        for i in range(3):
            self.paddles_r[i].backward(10)
    def upl(self):
        for i in range(3):
            self.paddles_l[i].forward(10)
    def downl(self):
        for i in range(3):
            self.paddles_l[i].backward(10)