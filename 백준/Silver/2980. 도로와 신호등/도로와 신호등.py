import sys

input = sys.stdin.readline

N, L = map(int, input().split())
arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    
ans = 0
cur = 0
for item in arr:
    ans += (item[0] - cur)
    cur = item[0]
    tmp = ans
    isRed = True
    isGreen = False
    while True:
        if tmp - item[1] < 0:
            break
        tmp -= item[1]
        isRed = False
        isGreen = True
        if tmp - item[2] < 0:
            break
        tmp -= item[2]
        isRed = True
        isGreen = False
    if isRed:
        ans += (item[1] - tmp)
    ans += 1
    cur += 1
ans += (L - cur)

print(ans)