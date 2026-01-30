import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
recommands = list(map(int, input().split()))
frames = []

for i in range(M):
    student = recommands[i]
    
    is_existed = False
    
    for j in range(len(frames)):
        if frames[j][0] == student:
            is_existed = True
            frames[j][1] += 1
            break
    
    if is_existed:
        continue
        
    if len(frames) < N:
        frames.append([student, 1, i])
    else:
        frames.sort(key = lambda x : (-x[1], -x[2]))
        frames.pop()
        frames.append([student, 1, i])
        
ans = sorted([f[0] for f in frames])
print(*ans)