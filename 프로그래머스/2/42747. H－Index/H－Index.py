def solution(citations):
    answer = 0
    
    citations.sort(reverse = True)
    
    for i in range(1, len(citations)):
        if (i + 1) > citations[i]:
            answer = min(i, citations[i - 1])
            break
    
    if answer == 0:
        answer = min(len(citations), citations[-1])
        
    return answer