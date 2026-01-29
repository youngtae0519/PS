N = int(input())
arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append([i, [x, y]])

ans = [0 for _ in range(N)]

for i in range(N):
    cnt = 1
    for j in range(N):
        if arr[j][1][0] > arr[i][1][0] and arr[j][1][1] > arr[i][1][1]:
            cnt += 1
    ans[arr[i][0]] = cnt

for item in ans:
    print(item, end = " ")