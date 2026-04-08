import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = []

for _ in range(R):
    board.append(list(input().rstrip()))
    
visited = [False for _ in range(26)]
visited[ord(board[0][0]) - 65] = True
ans = 0

def dfs(row, col, cnt, visited):
    global ans
    
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if 0 <= row + dr < R and 0 <= col + dc < C:
            if not visited[ord(board[row + dr][col + dc]) - 65]:
                visited[ord(board[row + dr][col + dc]) - 65] = True
                dfs(row + dr, col + dc, cnt + 1, visited)
                visited[ord(board[row + dr][col + dc]) - 65] = False
                
    ans = max(ans, cnt)

dfs(0, 0, 1, visited)

print(ans)