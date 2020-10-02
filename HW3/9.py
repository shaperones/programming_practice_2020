counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

max_count = max(counter.values())
nya = [k for k, v in counter.items() if v == max_count]
print(min(nya))