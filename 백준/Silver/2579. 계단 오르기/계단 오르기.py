import sys
input = sys.stdin.readline

N = int(input())

score = [0] * (N + 1)

for i in range(N):
    score[i + 1] = int(input())
    
ans = [[0, 0] for _ in range(N + 1)]
ans[1][0] = score[1]

if N > 1:
    ans[2][0] = score[1] + score[2]
    ans[2][1] = score[2]

for i in range(3, N + 1):
    ans[i][0] = ans[i - 1][1] + score[i]
    ans[i][1] = max(ans[i - 2][0], ans[i - 2][1]) + score[i]

print(max(ans[-1]))