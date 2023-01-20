from turtle import Turtle
import time


class Shooter(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.goto(position)
        self.tilt(90)
        self.x_move = 15

    def move_left(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over!', font=('Arial', 20, 'normal'), align='center')

