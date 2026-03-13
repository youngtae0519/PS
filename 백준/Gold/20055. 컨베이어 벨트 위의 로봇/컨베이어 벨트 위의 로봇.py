import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

belt = list(map(int, input().rstrip().split()))
dq = deque([])
cnt = 0
for item in belt:
    if item == 0:
        cnt += 1
    dq.append([item, False])

ans = 0
while True:
    ans += 1
    dq.appendleft(dq.pop())
    
    dq[N - 1][1] = False
    
    for i in range(N - 1, -1, -1):
        if not dq[i][1] and dq[i - 1][1] and dq[i][0] > 0:
            dq[i][1] = True
            dq[i][0] -=1
            if dq[i][0] == 0:
                cnt += 1
            dq[i - 1][1] = False
            
    dq[N - 1][1] = False
            
    if dq[0][0] > 0:
        dq[0][1] = True
        dq[0][0] -= 1
        if dq[0][0] == 0:
            cnt += 1
            
    if cnt >= K:
        print(ans)
        break