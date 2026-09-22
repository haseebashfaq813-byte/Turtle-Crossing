import turtle


class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,250)
        self.level = 1
        self.write(f"Level = {self.level}",font =("ComicSans",15,"normal"))


    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}", font=("ComicSans", 15, "normal"))
