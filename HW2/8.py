a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
for el in a:
    if el % 2 == 0:
        print(el, end=' ')