import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().rstrip().split()))
    count = Counter(arr)
    
    cur = 1
    info = [[0, 0, 0] for _ in range(201)]
    for i in range(N):
        if count[arr[i]] < 6:
            continue
        if info[arr[i]][1] < 4:
            info[arr[i]][0] += cur
            info[arr[i]][1] += 1
        elif info[arr[i]][1] == 4 and info[arr[i]][2] == 0:
            info[arr[i]][2] = cur
        cur += 1
    
    score = sys.maxsize
    ans = 0
    for i in range(1, 201):
        if info[i][0] != 0 and score > info[i][0]:
            ans = i
            score = info[i][0]
        elif score == info[i][0]:
            if info[ans][2] > info[i][2]:
                ans = i
                
    print(ans)