import sys, heapq

input = sys.stdin.readline

N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))
    
pq = []
idx = [(N - 1) for _ in range(N)]
for i in range(N):
    heapq.heappush(pq, (-matrix[-1][i], i))

while N > 1:
    col = heapq.heappop(pq)[1]
    if idx[col] >= 0:
        idx[col] -= 1
        heapq.heappush(pq, (-matrix[idx[col]][col], col))
    N -= 1
    
print(-heapq.heappop(pq)[0])