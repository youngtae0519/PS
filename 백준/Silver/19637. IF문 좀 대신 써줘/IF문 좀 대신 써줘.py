import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    chingho, power = map(str, input().split())
    arr.append((chingho, int(power)))

ans = []
for _ in range(M):
    power = int(input())
    left = 0
    right = N - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if power > arr[mid][1]:
            left = mid + 1
        else:
            right = mid - 1
    ans.append(arr[left][0] + '\n')
    
print(''.join(ans))