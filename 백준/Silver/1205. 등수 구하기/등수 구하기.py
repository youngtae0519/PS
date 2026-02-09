import sys

input = sys.stdin.readline

N, S, P = map(int, input().split())

tmp = list(map(int, input().rstrip().split()))

arr = []
for idx, item in enumerate(tmp):
    arr.append([item, idx])

arr.append([S, N])
arr.sort(key = lambda x : (-x[0], x[1]))

cur = sys.maxsize
grade = 0
cnt = 1
ans = -1
for i in range(min(P, N + 1)):
    if arr[i][0] < cur:
        cur = arr[i][0]
        grade += cnt
        cnt = 1
    elif arr[i][0] == cur:
        cnt += 1
    if arr[i][1] == N:
        ans = grade
        break
        
print(ans)