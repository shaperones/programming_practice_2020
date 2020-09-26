n = 0
i = 1
max1 = 0
max2 = 0
while i != 0:
    i = int(input())
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2:
        max2 = i
print(max2)
