import sys
from bisect import bisect_left

input = sys.stdin.readline

N, M = map(int, input().split())
names = []
limits = []

for _ in range(N):
    name, limit = map(str, input().split())
    names.append(name)
    limits.append(int(limit))

ans = []
for _ in range(M):
    ans.append(names[bisect_left(limits, int(input()))] + '\n')
    
print(''.join(ans))