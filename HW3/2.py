a = [int(s) for s in input().split()]
imin = 0
imax = 0
for i in range(1, len(a)):
    if a[i] > a[imax]:
        imax = i
    if a[i] < a[imin]:
        imin = i
a[imin], a[imax] = a[imax], a[imin]
print(' '.join([str(i) for i in a]))
