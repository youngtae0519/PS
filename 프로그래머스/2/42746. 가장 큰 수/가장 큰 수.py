def solution(numbers):
    answer = ''
    arr = []
    
    for i in range(len(numbers)):
        num = str(numbers[i])
        first = str(numbers[i])
        second = str(numbers[i])
        while len(first) < 4:
            first += num[0]
            second += num[-1]
        arr.append([first, second, num])
        
    arr.sort(key = lambda x : (x[0], x[1]), reverse = True)
    
    if arr[0][2] == "0":
        answer = '0'
    else:
        for _, _, num in arr:
            answer += num
    
    return answer