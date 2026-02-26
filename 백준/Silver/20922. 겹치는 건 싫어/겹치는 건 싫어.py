import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().rstrip().split()))

start, end = 0, 0
cnt = [0 for _ in range(100001)]
ans = 0

while start < N:
    if cnt[arr[start]] < K:
        cnt[arr[start]] += 1
        start += 1
    else:
        cnt[arr[end]] -= 1
        end += 1
    ans = max(ans, start - end)
    
print(ans)