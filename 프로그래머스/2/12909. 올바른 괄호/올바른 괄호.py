def solution(s):
    answer = True
    stack = []
    
    for c in s:
        if c == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                answer = False
                break
            stack.pop()
            
    if len(stack) != 0:
        answer = False

    return answer