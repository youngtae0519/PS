import heapq
from collections import deque

def solution(genres, plays):
    answer = []
    dic = {}
    
    for i in range(len(genres)):
        if not dic.get(genres[i]):
            dic[genres[i]] = deque([plays[i], [plays[i], i]])
        else:
            dic[genres[i]][0] += plays[i]
            dic[genres[i]].append([plays[i], i])
    
    hq = []
    for value in dic.values():
        cnt = value.popleft()
        heapq.heappush(hq, [-cnt, list(value)])
    
    while hq:
        arr = heapq.heappop(hq)
        tmp = []
        for item in arr[1]:
            heapq.heappush(tmp, (-item[0], item[1]))
        
        for i in range(min(2, len(tmp))):
            answer.append(heapq.heappop(tmp)[1])
        
    return answer