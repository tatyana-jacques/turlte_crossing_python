import time
from turtle import Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("white")
screen.title("TURTLE CROSSING")
screen.tracer(0)


game_time = 0.1


game_is_on = True
while game_is_on:
   screen.update()
   time.sleep(game_time)

screen.exitonclick()