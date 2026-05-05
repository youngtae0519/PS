import math

def is_prime(cur):
    for i in range(2, int(math.sqrt(cur)) + 1):
        if cur % i == 0:
            return False
        
    return True

def combinate(length, num, idx, cur, s):
    if len(cur) == length:
        tmp = int(cur)
        if tmp > 1 and is_prime(tmp):
            s.add(tmp)
    
    for i in range(len(num)):
        if not idx[i]:
            idx[i] = True
            combinate(length, num, idx, cur + num[i], s)
            idx[i] = False
    

def solution(numbers):
    num = []
    s = set()
    
    for n in numbers:
        num.append(n)
    
    idx = [False] * len(num)
    
    for i in range(1, len(num) + 1):
        combinate(i, num, idx, "", s)
    print(s)
    return len(s)