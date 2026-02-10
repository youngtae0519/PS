import sys

input = sys.stdin.readline

N = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = price[0] * dis[0]
cur = price[0]

for i in range(1, N - 1):
    if cur > price[i]:
        cur = price[i]
    ans += cur * dis[i]

print(ans)