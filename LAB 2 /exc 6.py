import turtle

n = int(input())
turtle.shape('turtle')

for i in range(n):
    turtle.forward(150)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(150)
    turtle.left(180 - 360 / n)
