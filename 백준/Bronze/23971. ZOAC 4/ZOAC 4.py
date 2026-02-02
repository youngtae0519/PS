import sys

input = sys.stdin.readline

H, W, N, M = map(int, input().split())

ans = 0
if W % (M + 1) == 0:
    ans += W // (M + 1)
else:
    ans += W // (M + 1) + 1

if H % (N + 1) == 0:
    ans *= H // (N + 1)
else:
    ans *= H // (N + 1) + 1
    
print(ans)