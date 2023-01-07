STARTING_POSITION=[]  #constant in python, all capital letters
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
from turtle import Turtle

class Snake:
    def __init__(self):
        self.total=[]
        self.add_segment()

    def add_segment(self):
        for n in range(3):
            block = Turtle(shape="square")
            block.penup()
            block.color("white")
            block.setx(0-n*20)
            self.total.append(block)
        self.head=self.total[0]

    def extend(self):
        new = Turtle(shape="square")
        new.penup()
        new.color("white")
        x=self.total[-1].xcor()
        y=self.total[-1].ycor()
        new.goto(x,y)
        self.total.append(new)

        #add a new segment to the snake

    def move(self):
        for number in range(len(self.total)-1,0,-1):
            x = self.total[number - 1].xcor()
            y = self.total[number - 1].ycor()
            self.total[number].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.total:
            seg.goto(1000,1000)
        self.total.clear()
        self.add_segment()
