from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    
    for _, category in clothes:
        dic[category] += 1
        
    for value in dic.values():
        answer *= (value + 1)
    
    answer -= 1
    return answer