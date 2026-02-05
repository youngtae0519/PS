import sys, heapq

input = sys.stdin.readline

P = int(input())
ans = []
for _ in range(P):
    arr = input().rstrip().split()
    
    T = int(arr[0])
    num = list(map(int, arr[1 : ]))
    
    pq = list(map(int, arr[1 : ]))
    heapq.heapify(pq)
    cnt = 0
    while len(pq) != 0:
        cur = heapq.heappop(pq)
        for item in num:
            if cur == item:
                break
            if cur < item:
                cnt += 1
    
    ans.append(T)
    ans.append(" ")
    ans.append(cnt)
    ans.append("\n")
    
print(''.join(map(str, ans)))