import sys

input = sys.stdin.readline

N, D = map(int, input().split())
info = [[] for _ in range(D + 1)]

for _ in range(N):
    start, end, dis = map(int, input().split())
    
    if end > D or (end - start) < dis:
        continue
    
    info[start].append([end, dis])
    
ans = [sys.maxsize for _ in range(D + 1)]
ans[0] = 0

for i in range(D + 1):
    ans[i] = min(ans[i], ans[i - 1] + 1)
    for end, dis in info[i]:
        ans[end] = min(ans[end], ans[i] + dis)

print(ans[-1])