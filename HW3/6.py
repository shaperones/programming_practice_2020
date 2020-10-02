cyfr = [int(s) for s in input().split()]
was = set()
for num in cyfr:
    if num in was:
        print('YES')
    else:
        print('NO')
        was.add(num)