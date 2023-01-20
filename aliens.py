from turtle import Turtle


class Aliens(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.tilt(270)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.slow_x = 0.3
        self.y_move = 7
        self.goto(position)
        self.color("green")

    def move(self):
        self.backward(self.slow_x)

    def reverse_left(self):
        self.slow_x *= -1

    def reverse_right(self):
        self.slow_x *= -1

    def approach(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)
