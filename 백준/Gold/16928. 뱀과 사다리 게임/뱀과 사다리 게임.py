import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(int)

for _ in range(N):
    x, y = map(int, input().split())
    graph[x] = y
    
for _ in range(M):
    u, v = map(int, input().split())
    graph[u] = v
    
visited = [False for _ in range(101)]
dq = deque([[1, 0]])
ans = float('inf')

while len(dq) > 0:
    cur = dq.popleft()
    pos, cnt = cur[0], cur[1]
    
    if pos == 100:
        ans = min(ans, cnt)
    
    if visited[pos]:
        continue
        
    visited[pos] = True
    
    for i in range(1, 7):
        if graph[pos + i] != 0:
            if graph[pos + i] <= 100 and not visited[graph[pos + i]]:
                dq.append([graph[pos + i], cnt + 1])
        else:
            if pos + i <= 100 and not visited[pos + i]:
                dq.append([pos + i, cnt + 1])
                
print(ans)