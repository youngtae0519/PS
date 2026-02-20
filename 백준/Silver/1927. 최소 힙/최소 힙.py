import sys, heapq

input = sys.stdin.readline

N = int(input())
pq = []
ans = []

for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(pq, x)
    elif x == 0:
        if len(pq) > 0:
            ans.append(str(heapq.heappop(pq)) + '\n')
        else:
            ans.append('0\n')
print(''.join(ans))