from collections import defaultdict
from sys import stdin
clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    cl, th, val = line.split()
    clients[cl][th] += int(val)
for cl in sorted(clients):
    print(cl + ':')
    for th in sorted(clients[cl]):
        print(th, clients[cl][th])