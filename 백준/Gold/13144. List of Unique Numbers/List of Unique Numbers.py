import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split()))

ans = 0
cnt = [0] * 100001
start = 0

for end in range(N):
    cnt[nums[end]] += 1
    
    while cnt[nums[end]] > 1:
        cnt[nums[start]] -= 1
        start += 1
        
    ans += (end - start + 1)
    
print(ans)