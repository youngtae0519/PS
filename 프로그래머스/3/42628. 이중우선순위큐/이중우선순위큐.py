import heapq
from collections import defaultdict

def solution(operations):
    answer = []
    max_hq = []
    min_hq = []
    max_cnt = defaultdict(int)
    min_cnt = defaultdict(int)
    
    for op in operations:
        command, num = op.split()
        num = int(num)
        if command[0] == 'I':
            heapq.heappush(max_hq, -num)
            heapq.heappush(min_hq, num)
        elif num == 1:
            while True:
                if not max_hq or min_cnt[-max_hq[0]] == 0:
                    break
                min_cnt[-max_hq[0]] -= 1
                heapq.heappop(max_hq)
            if max_hq:
                max_cnt[-max_hq[0]] += 1
                heapq.heappop(max_hq)
        elif num == -1:
            while True:
                if not min_hq or max_cnt[min_hq[0]] == 0:
                    break
                max_cnt[min_hq[0]] -= 1
                heapq.heappop(min_hq)
            if min_hq:
                min_cnt[min_hq[0]] += 1
                heapq.heappop(min_hq)
    while True:
        if not max_hq or min_cnt[-max_hq[0]] == 0:
            break
        min_cnt[-max_hq[0]] -= 1
        heapq.heappop(max_hq)
        
    while True:
        if not min_hq or max_cnt[min_hq[0]] == 0:
            break
        max_cnt[min_hq[0]] -= 1
        heapq.heappop(min_hq)
    
    if max_hq and min_hq:
        answer = [-heapq.heappop(max_hq), heapq.heappop(min_hq)]
    else:
        answer = [0, 0]
        
    return answer