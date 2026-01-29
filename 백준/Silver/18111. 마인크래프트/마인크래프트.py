import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
board = []
high = -1
low = 257
for _ in range(N):
    row = list(map(int, input().split()))
    for item in row:
        high = max(item, high)
        low = min(item, low)
    board.append(row)

ans = sys.maxsize
num = 0
for height in range(low, high + 1):
    cnt = B
    cur = 0
    for r in board:
        for c in r:
            if c > height:
                cur += 2 * (c - height)
                cnt += c - height
    for r in board:
        for c in r:
            if c < height:
                if cnt - (height - c) < 0:
                    cur = sys.maxsize
                    break
                cnt -= (height - c)
                cur += 1 * (height - c)
    if ans > cur:
        ans = cur
        num = height
    elif ans == cur:
        num = height
        
print(ans, num)