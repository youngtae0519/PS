import sys

input = sys.stdin.readline

A, B = map(str, input().rstrip().split())

ans = 50
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            cnt += 1
    ans = min(ans, cnt)
    
print(ans)