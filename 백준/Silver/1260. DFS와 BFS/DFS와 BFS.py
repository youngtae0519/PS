import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = defaultdict(list)
ans = []

def dfs(start, visited):
    s = [start]
    while len(s) > 0:
        n = s.pop()
        if not visited[n]:
            visited[n] = True
            ans.append(str(n) + ' ')
            for i in graph[n]:
                s.append(i)
                
def bfs(start, visited):
    q = deque([start])
    while len(q) > 0:
        n = q.popleft()
        if not visited[n]:
            visited[n] = True
            ans.append(str(n) + ' ')
            for i in graph[n]:
                q.append(i)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    
for value in graph.values():
    value.sort(reverse = True)

visited = [False] * (N + 1)

dfs(V, visited)

print(''.join(ans).rstrip())

visited = [False] * (N + 1)
ans = []

for value in graph.values():
    value.sort()

bfs(V, visited)
        
print(''.join(ans).rstrip())