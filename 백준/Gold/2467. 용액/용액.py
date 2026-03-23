import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

hap = float('inf')
left = 0
right = N - 1
ansLeft, ansRight = 0, 0

while left < right:
    cur = arr[left] + arr[right]
    
    if abs(cur) < hap:
        hap = abs(cur)
        ansLeft = left
        ansRight = right
    
    if cur == 0:
        break
    elif cur > 0:
        right -= 1
    else:
        left += 1

print(arr[ansLeft], arr[ansRight])