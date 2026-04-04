import sys, heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [float('inf') for _ in range(N + 1)]
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    
    while pq:
        dis, cur = heapq.heappop(pq)
        
        if distance[cur] < dis:
            continue
            
        for item in graph[cur]:
            if distance[item[0]] > dis + item[1]:
                distance[item[0]] = dis + item[1]
                heapq.heappush(pq, (dis + item[1], item[0]))
                
    return distance

one_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_to_v2 = one_distance[v1] + v1_distance[v2] + v2_distance[N]
v2_to_v1 = one_distance[v2] + v2_distance[v1] + v1_distance[N]

ans = min(v1_to_v2, v2_to_v1)
print(ans if ans < float('inf') else -1)