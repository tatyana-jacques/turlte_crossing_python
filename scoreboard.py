from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "right"

class Scoreboard(Turtle):
    def __init__(self,level):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.write_level(level)

    def write_level(self,level):
        self.goto(-150, 250)
        self.write(f"Level: {level}", align="right", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)



