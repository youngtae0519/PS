def solution(word):
    answer = 0
    dic = {"E": 1, "I": 2, "O": 3, "U": 4}
    
    for idx, w in enumerate(word):
        if w == 'A':
            answer += 1
        elif idx == 4:
            answer += dic[w] + 1
        else:
            cnt = 6
            for i in range(4 - idx - 1):
                cnt = cnt * 5 + 1
            cnt *= dic[w]
            answer += cnt + 1
            
    return answer