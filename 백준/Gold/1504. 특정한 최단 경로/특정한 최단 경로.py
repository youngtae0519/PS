import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, E = map(int, input().split())

graph = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    
v1, v2 = map(int, input().split())

def dijkstra(start):
    dis = [float('inf')] * (N + 1)
    dis[start] = 0
    dq = deque([[start, 0]])
    
    while dq:
        u, c = dq.popleft()
            
        for neighbor, cost in graph[u]:
            if dis[u] + cost < dis[neighbor]:
                dis[neighbor] = dis[u] + cost
                dq.append([neighbor, cost])
                
    return dis

distance_one = dijkstra(1)
distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)

v1_to_v2 = distance_one[v1] + distance_v1[v2] + distance_v2[N]
v2_to_v1 = distance_one[v2] + distance_v2[v1] + distance_v1[N]
ans = min(v1_to_v2, v2_to_v1)

print(ans if ans != float('inf') else -1)