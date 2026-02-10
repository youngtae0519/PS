import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
pos = list(map(int, input().split()))

ans = max(pos[0], N - pos[-1])

for i in range(1, M):
    if (pos[i] - pos[i - 1]) % 2 == 0:
        ans = max(ans, (pos[i] - pos[i - 1]) // 2)
    else:
        ans = max(ans, (pos[i] - pos[i - 1]) // 2 + 1)
    
print(ans)