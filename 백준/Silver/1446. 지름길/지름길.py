import sys

input = sys.stdin.readline

N, D = map(int, input().split())
info = []

for _ in range(N):
    start, end, dis = map(int, input().split())
    
    if end > D or (end - start) < dis:
        continue
    
    info.append([start, end, dis])
    
ans = [sys.maxsize for _ in range(D + 1)]
ans[0] = 0

for i in range(D + 1):
    ans[i] = min(ans[i], ans[i - 1] + 1)
    for item in info:
        if item[0] == i:
            ans[item[1]] = min(ans[item[1]], ans[item[0]] + item[2])

print(ans[-1])