import sys
from collections import deque

input = sys.stdin.readline

S = input().rstrip()

cnt = S.count('a')

if cnt > 0:
    cur = deque(S[0 : cnt])
    ans = cur.count('b')
    tmp = cur.count('b')

    for i in range(cnt, cnt + len(S) - 1):
        if cur[0] == 'b':
            tmp -= 1
        
        cur.popleft()
        
        if S[i % len(S)] == 'b':
            tmp += 1
        
        cur.append(S[i % len(S)])
    
        ans = min(ans, tmp)
else:
    ans = 0

print(ans)