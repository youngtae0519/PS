import sys, heapq

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [sys.maxsize for _ in range(100001)]

pq = []
heapq.heappush(pq, (0, N))
arr[N] = 0

while True:
    cur = heapq.heappop(pq)
    time, pos = cur[0], cur[1]
    
    if pos == K:
        print(time)
        break
        
    if pos - 1 >= 0 and time + 1 < arr[pos - 1]:
        heapq.heappush(pq, (time + 1, pos - 1))
        arr[pos - 1] = time + 1
    
    if pos + 1 <= 100000 and time + 1 < arr[pos + 1]:
        heapq.heappush(pq, (time + 1, pos + 1))
        arr[pos + 1] = time + 1
    
    if pos * 2 <= 100000 and time + 1 < arr[pos * 2]:
        heapq.heappush(pq, (time + 1, pos * 2))
        arr[pos * 2] = time + 1