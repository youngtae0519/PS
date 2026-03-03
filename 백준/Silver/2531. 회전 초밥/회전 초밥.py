import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

sushi = []
for _ in range(N):
    sushi.append(int(input()))

ans = 0
for i in range(N):
    tmp = set()
    for j in range(k):
        tmp.add(sushi[(i + j) % N])
    if c not in tmp:
        tmp.add(c)
    ans = max(ans, len(tmp))

print(ans)