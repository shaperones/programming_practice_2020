from random import random
import turtle


turtle.shape('turtle')
turtle.speed(10)
for i in range(100):
    turtle.forward(80 * random())
    turtle.right(360 * random())

