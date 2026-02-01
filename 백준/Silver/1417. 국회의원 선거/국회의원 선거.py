import sys, heapq

input = sys.stdin.readline

N = int(input())

dasom = int(input())
pq = []
for _ in range(N - 1):
    heapq.heappush(pq, -int(input()))
    
ans = 0
while len(pq) != 0:
    num = -heapq.heappop(pq)
    if dasom > num:
        break
    ans += 1
    dasom += 1
    heapq.heappush(pq, -(num - 1))

print(ans)