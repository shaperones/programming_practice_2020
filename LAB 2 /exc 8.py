import turtle

n = int(input())
turtle.shape('turtle')
for i in range(2 * n):
    turtle.left(90)
    turtle.forward(10 * (2 * i + 1))
    turtle.left(90)
    turtle.forward(10 * (2 * i + 1))

