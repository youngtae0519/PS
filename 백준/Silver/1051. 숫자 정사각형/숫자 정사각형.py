import sys

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [['' for _ in range(M)] for _ in range(N)]
for i in range(N):
    arr = input().rstrip()
    for j in range(M):
        matrix[i][j] = arr[j]

ans = 0
for row in range(N):
    for i in range(M): 
        for j in range(i, M):
            if matrix[row][i] == matrix[row][j]:
                if row + j - i < N and matrix[row + j - i][i] == matrix[row][i] and matrix[row + j - i][j] == matrix[row][j]:
                    ans = max(ans, (j - i + 1) ** 2)
                    
print(ans)