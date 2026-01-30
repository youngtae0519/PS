import sys

input = sys.stdin.readline

X, Y = map(int, input().split())
N = int(input())
pos = []

for _ in range(N):
    way, dis = map(int, input().split())
    pos.append([way, dis])
    
way, dis = map(int, input().split())

ans = 0
for item in pos:
    if item[0] == way:
        ans += abs(dis - item[1])
    elif item[0] == 1:
        if way == 2:
            ans += min(item[1] + dis, 2 * X - (item[1] + dis)) + Y
        elif way == 3:
            ans += dis + item[1]
        elif way == 4:
            ans += dis + X - item[1]
    elif item[0] == 2:
        if way == 1:
            ans += min(item[1] + dis, 2 * X - (item[1] + dis)) + Y
        elif way == 3:
            ans += Y - dis + item[1]
        elif way == 4:
            ans += Y - dis + X - dis
    elif item[0] == 3:
        if way == 4:
            ans += min(item[1] + dis, 2 * Y - (item[1] + dis)) + X
        elif way == 1:
            ans += dis + item[1]
        elif way == 2:
            ans += dis + Y - item[1]
    elif item[0] == 4:
        if way == 3:
            ans += min(item[1] + dis, 2 * Y - (item[1] + dis)) + X
        elif way == 1:
            ans += X - dis + item[1]
        elif way == 2:
            ans += X - dis + Y - item[1]
            
print(ans)        