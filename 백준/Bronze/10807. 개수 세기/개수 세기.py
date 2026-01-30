import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
v = int(input())

ans = 0
for num in arr:
    if num == v:
        ans += 1
        
print(ans)