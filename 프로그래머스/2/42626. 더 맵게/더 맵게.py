import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    length = len(scoville)
    
    while length >= 2 and scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        length -= 1
    
    return answer if scoville[0] >= K else -1