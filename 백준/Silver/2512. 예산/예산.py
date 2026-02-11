import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

if sum(arr) <= M:
    print(max(arr))
else:
    left = 0
    right = max(arr)
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        for item in arr:
            tmp += min(item, mid)
        if tmp <= M:
            left = mid + 1
        else:
            right = mid - 1
    print(right)