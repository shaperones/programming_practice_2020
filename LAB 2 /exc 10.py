import turtle
turtle.shape('turtle')
turtle.speed(10)
for i in range(3):
    turtle.circle(50)
    turtle.left(180)
    turtle.circle(50, -360)
    turtle.left(60)