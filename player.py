import turtle
starting_position = (0,-280)

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(starting_position)


    def is_at_finishline(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def start_again(self):
        self.goto(starting_position)
        self.setheading(90)

    def move(self):
        self.forward(10)