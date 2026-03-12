import sys
from collections import deque

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

dq = deque([T])
ans = 0

while len(dq) > 0:
    tmp = dq.popleft()
    
    if len(tmp) == len(S):
        if tmp == S:
            ans = 1
            break
            
    if len(tmp) > 0:
        if tmp[-1] == 'A':
            dq.append(tmp[:-1])
        if tmp[0] == 'B':
            dq.append(tmp[1:][::-1])
            
print(ans)     