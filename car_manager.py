import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_QUANTITY = 30


class CarManager(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(1.5,2.5)
        self.recycle(x_pos, y_pos)


    def recycle (self,x_pos,y_pos):
        self.color(random.choice(COLORS))
        self.goto(x_pos,y_pos)

    def move(self):
        self.backward(20)






