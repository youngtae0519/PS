import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])
    
dist = [float('inf') for _ in range(N + 1)]
dist[1] = 0
pq = [(0, 1)]

while pq:
    w, v = heapq.heappop(pq)
    
    if dist[v] < w:
        continue

    for nv, nw in graph[v]:
        if dist[v] + nw < dist[nv]:
            dist[nv] = dist[v] + nw
            heapq.heappush(pq, (dist[v] + nw, nv))
            
print(dist[N])