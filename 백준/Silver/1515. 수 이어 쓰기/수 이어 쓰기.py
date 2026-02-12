import sys

input = sys.stdin.readline

S = input().rstrip()
idx = 0
ans = 1

while True:
    num = str(ans)
    cnt = 0
    for i in range(len(num)):
        if idx + cnt >= len(S):
            break
        if S[idx + cnt] == num[i]:
            cnt += 1
    idx += cnt
    if idx >= len(S):
        print(ans)
        break
    ans += 1