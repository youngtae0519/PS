def solution(progresses, speeds):
    answer = []
    arr = []
    
    for progress, speed in zip(progresses, speeds):
        if ((100 - progress) % speed) == 0:
            arr.append((100 - progress) // speed)
        else:
            arr.append(((100 - progress) // speed) + 1)
            
    day = arr[0]
    cnt = 1
    
    for i in range(1, len(arr)):
        if day >= arr[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day = arr[i]
    answer.append(cnt)
    return answer