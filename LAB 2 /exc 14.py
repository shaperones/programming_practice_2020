import turtle


def star(n):
    for i in range(n):
        turtle.forward(100)
        turtle.left(180 - 180 / n)


# работает для звезд с нечетным числом лучей

turtle.shape('turtle')
star(5)
turtle.pu()
turtle.goto(250, 0)
turtle.pd()
star(11)
