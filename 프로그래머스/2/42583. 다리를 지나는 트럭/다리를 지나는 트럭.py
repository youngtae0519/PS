from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    idx = 0
    dq = deque()
    
    while True:
        if idx == len(truck_weights):
            answer += bridge_length - dq[-1][1] + 1
            break
            
        if len(dq) < bridge_length and weight - truck_weights[idx] >= 0:
            for item in dq:
                item[1] += 1
            if len(dq) > 0 and dq[0][1] == bridge_length:
                weight += dq[0][0]
                dq.popleft()
            weight -= truck_weights[idx]
            dq.append([truck_weights[idx], 1])
            idx += 1
            answer += 1
        else:
            rest = bridge_length - dq[0][1]
            weight += dq[0][0]
            answer += rest
            dq.popleft()
            
            for item in dq:
                item[1] += rest
    
    return answer