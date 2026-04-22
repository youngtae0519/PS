import sys
input = sys.stdin.readline

def find(x):
    if parent[x] < 0:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if parent[x] < parent[y]:
        parent[y] = x
    elif parent[y] < parent[x]:
        parent[x] = y
    else:
        parent[x] = y
        parent[y] -= 1
        
    return

N = int(input())
M = int(input())
parent = [-1] * (N + 1)

for i in range(N):
    arr = list(map(int, input().rstrip().split()))
    
    for j in range(N):
        if arr[j]:
            union(i + 1, j + 1)
            
plan = list(set(map(int, input().rstrip().split())))
root = find(plan[0])
ans = "YES"

for i in range(1, len(plan)):
    if root != find(plan[i]):
        ans = "NO"
        break
        
print(ans)