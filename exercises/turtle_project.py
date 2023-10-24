"""TODO: Describe your scene program."""

__author__ = "730705250"

from turtle import Turtle, TurtleScreen, colormode, done, update
from random import random


def main() -> None:
    """Entrypoint of the scene."""
    colormode(1.0)  # I'm using floats for colors here.

    # Drawing a sky, with Bob
    bob: Turtle = Turtle()  # Named after Bob Ross.
    bob.hideturtle()
    screen: TurtleScreen = bob.getscreen()  # Get screen to do some fun things
    screen.setworldcoordinates(0, 0, 400, 400)  # Set consistent coordinates, make my like marginally easier
    screen.tracer(24, 16)  # Draw faster!!!
    draw_sky(bob, 1, 0.1, 0.1, 1, 0.9, 0.1)
    # Draw a sun, maybe
    bob.color(1, 1, 0.7)
    draw_360gon(bob, 200, 215, 150, True)
    # The ground too, I guess
    bob.color(0.2, 0.8, 0.3)
    draw_rectangle(bob, -25, -25, 450, 180, True)

    # Drawing some trees, with John
    john: Turtle = Turtle()  # I just thought it'd be funny to call this one John
    john.hideturtle()

    trees: int = 0
    while trees < 40:
        # "trees" is included in the "y" calculation to ensure "closer" trees are always in front
        draw_tree(john, (random() * 450) - 67.5, ((random() * 3) - (trees * 2.1) + 150))
        trees += 1

    # Signature
    ayu: Turtle = Turtle()
    ayu.hideturtle()
    ayu.color("white")
    ayu.pensize(2)
    draw_signature(ayu, 370, 20)

    update()
    done()


def draw_rectangle(turtle: Turtle, x: float, y: float, width: float, height: float, fill: bool = False) -> None:
    """Draw a rectangle with the given width and height. x and y denote the top left corner."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()

    if fill:
        turtle.begin_fill()

    i: int = 0
    while i < 4:
        if i % 2 == 0:
            turtle.forward(width)
        else:
            turtle.forward(height)
        turtle.left(90)
        i += 1

    if fill:
        turtle.end_fill()


def draw_triangle(turtle: Turtle, x: float, y: float, side_length: float, fill: bool = False) -> None:
    """Draw an equilateral triangle given a side length. x and y denote the bottom left corner."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()

    if fill:
        turtle.begin_fill()

    i: int = 0
    while i < 3:
        turtle.forward(side_length)
        turtle.left(120)
        i += 1

    if fill:
        turtle.end_fill()


def draw_tree(turtle: Turtle, x: float, y: float) -> None:
    """Draw a tree. x and y denote the bottom left corner."""
    size: float = 50
    # The trunk
    turtle.color(0.6 + random() * 0.1, 0.5 - random() * 0.1, 0.25 - random() * 0.1)
    draw_rectangle(turtle, x + size * 0.333, y, size * 0.333, size * 0.4, True)
    # The two triangle "leaves"
    turtle.color(0.4 - random() * 0.05, 0.8 + random() * 0.15, 0.6 - random() * 0.05)
    draw_triangle(turtle, x, y + (size * 0.4), size, True)
    draw_triangle(turtle, x, y + (size * 0.9), size, True)


def draw_360gon(turtle: Turtle, x: float, y: float, size: float, fill: bool = False) -> None:
    """Draws a 360-sided polygon. Close enough to a circle. x and y denote center."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.pendown()

    if fill:
        turtle.begin_fill()

    i: int = 0
    while i < 360:
        turtle.forward(size / 90)
        turtle.left(1)
        i += 1

    if fill:
        turtle.end_fill()


def draw_signature(turtle: Turtle, x: float, y: float) -> None:
    """Draw the author's signature. x and y indicate... somewhere (left center-ish)."""
    size: float = 7
    # Triangle
    draw_triangle(turtle, x, y, size)
    turtle.penup()
    # Caret (^)
    turtle.goto(x + size, y - size)
    turtle.pendown()
    turtle.setheading(60)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.penup()
    # Left angle bracket (<)
    turtle.setheading(55)
    turtle.forward(size * 1.1)
    turtle.setheading(145)
    turtle.pendown()
    turtle.forward(size * 0.9)
    turtle.right(110)
    turtle.forward(size * 0.9)
    turtle.penup()


def draw_sky(turtle: Turtle,
             init_r: float, init_g: float, init_b: float,
             end_r: float, end_g: float, end_b: float,
             ) -> None:
    """Draw a pretty sky covering the canvas."""
    turtle.width(2)

    i: int = 0
    loops: int = 410
    while i < loops:
        r: float = (init_r * (loops - i) / loops) + (end_r * i / loops)
        g: float = (init_g * (loops - i) / loops) + (end_g * i / loops)
        b: float = (init_b * (loops - i) / loops) + (end_b * i / loops)
        turtle.color(r, g, b)

        turtle.penup()
        turtle.goto(-10, i - 5)
        turtle.pendown()
        turtle.forward(410)
        i += 1


if __name__ == "__main__":
    main()
