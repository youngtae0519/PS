from collections import defaultdict

def solution(phone_book):
    answer = True    
        
    cnt = defaultdict(int)
    s = set()
    for num in phone_book:
        cnt[int(num)] = 1
        s.add(len(num))

    s = list(s)

    for num in phone_book:
        for length in s:
            if len(num) <= length:
                continue
            if cnt[int(num) // (10 ** (len(num) - length))] == 1:
                answer = False
                break
        if not answer:
            break
                
    return answer