import sys

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(1)
else:
    ans = 1
    N -= 1
    while True:
        if N <= 0:
            break
        N -= 6 * ans
        ans += 1
    print(ans)