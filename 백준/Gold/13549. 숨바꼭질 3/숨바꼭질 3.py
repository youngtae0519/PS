import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

time = [sys.maxsize for _ in range(200001)]
time[N] = 0

dq = deque([[N, 0]])

while len(dq) > 0:
    cur = dq.popleft()
        
    if cur[0] * 2 <= 200000 and time[cur[0] * 2] > cur[1]:
        time[cur[0] * 2] = cur[1]
        dq.append([cur[0] * 2, cur[1]])
        
    if cur[0] + 1 <= 200000 and time[cur[0] + 1] > cur[1] + 1:
        time[cur[0] + 1] = cur[1] + 1
        dq.append([cur[0] + 1, cur[1] + 1])
        
    if cur[0] - 1 >= 0 and time[cur[0] - 1] > cur[1] + 1:
        time[cur[0] - 1] = cur[1] + 1
        dq.append([cur[0] - 1, cur[1] + 1])
        
print(time[K])