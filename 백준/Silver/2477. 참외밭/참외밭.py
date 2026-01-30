import sys
import collections

input = sys.stdin.readline

K = int(input())

x = 0
y = 0
deq = collections.deque()

for _ in range(6):
    way, dis = map(int, input().split())
    if way == 1 or way == 2:
        x = max(x, dis)
    else:
        y = max(y, dis)
    deq.append(dis)
        
while True:
    if (deq[0] == x and deq[1] == y) or (deq[0] == y and deq[1] == x):
        break
    deq.append(deq.popleft())

print(K * (x * y - deq[3] * deq[4]))