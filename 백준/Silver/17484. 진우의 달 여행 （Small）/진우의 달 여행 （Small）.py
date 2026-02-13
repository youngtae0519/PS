import sys

input = sys.stdin.readline

def isInBound(row, col):
    return 0 <= row < N and 0 <= col < M

def dfs(row, col, cur, way):
    global ans
    if row == N - 1:
        ans = min(ans, cur)
        return
    if way != 1:
        if isInBound(row + 1, col - 1):
            dfs(row + 1, col - 1, cur + matrix[row + 1][col - 1], 1)
    if way != 2:
        if isInBound(row + 1, col):
            dfs(row + 1, col, cur + matrix[row + 1][col], 2)
    if way != 3:
        if isInBound(row + 1, col + 1):
            dfs(row + 1, col + 1, cur + matrix[row + 1][col + 1], 3)

N, M = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
    
ans = sys.maxsize

for i in range(M):
    dfs(0, i, matrix[0][i], 0)
    
print(ans)