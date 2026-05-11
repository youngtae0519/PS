def solution(n, lost, reserve):
    clothes = [True] * (n + 1)
    
    for num in lost:
        clothes[num] = False
    
    rest = []
    for num in reserve:
        if not clothes[num]:
            clothes[num] = True
        else:
            rest.append(num)
            
    rest.sort()
    
    for num in rest:
        if num > 1 and not clothes[num - 1]:
            clothes[num - 1] = True
        elif num < n and not clothes[num + 1]:
            clothes[num + 1] = True
    
    return sum(clothes) - 1