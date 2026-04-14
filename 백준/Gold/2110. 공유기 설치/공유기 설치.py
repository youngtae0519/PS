import sys
input = sys.stdin.readline

N, C = map(int, input().split())

pos = []
for _ in range(N):
    pos.append(int(input()))
    
pos.sort()
start = 1
end = pos[-1] - pos[0]
ans = 0

while start <= end:
    mid = (start + end) // 2
    cur = pos[0]
    count = 1
    
    for i in range(1, N):
        if pos[i] >= cur + mid:
            cur = pos[i]
            count += 1
            
    if count >= C:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
        
print(ans)