from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        self.tims=[]
        self.create_snake()
        self.head = self.tims[0]
    def create_snake(self):
        for i in range(len(self.tims)):
            self.add_tims()
            i+=1
    
    def move(self):
        for i in reversed(range(1,len(self.tims))):
            self.tims[i].goto(self.tims[i-1].pos())
        self.tims[0].forward(20)
    
    
    def up(self):
        self.tims[0].setheading(90)
    
    def down(self):
        self.tims[0].setheading(270)
    
    def left(self):
        self.tims[0].setheading(180)
        
    def right(self):
        self.tims[0].setheading(0)
    
    
    def add_tims(self):
        i=0
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(-(20*i),0)
        self.tims.append(tim)
    def extend(self):
        self.add_tims()
        self.tims[-1].goto(self.tims[-2].pos())