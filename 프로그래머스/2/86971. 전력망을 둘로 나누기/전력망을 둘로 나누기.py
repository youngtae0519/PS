from collections import deque

def bfs(n, matrix):
    q = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    cnt = 1
    
    while q:
        cur = q.popleft()
        
        for i in range(1, n + 1):
            if matrix[cur][i] and not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
                
    return abs(n - 2 * cnt)
    
def solution(n, wires):
    answer = n
    matrix = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    
    for v1, v2 in wires:
        matrix[v1][v2] = True
        matrix[v2][v1] = True
        
    for v1, v2 in wires:
        matrix[v1][v2] = False
        matrix[v2][v1] = False
        answer = min(answer, bfs(n, matrix))
        matrix[v1][v2] = True
        matrix[v2][v1] = True
        
    return answer