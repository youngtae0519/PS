import sys
import collections

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    deq = collections.deque()
    for i in range(N):
        deq.append([tmp[i], i])

    imp = []
    for item in deq:
        imp.append(item[0])
    imp.sort(reverse = True)
    
    idx = 0
    ans = 1
    while True:
        if imp[idx] == deq[0][0]:
            if deq[0][1] == M:
                print(ans)
                break
            else:
                idx += 1
                ans += 1
                deq.popleft()
        else:
            deq.append(deq.popleft())