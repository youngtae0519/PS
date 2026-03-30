import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

ans = 0

while True:
    visited = [[False] * N for _ in range(N)]
    check = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                dq = deque([[i, j]])
                idx = deque([[i, j]])
                total = board[i][j]
            
                while dq:
                    row, col = dq.popleft()
                    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        if 0 <= row + dr < N and 0 <= col + dc < N and not visited[row + dr][col + dc]:
                            if L <= abs(board[row][col] - board[row + dr][col + dc]) <= R:
                                check = True
                                visited[row + dr][col + dc] = True
                                dq.append([row + dr, col + dc])
                                idx.append([row + dr, col + dc])
                                total += board[row + dr][col + dc]
            
                total = total // len(idx)
            
                while idx:
                    row, col = idx.popleft()
                    board[row][col] = total
                    
    if not check:
        break
    
    ans += 1
                
print(ans)