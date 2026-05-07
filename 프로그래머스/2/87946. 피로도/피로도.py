answer = 0

def combinate(k, dungeons, visited, cnt):
    global answer
    
    for idx, (min_k, cost) in enumerate(dungeons):
        if visited[idx] or k < min_k or k - cost < 0:
            continue
        
        visited[idx] = True
        combinate(k - cost, dungeons, visited, cnt + 1)
        visited[idx] = False
        
    answer = max(answer, cnt)

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    combinate(k, dungeons, visited, 0)
            
    return answer 