import sys, heapq
from collections import deque
input = sys.stdin.readline

ans = []
idx = 1
while True:
    N = int(input())
    
    if N == 0:
        break
        
    board = []
    dis = [[float('inf')] * N for _ in range(N)]
    
    for _ in range(N):
        board.append(list(map(int, input().split())))
        
    dis[0][0] = board[0][0]
    pq = []
    heapq.heappush(pq, [dis[0][0], 0, 0])
    
    while pq:
        cur, row, col = heapq.heappop(pq)
        
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            if 0 <= row + dr < N and 0 <= col + dc < N:
                if cur + board[row + dr][col + dc] < dis[row + dr][col + dc]:
                    dis[row + dr][col + dc] = cur + board[row + dr][col + dc]
                    pq.append([dis[row + dr][col + dc], row + dr, col + dc])
                    
    ans.append(f'Problem {idx}: {dis[N - 1][N - 1]}')
    
    idx += 1
    
print('\n'.join(ans))