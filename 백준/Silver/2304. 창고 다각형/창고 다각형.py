import sys

input = sys.stdin.readline

N = int(input())

idx = []
high = -1
arr = []
for _ in range(N):
    L, H = map(int, input().split())
    arr.append([L, H])
    if H > high:
        idx = []
        idx.append(L)
        high = H
    elif H == high:
        idx.append(L)

arr.sort(key = lambda x : x[0])
idx.sort()

cur = arr[0][1]
ans = 0
before = 0
for i in range(1, N):
    if arr[i][1] > cur:
        ans += cur * (arr[i][0] - arr[before][0])
        cur = arr[i][1]
        before = i
    if arr[i][1] == high:
        break

if len(idx) == 1:
    ans += high
else:
    ans += high * (idx[-1] - idx[0] + 1)

cur = arr[-1][1]
before = N - 1
for i in range(N - 1, -1, -1):
    if arr[i][1] > cur:
        ans += cur * (arr[before][0] - arr[i][0])
        cur = arr[i][1]
        before = i
    if arr[i][1] == high:
        break
        
print(ans)