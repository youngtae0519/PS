import heapq

def solution(jobs):
    answer = []
    time = 0
    hq = []
    idx = 0
    work = False
    n = len(jobs)
    jobs.sort(key = lambda x : x[0])
    
    while True:
        if work and time == end_time:
            work = False
            answer.append(end_time - start_time)
            if len(answer) == n:
                break
                
        while True:
            if idx == n or jobs[idx][0] > time:
                break
            heapq.heappush(hq, (jobs[idx][1], jobs[idx][0], idx))
            idx += 1
            
        if not work and hq and time >= hq[0][1]:
            work = True
            start_time = hq[0][1]
            end_time = time + hq[0][0]
            heapq.heappop(hq)
                
        time += 1
    
    return sum(answer) // n