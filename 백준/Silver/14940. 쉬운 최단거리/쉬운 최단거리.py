import sys
from collections import deque

input = sys.stdin.readline

matrix = []

n, m = map(int, input().split())

def isInBound(row, col):
    return 0 <= row < n and 0 <= col < m

start = [0, 0, 0]

for i in range(n):
    row = list(map(int, input().rstrip().split()))
    matrix.append(row)
    for j in range(m):
        if row[j] == 2:
            start[0], start[1] = i, j

q = deque([start])
ans = [[sys.maxsize for _ in range(m)] for _ in range(n)]
ans[start[0]][start[1]] = 0
row = [1, -1, 0, 0]
col = [0, 0, 1, -1]

while len(q) > 0:
    cur = q.popleft()
    r, c, cnt = cur[0], cur[1], cur[2]
    
    for dr, dc in zip(row, col):
        if isInBound(r + dr, c + dc) and matrix[r + dr][c + dc] == 1:
            if cnt + 1 < ans[r + dr][c + dc]:
                ans[r + dr][c + dc] = cnt + 1
                q.append([r + dr, c + dc, cnt + 1])

for i in range(n):
    for j in range(m):
        if ans[i][j] == sys.maxsize:
            if matrix[i][j] == 0:
                ans[i][j] = 0
            else:
                ans[i][j] = -1

for row in ans:
    print(*row)