import turtle


def number(A, delta):  # А - индекс, записанный как список, delta - отступ вправо для написания в строку след. цифири
    delta2 = delta + 15
    turtle.penup()
    turtle.goto(A[0][0] + delta, A[0][1])  # к началу рисования цифири с учетом сдвига вправо для написания в строку
    turtle.pendown()
    for i in range(len(A) - 1):
        turtle.goto(A[i + 1][0] + delta, A[i + 1][1])  # бегает по координатам цифири и рисует ее
    return delta2  # возвращает сдвиг вправо для следующей цифири


x = 0
y = 0
coords = [(x, y), (x + 10, y), (x, y - 10), (x + 10, y - 10), (x, y - 20), (x + 10, y - 20)]
unus = [coords[2], coords[1], coords[5]]
quattuor = [coords[0], coords[2], coords[3], coords[5], coords[1]]
septem = [coords[0], coords[1], coords[2], coords[4]]
nihil = [coords[0], coords[1], coords[5], coords[4], coords[0]]

turtle.shape('turtle')
turtle.speed(1)
S = [unus, quattuor, unus, septem, nihil, nihil]  # почтовый индекс как список списков кортежей
delta = 0

for i in range(6):
    number(S[i], delta)
    delta = number(S[i], delta)  # подставляем в дельту дельту2, чтобы новую цифирь рисовать справа от этой


def coords_to_file():  # подготовим файл для следующего упражнения
    f = open("turtlecoords.txt", 'w')
    res = ""  # в переменную запишем особым образом координаты, а потом переменную запишем в файл
    for i in range(len(S)):
        res += str(i) + "\n"  # с новой строки записываем номер рисуемой цифири
        for coord in S[i]:  # S[i] - список из кортежей coord, которые в свою очередь состоят из пары х и у
            res += str(coord[0]) + " " + str(coord[1]) + "\n"  # с новой строки записываем х и у через пробел
    res += '6'  # для корректного выполнения следующего упражнения
    f.write(res)
    f.close()


coords_to_file()