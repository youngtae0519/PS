import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dic = defaultdict(list)

for i in range(N - 1):
    for j in range(i + 1, N):
        dic[nums[i] + nums[j]].append([i, j])

ans = 0

for i in range(N):
    num = nums[i]
    for item in dic[num]:
        if i not in item:
            ans += 1
            break
        
print(ans)