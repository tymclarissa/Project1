import turtle
import time
import random

class Shape:
    def __init__(self, x, y, shape, color):
        pass  # REPLACE PASS WITH YOUR CODE

    def move(self):
        pass  # REPLACE PASS WITH YOUR CODE

    def hide(self):
        pass  # REPLACE PASS WITH YOUR CODE

    def show(self):
        pass  # REPLACE PASS WITH YOUR CODE


class Text:

    def __init__(self, x, y, text):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.goto(x, y)
        self.pen.color("black")

        )

    def write_text(self, text):
        pass  # REPLACE PASS WITH YOUR CODE


class Game:

    def __init__(self):
        pass  # REPLACE PASS WITH YOUR CODE

    def create_shape(self):
        pass  # REPLACE PASS WITH YOUR CODE

    def move_shapes(self):
        pass  # REPLACE PASS WITH YOUR CODE

    def on_shape_click(self, x, y):
        pass  # REPLACE PASS WITH YOUR CODE

    def update_timer(self):
        pass  # REPLACE PASS WITH YOUR CODE

    def start(self):
        pass  # REPLACE PASS WITH YOUR CODE


if __name__ == "__main__":
    def __init__(self, x, y, shape, color):
        self. shape = turtle.Turtle()
        self.shape.penup()
        self.shape.hideturtle(
        self.shape.speed(0)
        self.shape.goto(x, y)
        self.shape.color(color)
        self.shape.shape(shape)
        self.shape.shapesize(2, 2)

        def move(self):
            self.shape.sety(self.shape.ycor() - 20)

        def hide(self):
            self.shape.hideturtle()

        def show(self):
            self.shape.showturtle()

