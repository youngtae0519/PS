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
pq = []

for nv, nw in graph[1]:
    heapq.heappush(pq, (nw, nv))

while len(pq) > 0:
    cur = heapq.heappop(pq)
    w, v = cur[0], cur[1]
    
    if dist[v] < w:
        continue
        
    dist[v] = w

    for nv, nw in graph[v]:
        if dist[v] + nw < dist[nv]:
            heapq.heappush(pq, (dist[v] + nw, nv))
            
print(dist[N])