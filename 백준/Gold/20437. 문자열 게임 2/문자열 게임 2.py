import sys

input = sys.stdin.readline

T = int(input())

ans = []

for _ in range(T):
    W = input().rstrip()
    K = int(input())
    
    idx = [[] for _ in range(26)]
    
    for i in range(len(W)):
        idx[ord(W[i]) - 97].append(i)

    ans3 = float('inf')
    ans4 = -1
    
    for i in range(26):
        if len(idx[i]) >= K:
            for j in range(len(idx[i]) - K + 1):
                ans3 = min(ans3, idx[i][j + K - 1] - idx[i][j] + 1)
                ans4 = max(ans4, idx[i][j + K - 1] - idx[i][j] + 1)
                
    if ans3 == float('inf'):
        ans.append('-1\n')
    else:
        ans.append(str(ans3) + ' ' + str(ans4) + '\n')
        
print(''.join(ans))        