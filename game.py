from turtle import Turtle


class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.write('Game Over!', font=('Arial', 20, 'normal'), align='center')

