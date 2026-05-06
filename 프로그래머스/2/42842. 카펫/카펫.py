def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for i in range((total // 2) + 1, 0, -1):
        if total % i != 0:
            continue

        if (2 * i + 2 * (total // i) - 4) == brown:
            answer = [i, total // i]
            break
            
    return answer