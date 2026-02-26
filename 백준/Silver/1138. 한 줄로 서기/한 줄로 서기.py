import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))

ans = []
for i in range(N - 1, -1, -1):
    ans.insert(arr[i], i + 1)
    
print(*ans)