import sys
from collections import deque

input = sys.stdin.readline

S = input().rstrip()
total = S.count('a')
cur = deque(S[0: total])
ans = cur.count('b')
tmp = cur.count('b')

if total == 0:
    ans = 0
else:
    for i in range(len(S)):
        left = cur.popleft()
        if left == 'b':
            tmp -= 1
        
        right = S[(i + total) % len(S)]
        cur.append(right)
        if right == 'b':
            tmp += 1
        
        ans = min(ans, tmp)

print(ans)