import turtle
turtle.shape('turtle')
turtle.speed(4)
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
for i in -20, 20:
    turtle.pu()
    turtle.goto(i, 60)
    turtle.pd()
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
turtle.pu()
turtle.goto(0, 50)
turtle.pd()
turtle.width(8)
turtle.left(90)
turtle.backward(20)
turtle.pu()
turtle.goto(20, 30)
turtle.pd()
turtle.pencolor('red')
turtle.circle(20, -180)
