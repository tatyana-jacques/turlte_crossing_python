import random
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
X_POS = [300,350,400,450,500,550]
X_START = [300,400,500,600,700,800,900,1000]
Y_POS = [-200,-150,-100,-50,0,50,100,150,200]
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("white")
screen.title("TURTLE CROSSING")
screen.tracer(0)

player = Player()
cars = []
game_time = 0.1






screen.listen()
screen.onkey(player.move,"Up")


game_is_on = True
index = 0
for pos in X_START:
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




screen.exitonclick()