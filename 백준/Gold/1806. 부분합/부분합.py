import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))

start, end = 0, 0
total = num[0]
ans = float('inf')

while True:
    if start > end:
        break
    if total >= S:
        ans = min(ans, end - start + 1)
        total -= num[start]
        start += 1
    elif end < N - 1:
        end += 1
        total += num[end]
    else:
        total -= num[start]
        start += 1
        
print(ans if ans != float('inf') else 0)