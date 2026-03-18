import sys
input = sys.stdin.readline

N = int(input())
height = list(map(int, input().rstrip().split()))

stack = [[1, height[0]]]
ans = [0]

for i in range(1, N):
    while stack:
        if stack[-1][1] > height[i]:
            ans.append(stack[-1][0])
            stack.append([i+1, height[i]])
            break
        else:
            stack.pop()
    
    if not stack:
        stack.append([i+1, height[i]])
        ans.append(0)
        
print(*ans)