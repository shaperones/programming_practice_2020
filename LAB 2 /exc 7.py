import turtle

n = int(input())
turtle.shape('turtle')
for i in range(36 * n):
    turtle.forward(0.1 * i)
    turtle.left(10)
