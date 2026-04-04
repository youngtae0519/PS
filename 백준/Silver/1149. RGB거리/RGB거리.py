import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
color = []

for _ in range(N):
    color.append(list(map(int, input().split())))
    
ans = [[float('inf')] * 3 for _ in range(N)]
ans[0][0] = color[0][0]
ans[0][1] = color[0][1]
ans[0][2] = color[0][2]

for i in range(1, N):
    ans[i][0] = color[i][0] + min(ans[i - 1][1], ans[i - 1][2])
    ans[i][1] = color[i][1] + min(ans[i - 1][0], ans[i - 1][2])
    ans[i][2] = color[i][2] + min(ans[i - 1][0], ans[i - 1][1])
            
print(min(ans[-1]))