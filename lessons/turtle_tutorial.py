from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

colormode(255)

leo.forward(50)
leo.left(30)
leo.right(40)


i: int = 0
leo.fillcolor(196, 196, 255)
leo.begin_fill()
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i += 1

leo.end_fill()


leo.penup()
leo.goto(-50, -20)
leo.pendown()

leo.color(99, 204, 250)
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

bob: Turtle = Turtle()
bob.goto(-50, -20)
bob.speed(50)
side_length: int = 300

j: int = 0
while(j < 10):
    i: int = 0
    while(i < 3):
        bob.forward(side_length)
        bob.left(121)
        i += 1
    side_length *= 0.99
    j += 1

done()
