import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split()))

ans = N
cnt = [0 for _ in range(100001)]
cnt[nums[0]] = 1
start, end = 0, 0

while start < N:
    if end < N - 1:
        end += 1
        cnt[nums[end]] += 1
        
        if cnt[nums[end]] == 2:
            while nums[start] != nums[end]:
                ans += (end - start - 1)
                cnt[nums[start]] -= 1
                start += 1
            ans += (end - start - 1)
            cnt[nums[start]] -= 1
            start += 1
    elif end == N - 1:
        ans += (end - start)
        start += 1
    
print(ans)