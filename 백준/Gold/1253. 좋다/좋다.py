import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.sort()
ans = 0

for i in range(N):
    num = nums[i]
    left = 0
    right = N - 1
    
    while left < right:
        cur = nums[left] + nums[right]
        
        if cur == num:
            if left != i and right != i:
                ans += 1
                break
            elif left == i:
                left += 1
            else:
                right -= 1
        elif cur > num:
            right -= 1
        else:
            left += 1

print(ans)