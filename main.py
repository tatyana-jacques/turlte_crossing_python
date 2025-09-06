import random
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

X_POS = [300,400,500,600,700,800,900,1000]
Y_POS = [-200,-150,-100,-50,0,50,100,150,200]
level = 0
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("white")
screen.title("TURTLE CROSSING")
screen.tracer(0)

player = Player()
cars = []
game_time = 0.2
scoreboard = Scoreboard(level)

screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True
index = 0
for pos in X_POS:
   cars.append(CarManager(pos,random.choice(Y_POS)))
while game_is_on:
   screen.update()
   time.sleep(game_time)
   for car in cars:
      car.move()
      if car.xcor()<=-300:
         car.recycle(random.choice(X_POS),Y_POS[index])
         index +=1
         if index >=len(Y_POS):
            index = 0
      if car.distance(player)<=30:
         scoreboard.game_over()
         game_is_on = False

      if player.ycor() >= 300:
         level += 1
         scoreboard.clear()
         scoreboard.write_level(level)
         player.refresh()
         game_time-=0.05
         print(game_time)


screen.exitonclick()