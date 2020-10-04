import turtle
turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
for i in range(1, 20):
    turtle.circle(20 + 9 * i)
    turtle.left(180)
    turtle.circle(20 + 9 * i, -360)
    turtle.left(180)