answer = 0

def dfs(idx, numbers, num, target):
    global answer
    if idx == len(numbers):
        if num == target:
            answer += 1
    else:
        dfs(idx + 1, numbers, num + numbers[idx], target)
        dfs(idx + 1, numbers, num - numbers[idx], target)

def solution(numbers, target):
    dfs(1, numbers, numbers[0], target)
    dfs(1, numbers, -numbers[0], target)
    
    return answer