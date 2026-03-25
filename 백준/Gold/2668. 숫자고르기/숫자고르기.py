import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [0] * (N + 1)

for i in range(N):
    arr[i + 1] = int(input())

check = [False] * (N + 1)
ans = []

for i in range(1, N + 1):
    if not check[i]:
        cur = i
        dq = deque([cur])
        
        while True:
            check[cur] = True
            cur = arr[cur]
            
            if check[cur]:
                break
                
            dq.append(cur)
            
    while dq and dq[0] != cur:
        dq.popleft()
        
    while dq:
        ans.append(dq.popleft())

ans.sort()
ans = set(ans)

print(len(ans))
print('\n'.join(map(str,ans)))