import sys
from collections import deque

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

dq = deque([T])
ans = 0

while len(dq) > 0:
    cur = dq.popleft()
    
    if len(cur) < len(S):
        continue
    elif len(cur) == len(S):
        if cur == S:
            ans = 1
            break
    else:
        if cur[-1] == 'A':
            dq.append(cur[:-1])
        if cur[0] == 'B':
            dq.append(cur[1:][::-1])
            
print(ans)