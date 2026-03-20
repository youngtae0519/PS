import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])
    
visited = [float('inf') for _ in range(N + 1)]
visited[1] = 0
pq = []

for nv, nw in graph[1]:
    heapq.heappush(pq, (nw, 1, nv))

while len(pq) > 0:
    cur = heapq.heappop(pq)
    w, u, v = cur[0], cur[1], cur[2]
    
    if visited[u] + w > visited[v]:
        continue
        
    visited[v] = visited[u] + w

    for nv, nw in graph[v]:
        if visited[v] + nw < visited[nv]:
            heapq.heappush(pq, (nw, v, nv))
            
print(visited[N])