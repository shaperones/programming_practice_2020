def power(a, n):
    if a == 1:
        return 1
    elif n == 0:
        return 1
    elif n > 0:
        return a * power(a, n - 1)
    else:
        return 1/power(a, -n)


a = float(input())
n = float(input())
a = power(a, n)
print(a)