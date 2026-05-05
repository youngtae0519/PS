def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt = [0] * 4
    
    for idx, num in enumerate(answers):
        if one[idx % len(one)] == num:
            cnt[1] += 1
        if two[idx % len(two)] == num:
            cnt[2] += 1
        if three[idx % len(three)] == num:
            cnt[3] += 1
            
    max_num = 0
    for i in range(1, 4):
        if cnt[i] > max_num:
            answer = [i]
            max_num = cnt[i]
        elif cnt[i] == max_num:
            answer.append(i)
    
    return answer