from turtle import Turtle


class Arrows(Turtle):
    def __init__(self, position, tilt):
        super().__init__()
        self.shape("classic")
        self.color("white")
        self.penup()
        self.tilt(tilt)
        self.goto(position)
        self.y_move = 1.2

    def attack(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def alien(self):
        self.tilt(90)

    def intercept(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)

