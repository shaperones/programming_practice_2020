n = int(input())
s = 0
k = 1
for i in range(1, n + 1):
    k *= i
    s += k
print(s)
