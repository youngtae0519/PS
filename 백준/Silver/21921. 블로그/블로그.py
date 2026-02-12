import sys

input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

cur = sum(arr[0 : X])
left = 0
right = X - 1
ans = -1
cnt = 0

while True:
    if cur > ans:
        ans = cur
        cnt = 1
    elif cur == ans:
        cnt += 1
        
    right += 1
    if right == N:
        break
    cur += arr[right]
        
    cur -= arr[left]
    left += 1
    
if ans == 0:
    print("SAD")
else:
    print(ans, cnt, sep = '\n')