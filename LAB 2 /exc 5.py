import turtle

turtle.shape('turtle')
for i in range(10):
    turtle.forward(10 * (2 * i + 1))
    turtle.left(90)
    turtle.forward(10 * (2 * i + 1))
    turtle.left(90)
    turtle.forward(10 * (2 * i + 1))
    turtle.left(90)
    turtle.forward(10 * (2 * i + 1))
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.pendown()