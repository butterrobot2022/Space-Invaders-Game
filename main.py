from turtle import Screen
from shooter import Shooter
from aliens import Aliens
from arrows import Arrows
from random import *


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=550)
screen.tracer(0)

alien_list = []
second_alien_list = []
third_alien_list = []
spaceship = Shooter((-20, -200))
n = -280

for i in range(13):
    aliens = Aliens((n, 200))
    alien_list.append(aliens)
    second_row = Aliens((n, 160))
    second_alien_list.append(second_row)
    third_row = Aliens((n, 120))
    third_alien_list.append(third_row)
    n += 50
game_is_on = True
left_end = -350

arrow_list = []
second_arrow_list = []
third_arrow_list = []


def shoot():
    arrows = Arrows((spaceship.xcor(), spaceship.ycor() + 30), 90)
    arrow_list.append(arrows)


def defend():
    global second_alien_list
    for enemies in alien_list:
        if randint(1, 400) == 1:
            alien_arrows = Arrows((enemies.xcor(), enemies.ycor() - 30), 270)
            second_arrow_list.append(alien_arrows)
    for enemies in second_alien_list:
        if randint(1, 500) == 1:
            alien_arrows = Arrows((enemies.xcor(), enemies.ycor() - 30), 270)
            second_arrow_list.append(alien_arrows)
    for enemies in third_alien_list:
        if randint(1, 500) == 1:
            alien_arrows = Arrows((enemies.xcor(), enemies.ycor() - 30), 270)
            second_arrow_list.append(alien_arrows)


while game_is_on:
    screen.update()
    screen.onkey(spaceship.move_left, "Left")
    screen.onkey(spaceship.move_right, "Right")
    screen.onkey(shoot, "Up")
    screen.listen()
    defend()
    try:
        for arrows in arrow_list:
            arrows.attack()
            for alien in second_alien_list:
                if arrows.distance(alien) < 20 and arrows.ycor() > 150:
                    alien.hideturtle()
                    second_alien_list.remove(alien)
                    arrows.hideturtle()
                    arrow_list.remove(arrows)
                elif alien.distance(spaceship) < 20 and alien.ycor() < - 180:
                    game_is_on = False
                    spaceship.game_over()
            for alien in alien_list:
                if arrows.distance(alien) < 20 and arrows.ycor() > 190:
                    alien.hideturtle()
                    arrow_list.remove(arrows)
                    alien_list.remove(alien)
                    arrows.hideturtle()
                elif alien.distance(spaceship) < 20 and alien.ycor() < - 180:
                    game_is_on = False
                    spaceship.game_over()
            for alien in third_alien_list:
                if arrows.distance(alien) < 20 and arrows.ycor() > 110:
                    alien.hideturtle()
                    arrow_list.remove(arrows)
                    third_alien_list.remove(alien)
                    arrows.hideturtle()
                elif alien.distance(spaceship) < 20 and alien.ycor() < - 180:
                    game_is_on = False
                    spaceship.game_over()
        for alien in alien_list:
            alien.move()
            if alien.xcor() < left_end:
                alien.reverse_right()
                alien.approach()
            elif alien.xcor() > 350:
                alien.reverse_left()
                alien.approach()
        for alien in second_alien_list:
            alien.move()
            if alien.xcor() < left_end:
                alien.reverse_right()
                alien.approach()
            elif alien.xcor() > 350:
                alien.reverse_left()
                alien.approach()
        for alien in third_alien_list:
            alien.move()
            if alien.xcor() < left_end:
                alien.reverse_right()
                alien.approach()
            elif alien.xcor() > 350:
                alien.reverse_left()
                alien.approach()
        for arrows in second_arrow_list:
            arrows.intercept()
            if arrows.distance(spaceship) < 20 and arrows.ycor() < -180:
                game_is_on = False
                spaceship.game_over()

    except ValueError:
        pass
    if len(alien_list) == 0 and len(second_alien_list) == 0 and len(third_alien_list) == 0:
        game_is_on = False
        spaceship.game_over()

screen.exitonclick()
