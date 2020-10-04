import turtle
import numpy as np
turtle.shape('turtle')
turtle.speed(1)
for n in range(3, 13):
    turtle.penup()
    turtle.sety(-(5 * n / np.sin(np.pi / n)))
    turtle.pendown()
    turtle.circle((5 * n / np.sin(np.pi / n)), None, n)