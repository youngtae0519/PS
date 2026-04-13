import sys
input = sys.stdin.readline

N = int(input())
start = list(map(int, input().rstrip()))
end = list(map(int, input().rstrip()))

def simulate(start, first):
    bulb = start[:]
    cnt = 0
    
    if first:
        bulb[0] = 1 - bulb[0]
        bulb[1] = 1 - bulb[1]
        cnt += 1
        
    for i in range(1, N):
        if bulb[i - 1] != end[i - 1]:
            bulb[i - 1] = 1 - bulb[i - 1]
            bulb[i] = 1 - bulb[i]
            if i != N - 1:
                bulb[i + 1] = 1 - bulb[i + 1]
            cnt += 1
            
    if bulb == end:
        return cnt
    else:
        return float('inf')

first_on = simulate(start, True)
first_off = simulate(start, False)
ans = min(first_on, first_off)

print(ans if ans != float('inf') else -1)