import sys
input = sys.stdin.readline

def change(b):
    return 1 if b == 0 else 0

def switch(bulb, idx):
    for i in [idx - 1, idx, idx + 1]:
        if 0 <= i < N:
            bulb[i] = change(bulb[i])

def simulate(now, goal, first):
    bulb = now[:]
    cnt = 0
    
    if first:
        switch(bulb, 0)
        cnt += 1
    
    for i in range(1, N):
        if bulb[i - 1] != goal[i - 1]:
            switch(bulb, i)
            cnt += 1
            
    return cnt if bulb == goal else float('inf')

N = int(input())
now = list(map(int, input().rstrip()))
goal = list(map(int, input().rstrip()))


res1 = simulate(now, goal, False)
res2 = simulate(now, goal, True)

ans = min(res1, res2)

print(ans if ans != float('inf') else -1)