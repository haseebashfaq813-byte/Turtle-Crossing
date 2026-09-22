import turtle
import random

colors = ["red","orange","yellow","green","blue","violet","purple"]


class Car(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.new_speed = 10
        self.penup()
        self.hideturtle()
        self.all_cars = []



    def new_car(self):

        random_num = random.randint(0,6)
        if random_num == 5:
            new_car = turtle.Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(colors))
            new_car.penup()
            new_car.setheading(0)
            new_car.goto(300,random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for x in self.all_cars:
            x.backward(self.new_speed)

    def increase_speed(self):
        self.new_speed += 10

