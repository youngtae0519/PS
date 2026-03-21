import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))

stack = [[1, arr[0]]]
ans = [0]

for i in range(1, N):
    while stack:
        if stack[-1][1] > arr[i]:
            ans.append(stack[-1][0])
            stack.append([i+1, arr[i]])
            break
        else:
            stack.pop()
            
    if not stack:
        stack.append([i+1, arr[i]])
        ans.append(0)
        
print(*ans)