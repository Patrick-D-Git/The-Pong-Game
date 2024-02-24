from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.x_move = 10
        self.y_move = 10
        self.penup()
        self.move_speed = 0.1

    def move(self):
        set_y = self.ycor() + self.y_move
        set_x = self.xcor() + self.x_move
        self.goto(set_x, set_y)

    def bounce_y(self):

        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):

        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1

