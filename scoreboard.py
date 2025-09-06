from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "right"

class Scoreboard(Turtle):
    def __init__(self,level,life):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.write_level_life(level,life)

    def write_level_life(self,level,life):
        self.goto(-150, 250)
        self.write(f"Level: {level}", align="right", font=FONT)

        self.goto(180, 250)
        self.write(f"Lives: {life}", align="right", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def you_win(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=FONT)



