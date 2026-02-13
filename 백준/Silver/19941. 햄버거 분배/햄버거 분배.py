import sys

input = sys.stdin.readline

N, K = map(int, input().split())

pos = list(input().rstrip())
ans = 0
for i in range(N):
    if pos[i] == 'P':
        for j in range(-K, K + 1):
            if i + j < 0 or i + j >= N:
                continue
            if pos[i + j] == 'H':
                ans += 1
                pos[i + j] = ''
                break
print(ans)