import turtle
import time
import player
import score
import car_manager
from player import starting_position

display = turtle.Screen()
display.setup(width=600, height=600)
display.tracer(0)

jhon = turtle.Turtle()
jhon.hideturtle()

score = score.Score()

car = car_manager.Car()


player_1 = player.Player()
display.listen()
display.onkeypress(player_1.move, "w")


game_is_on = True
while game_is_on:
    display.update()
    time.sleep(0.1)
    car.new_car()
    car.move_cars()

    for c in car.all_cars:
        if c.distance(player_1) < 20:
            game_is_on = False


    if  player_1.is_at_finishline():

        score.increase_level()
        car.increase_speed()
        player_1.start_again()


jhon.write("you lose",align="center", font=("ComicSans", 20, "bold"))


display.exitonclick()