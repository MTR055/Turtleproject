import time
import turtle as t
import player as p
import car_manager as c
import scoreboard
import scoreboard as s

my_screen  = t.Screen()
my_screen.screensize(600,600)
my_screen.tracer(0)
player1 = p.player_game()
cars = c.cars_crossing()
score = scoreboard.scoreboard()
my_screen.listen()
my_screen.onkey(player1.go_up,"Up")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    player1
    cars.create_cars()
    cars.move()
    for carss in cars.all_cars:
        if carss.distance(player1) < 10:
             game_is_on = False

    if player1.ycor() >280:
        score.increase_score()
        player1.level_up()
        cars.increase_speed()












my_screen.exitonclick()