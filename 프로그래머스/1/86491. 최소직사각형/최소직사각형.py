def solution(sizes):    
    max_num = 0
    for row, col in sizes:
        max_num = max(max_num, row, col)
    
    rest = 0
    for row, col in sizes:
        rest = max(rest, min(row, col))
        
    return max_num * rest