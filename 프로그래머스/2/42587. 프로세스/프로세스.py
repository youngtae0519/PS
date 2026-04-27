import heapq
from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque([])
    hq = []
    
    for idx, item in enumerate(priorities):
        dq.append([idx, item])
        heapq.heappush(hq, -item)
    
    while True:
        cur = dq.popleft()
        
        if -hq[0] != cur[1]:
            dq.append(cur)
        else:
            answer += 1
            heapq.heappop(hq)
            if cur[0] == location:
                break
        
    return answer