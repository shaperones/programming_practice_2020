def distance(x1, y1, x2, y2):
    res = 0
    res = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
    return res


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))
