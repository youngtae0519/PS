import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))

cnt = 0
ans = []
while True:
    if cnt == N:
        break
    for i in range(N):
        if arr[i] == 0:
            ans.append(str(i + 1) + ' ')
            for j in range(i + 1):
                arr[j] -= 1
            break
    cnt += 1
    
print(''.join(ans))