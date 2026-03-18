import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().rstrip().split()))

maxHeight = max(block)
arr = []

for idx, item in enumerate(block):
    if item == maxHeight:
        arr.append(idx)

ans = 0

cur = 0
for i in range(arr[0]):
    if block[i] < cur:
        ans += (cur - block[i])
    else:
        cur = block[i]

for i in range(arr[0], arr[-1]):
    ans += (maxHeight - block[i])

cur = 0
for i in range(W-1, arr[-1], -1):
    if block[i] < cur:
        ans += (cur - block[i])
    else:
        cur = block[i]
        
print(ans)