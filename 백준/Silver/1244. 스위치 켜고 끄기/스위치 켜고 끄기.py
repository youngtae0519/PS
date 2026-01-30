import sys

input = sys.stdin.readline

N = int(input())
switch = [0] + list(map(int, input().split()))

T = int(input())
for _ in range(T):
    child, num = map(int, input().split())
    if child == 1:
        for i in range(num, N + 1, num):
            switch[i] = (switch[i] + 1) % 2
    else:
        cnt = 0
        while True:
            if num - cnt < 1 or num + cnt > N:
                break
            if switch[num - cnt] == switch[num + cnt]:
                cnt += 1
            else:
                break
        switch[num] = (switch[num] + 1) % 2
        for i in range(1, cnt):
            switch[num + i] = (switch[num + i] + 1) % 2
            switch[num - i] = (switch[num - i] + 1) % 2

for i in range(1, N + 1):
    if i % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end = " ")