from collections import deque

def is_in_bound(row, col, n, m):
    return 0 <= row < n and 0 <= col < m

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dq = deque([[0, 0, 1]])
    
    while dq:
        row, col, cnt = dq.popleft()
        
        if visited[row][col]:
            continue
            
        visited[row][col] = True
        
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if is_in_bound(row + dr, col + dc, n, m):
                if not visited[row + dr][col + dc] and maps[row + dr][col + dc] == 1:
                    if row + dr == n - 1 and col + dc == m - 1:
                        return cnt + 1
                    dq.append([row + dr, col + dc, cnt + 1])
                
    return -1