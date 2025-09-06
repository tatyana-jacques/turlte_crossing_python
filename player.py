from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 100
FINISH_LINE_Y = 280
LIVES = 3

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self. speed("fastest")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.life = LIVES


    def move(self):
        self.forward(10)

    def refresh(self):
        self.clear()
        self.goto(STARTING_POSITION)





